# Mobile Catalog RAG Agent

This project implements a Retrieval-Augmented Generation (RAG) agent for querying mobile catalog information. The agent can answer questions about pricing plans, discounts, and other mobile service-related queries.

## Prerequisites

- Python 3.x
- Azure AI Project credentials
- Environment variables set up (see Configuration section)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up the agent:
```bash
python agent_setup.py
```

## Configuration

1. Create a `.env` file with your Azure AI Project connection string:
```
PROJECT_CONNECTION_STRING=your_connection_string_here
```

2. Update the agent ID in [agent_test.py](agent_test.py#L17):
```python
agent_id = "asst_cjJBBmJYcmhCjuhiTs9PhlWe"  # Replace with your agent ID
```

## Usage

Run the test suite to verify the agent's functionality:
```bash
python agent_test.py
```

The test suite includes the following queries:
1. Smartphone pricing plans
2. Data plan options and prices
3. Discounts and promotional offers
4. PayPay point system
5. Eligibility requirements
6. Special mobile plans

## Example Output

Here's a sample of what the agent can answer:

```bash
python agent_test.py
Created thread, ID: thread_qZ2TviyBsc3o94Wscn339rce

Test 1: Check smartphone pricing plans
Created message, ID: msg_GIPQi4iXrexN0rK4NJAiPKy1
Created run, ID: run_TAie3LDQpWV7RfCfM9kTCQfZ
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:49:54+00:00
Message ID: msg_GIPQi4iXrexN0rK4NJAiPKy1
Content:
What smartphone pricing plans are available according to the catalog?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:49:57+00:00
Message ID: msg_i4YbomJAjfqrZAdMeh5rsgwM
Content:
The mobile catalog offers the following smartphone pricing plans:

1. **Basic Plans**:
    - **0-1GB**:
      - Regular price: ¥1,078/month
      - Discounted price: ¥980/month

    - **1-2GB**:
      - Regular price: ¥2,178/month
      - Discounted price: ¥1,980/month

    - **2-3GB**:
      - Regular price: ¥3,278/month
      - Discounted price: ¥2,980/month

2. **New Family Discounts**:
    - **4GB (Light)**:
      - Regular price: ¥2,728/month
      - Discounted price: ¥2,480/month for 12 months, then ¥2,580/month afterwards.

    - **20GB (Basic)**:
      - Regular price: ¥4,928/month
      - Discounted price: ¥4,480/month for 12 months, then ¥3,560/month afterwards【4:0†source】【4:1†source】.

3. **Unlimited Data Plan**:
    - **MeriHaru Unlimited Plus**:
      - Basic monthly fee: Regular price is ¥7,425/month, discounted to ¥6,750/month with various discounts such as "おうち割 光セット" and "新みんな家族割"【4:6†source】.

These plans provide options based on the data capacity required, including a high-use unlimited plan that takes advantage of several discount bundles.

Test 2: Check data plan options and prices
Created message, ID: msg_ohtikTuskooUb1ipDgtOUOsF
Created run, ID: run_x3tJ0pIS5d2VxBIqOtnC1EQ6
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:50:07+00:00
Message ID: msg_ohtikTuskooUb1ipDgtOUOsF
Content:
Can you provide details on the data plan options and their respective prices?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:50:10+00:00
Message ID: msg_CUijrBnshbt0fqIiP6V5KdbO
Content:
Here are the details of the data plan options and their respective prices according to the mobile catalog:

1. **Basic Data Plans**:
   - **0-1GB Data Plan**:
     - Monthly fee: ¥1,078 (discounted to ¥980)
   - **1-2GB Data Plan**:
     - Monthly fee: ¥2,178 (discounted to ¥1,980)
   - **2-3GB Data Plan**:
     - Monthly fee: ¥3,278 (discounted to ¥2,980)

2. **Light and Basic Data Plans**:
   - **4GB (Light Plan)**:
     - Monthly fee: ¥2,728 (discounted to ¥2,480 for the first 12 months, then ¥2,580)
   - **20GB (Basic Plan)**:
     - Monthly fee: ¥4,928 (discounted to ¥4,480 for the first 12 months, then ¥3,560)

3. **Unlimited Data Plan (MeriHaru Unlimited Plus)**:
   - Basic Monthly Fee: Regular price is ¥7,425 (discounted to ¥6,750 with various applicable discounts like "おうち割 光セット" and "新みんな家族割")【8:0†source】【8:1†source】【8:7†source】.

The above data plans cater to different data usage requirements, from low to high usage, including unlimited data options with various discount bundles.

Test 3: Check discounts and promotional offers
Created message, ID: msg_IXdJRAIa4rnJgYUsCGZUVWuQ
Created run, ID: run_a0N2ZTRgeh9ec6kMgrlWfZh5
Current run status: RunStatus.QUEUED
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:50:19+00:00
Message ID: msg_IXdJRAIa4rnJgYUsCGZUVWuQ
Content:
What discounts or promotional offers are mentioned in the catalog?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:50:22+00:00
Message ID: msg_fs8aQYLAQxcobSBSCUhyS8b6
Content:
The mobile catalog provides several discounts and promotional offers, including:

1. **おうち割 (Home Discount)**:
    - Discount for combining mobile and fixed communication services such as SoftBank 光.
    - Up to 10 lines can be included for a discount of ¥1,100/month per eligible line.

2. **PayPay Benefits**:
    - Discounts for users who link their SoftBank accounts with PayPay.
    - Cashback campaigns where users earn PayPay points based on their expenditure【12:0†source】【12:2†source】.

3. **LINE MUSIC for SoftBank**:
    - Free 6 months for SoftBank users when they subscribe to the LINE MUSIC for SoftBank plan.
    - Discounted rates after the free period: ¥980/month for the general plan and ¥480/month for the student plan【12:16†source】.

4. **ハートフレンド割引 (Heart Friend Discount)**:
    - Available for individuals holding various disability certifications.
    - Offers basic plan discounts and reductions in option service fees【12:7†source】【12:13†source】.

5. **Purchase Discount Program**:
    - Discounts on new devices when the old device is traded in.
    - PayPay points as an alternative benefit for trading in old devices【12:6†source】【12:14†source】.

These discounts and promotional offers help customers reduce their overall costs and benefit from additional services linked to their mobile usage.

Test 4: Check PayPay point system
Created message, ID: msg_kNUeOB5Z6dUpgTUo4L11AsDn
Created run, ID: run_zGUvrjifiV5vP5IsXUeZD9p2
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:50:32+00:00
Message ID: msg_kNUeOB5Z6dUpgTUo4L11AsDn
Content:
How does the PayPay point system work as described in the document?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:50:35+00:00
Message ID: msg_pCnNlPuSh7N9m1gLrioPbkTT
Content:
The PayPay point system works as follows according to the mobile catalog:

1. **Earning PayPay Points**:
    - Users can earn PayPay points by linking their SoftBank account with PayPay.
    - For every ¥200 spent, users earn PayPay points, with different rates applied based on the type of purchase and promotion.
    - Specific point allocation examples include up to 1.5% or 3% of the spend, depending on the service used【16†source】【16†source】【17†source】.

2. **Conditions and Limitations**:
    - Points are not transferable or redeemable for cash.
    - Rewards and point conversions have specific conditions, such as required account linking and meeting the minimum spend criteria.
    - Certain charges such as device fees, optional services, and some family communication fees do not qualify for points【16†source】【17†source】.

3. **Usage and Conversion**:
    - Points can be used at PayPay or PayPay Card official stores.
    - PayPay points earned from SoftBank services can be exchanged for PayPay points through a specific procedure indicated in the PayPay app【16†source】.

4. **Account Linking and Requirements**:
    - Users must link their PayPay account to a Yahoo! JAPAN ID with smart login setup to receive points.
    - Family cards may have different rates or be excluded from earning points under certain conditions【17†source】.

These detailed conditions ensure that users can earn valuable rewards while utilizing their SoftBank services in conjunction with PayPay.

Test 5: Check eligibility requirements
Created message, ID: msg_5KWjfjDUDRyLk9lLVNITW8qe
Created run, ID: run_L18iSWS0KvIT5OG16gkxsq4m
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:50:45+00:00
Message ID: msg_5KWjfjDUDRyLk9lLVNITW8qe
Content:
What are the eligibility requirements for the special mobile plans listed?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:50:49+00:00
Message ID: msg_tAd1FK1nqqlxnxdLKrpNXwem
Content:
The eligibility requirements for special mobile plans specified in the catalog are summarized as follows:

1. **スマホデビュープラン＋**:
   - This plan is not available to users who previously had contracts for "データプラン4GB（スマホ）", "データプラン20GB（スマホ）", "データプラン4GB（ケータイ）", "データプラン3GB（スマホ）", or "データプラン3GB（ケータイ)"【20:0†source】.
   - Applicable devices are restricted to iPhone and smartphones (Windows Mobile and prepaid phones are excluded).
   - The plan is not eligible for data-sharing services.
   - Cannot be combined with "おうち割 光セット", "長期継続特典", "ワイモバイル→ソフトバンクのりかえ特典" (特典B).

2. **1年おトク割＋** (1-Year Discount):
   - Applies if there is a new subscription to "データプラン20GB（スマホ）", "データプラン4GB（スマホ）", or "データプラン4GB（ケータイ）" excluding prior users of these plans.
   - Also applies if an existing "データプラン3GB（スマホ）" or "データプラン3GB（ケータイ)" user switches from a feature phone to a smartphone (iPhone or other) and continues or starts a new subscription to the specified data plans.
   - Cannot be applied if it has already been used or is currently active【20:1†source】【20:5†source】.

3. **60歳以上通話おトク割** (Discount for Users 60+):
   - Available for users aged 60 and above, verified with relevant IDs (driver's license, My Number card, etc.).
   - Only one line per eligible user is allowed.
   - Business accounts are excluded.
   - Period: November 16, 2022, to an unspecified end date【20:8†source】【20:17†source】.

These requirements ensure that only qualifying users can access the specified benefits of these special plans.

Test 6: Check special mobile plans
Created message, ID: msg_ksImyszMARDzmJA86LtzCsMq
Created run, ID: run_RiuGTjlHUQgE7r2HNZ1ipH3L
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.IN_PROGRESS
Current run status: RunStatus.COMPLETED

Latest message exchange:

-------------------
Role: MessageRole.USER
Created at: 2025-02-18 23:51:01+00:00
Message ID: msg_ksImyszMARDzmJA86LtzCsMq
Content:
What smartphone pricing plans are available according to the catalog?

-------------------
Role: MessageRole.AGENT
Created at: 2025-02-18 23:51:02+00:00
Message ID: msg_Hw7agZ86uLx8lj2PLURzUn79
Content:
The mobile catalog offers the following smartphone pricing plans:

1. **Basic Plans**:
    - **0-1GB**:
      - Regular price: ¥1,078/month
      - Discounted price: ¥980/month

    - **1-2GB**:
      - Regular price: ¥2,178/month
      - Discounted price: ¥1,980/month

    - **2-3GB**:
      - Regular price: ¥3,278/month
      - Discounted price: ¥2,980/month

2. **New Family Discounts**:
    - **4GB (Light)**:
      - Regular price: ¥2,728/month
      - Discounted price: ¥2,480/month for 12 months, then ¥2,580/month afterwards.

    - **20GB (Basic)**:
      - Regular price: ¥4,928/month
      - Discounted price: ¥4,480/month for 12 months, then ¥3,560/month afterwards【4:0†source】【4:1†source】.

3. **Unlimited Data Plan**:
    - **MeriHaru Unlimited Plus**:
      - Basic monthly fee: Regular price is ¥7,425/month, discounted to ¥6,750/month with various discounts such as "おうち割 光セット" and "新みんな家族割"【4:6†source】.

These plans provide options based on the data capacity required, including a high-use unlimited plan that takes advantage of several discount bundles.
Deleted thread, ID: thread_qZ2TviyBsc3o94Wscn339rce
```