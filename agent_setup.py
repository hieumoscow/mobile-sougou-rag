import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import (
    FunctionTool,
    ToolSet,
    FileSearchTool,
    FilePurpose
)

load_dotenv()

# Create an Azure AI Client
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Upload specialists.json and create vector store
mobile_sougou_file = project_client.agents.upload_file_and_poll(
    file_path='./mobile-sougou.pdf',
    purpose=FilePurpose.AGENTS
)
print(f"Uploaded  file, file ID: {mobile_sougou_file.id}")

# Create vector store for specialists data
file_vector_store = project_client.agents.create_vector_store_and_poll(
    file_ids=[mobile_sougou_file.id],
    name="mobile_sougou_vectorstore"
)
print(f"Created specialists vector store, vector store ID: {file_vector_store.id}")

# Create file search tool for specialists data
file_search_tool = FileSearchTool(vector_store_ids=[file_vector_store.id])

# Initialize agent toolset with function and file search tools
toolset = ToolSet()
toolset.add(file_search_tool)

agent = project_client.agents.create_agent(
    model="gpt-4o",
    name="Mobile-Sougou-agent",
    instructions="""You are an AI agent specialized in retrieving and summarizing information from the mobile catalog document (mobile-sougou.pdf). 
    When a user asks a question, search the document for relevant information and provide a clear, concise answer with supporting citations from the document. 
    If a query is ambiguous, ask for clarification before answering. 
    Your responses should accurately reflect the details about mobile plans, pricing, service features, and promotional offers contained in the catalog.
    """,
    tools=file_search_tool.definitions,
    tool_resources=file_search_tool.resources,
    toolset=toolset
)

print(f"Created Mobile-Sougou agent, ID: {agent.id}")