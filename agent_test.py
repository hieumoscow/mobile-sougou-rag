import os
import time
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_result

load_dotenv()

# Create an Azure AI Client
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Get the agent by ID
agent_id = "asst_cjJBBmJYcmhCjuhiTs9PhlWe"  # Replace with your agent ID
agent = project_client.agents.get_agent(agent_id)

# Initialize thread as None
thread = None


def is_not_complete(run_status):
    """Check if the run is not complete."""
    return run_status.status in ["queued", "in_progress", "requires_action"]

@retry(stop=stop_after_attempt(60), wait=wait_fixed(1), retry=retry_if_result(is_not_complete))
def wait_for_run_completion(thread_id: str, run_id: str):
    """Wait for the run to complete with retries."""
    run = project_client.agents.get_run(thread_id=thread_id, run_id=run_id)
    print(f"Current run status: {run.status}")
    return run

def cancel_run_if_needed(thread_id: str, run_id: str):
    """Cancel a run if it's still active."""
    try:
        run = project_client.agents.get_run(thread_id=thread_id, run_id=run_id)
        if run.status in ["queued", "in_progress", "requires_action"]:
            project_client.agents.cancel_run(thread_id=thread_id, run_id=run_id)
            print(f"Cancelled run {run_id}")
    except Exception as e:
        print(f"Error cancelling run: {str(e)}")

def send_message_and_wait(message: str):
    """Send a message and wait for the run to complete."""
    try:
        # Create message in thread
        message_obj = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=message
        )
        print(f"Created message, ID: {message_obj.id}")

        # Create and run the agent
        run = project_client.agents.create_run(
            thread_id=thread.id,
            assistant_id=agent.id
        )
        print(f"Created run, ID: {run.id}")

        # Monitor the run status with retries
        try:
            run = wait_for_run_completion(thread.id, run.id)
        except Exception as e:
            print(f"Run timed out or failed: {str(e)}")
            cancel_run_if_needed(thread.id, run.id)
            return False

        # Check final run status
        if run.status == "failed":
            print(f"Run failed with error: {run.last_error}")
            return False
        elif run.status != "completed":
            print(f"Run ended with unexpected status: {run.status}")
            return False

        return True

    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return False

def print_thread_messages(last_printed_time=None):
    """Print messages in the thread after the last_printed_time."""
    try:
        # Get all messages in the thread
        messages = project_client.agents.list_messages(thread_id=thread.id)
        
        # Find messages to print (messages after last_printed_time)
        messages_to_print = []
        for msg in messages.data:
            msg_time = msg.created_at
            if last_printed_time is None or msg_time > last_printed_time:
                messages_to_print.append(msg)
        
        if not messages_to_print:
            print("No new messages found")
            return last_printed_time
            
        # Sort messages by creation time
        messages_to_print.sort(key=lambda x: x.created_at)
        
        # Print messages in a structured format
        print("\nLatest message exchange:")
        for msg in messages_to_print:
            print("\n-------------------")
            print(f"Role: {msg.role}")
            print(f"Created at: {msg.created_at}")
            print(f"Message ID: {msg.id}")
            print("Content:")
            for content in msg.content:
                if content.type == 'text':
                    print(content.text.value)
        
        # Return the timestamp of the latest message printed
        return messages_to_print[-1].created_at if messages_to_print else last_printed_time
            
    except Exception as e:
        print(f"Error printing messages: {str(e)}")
        return last_printed_time

def test_agent():
    # Create a thread
    global thread
    thread = project_client.agents.create_thread()
    print(f"Created thread, ID: {thread.id}")

    test_cases = [
        ("Test 1: Check smartphone pricing plans", "What smartphone pricing plans are available according to the catalog?"),
        ("Test 2: Check data plan options and prices", "Can you provide details on the data plan options and their respective prices?"),
        ("Test 3: Check discounts and promotional offers", "What discounts or promotional offers are mentioned in the catalog?"),
        ("Test 4: Check PayPay point system", "How does the PayPay point system work as described in the document?"),
        ("Test 5: Check eligibility requirements", "What are the eligibility requirements for the special mobile plans listed?"),
        ("Test 6: Check special mobile plans", "What smartphone pricing plans are available according to the catalog?")
    ]

    last_printed_time = None
    for test_name, query in test_cases:
        print(f"\n{test_name}")
        if not send_message_and_wait(query):
            print("Failed to get response, stopping conversation")
            break
        last_printed_time = print_thread_messages(last_printed_time)
        time.sleep(5)  # Small delay between messages

    # Delete the thread
    project_client.agents.delete_thread(thread_id=thread.id)
    print(f"Deleted thread, ID: {thread.id}")

if __name__ == "__main__":
    test_agent()
