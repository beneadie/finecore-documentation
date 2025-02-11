Customer Wallet
===============


Create Customer Wallet
----------------------

**Description:**

This endpoint creates a customer wallet. The required fields are bvn, first_name, last_name, date_of_birth, phone_number, email, and address.

**Endpoint:**

POST  https://stagingapi.finecore.co/v1/wallets

**Request JSON Example:**

.. code-block:: json

     { "bvn": "11317307361",
    "first_name": "Ben",
    "last_name": "Testing",
    "date_of_birth": "12-11-2003",
    "phone_number": "08023094111",
    "email": "bentesting@finecore.co",
    "address": "No 10, Adewale Ajasin University" }

**Response JSON Example:**

.. code-block:: json

     { "statusCode": 201,
     "status": "success",
     "data": {
          "id": "e0aec692-0de0-4857-b448-471645f46ebd",
          "merchant_id": "b2da9c0a-cd46-4100-989a-db0641e1f532",
          "environment": "SANDBOX",
          "currency": "NGN",
          "bank_name": "Xpresswallet",
          "bank_code": "100040",
          "account_name": "Ben Testing",
          "account_number": "4458333576",
          "updated_at": "2025-02-11T06:51:10.915007Z",
          "created_at": "2025-02-11T06:51:10.915007Z",
          "booked_balance": 0,
          "available_balance": 0,
          "status": "ACTIVE",
          "updated": false,
          "wallet_type": "Customer",
          "user_id": "bec56c05-1257-47b0-9d4b-46a6c256999a" }
          }

**Python Demonstration:**

.. code-block:: python

   import requests
   import json

   url = "https://stagingapi.finecore.co/v1/wallets"
   api_key = "your-api-key-here"  # Replace with your actual API key

   payload = {
       "bvn": "11317307361",
       "first_name": "Ben",
       "last_name": "Testing",
       "date_of_birth": "12-11-2003",
       "phone_number": "08023094123",
       "email": "bentesting@finecore.co",
       "address": "No 10, Adewale Ajasin University"
   }

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.post(url, headers=headers, data=json.dumps(payload))




Credit Customer
---------------

**Description:**

This endpoint credits a customer wallet. The required fields are amount and customer_id.

**Endpoint:**

POST  https://stagingapi.finecore.co/v1/wallets/credit

**Request JSON Example:**

.. code-block:: json

     { "amount": 200,
        "customer_id": "e0aec692-0de0-4857-b448-471645f46ebd",
        "metadata": {
        "reason": "for test example" }
        }

**Response JSON Example:**

.. code-block:: json

     {"FIX": "ADD THIS WHEN POSTMAN WORKING AGAIN"}

**Python Demonstration:**

This is an example documentation using reStructuredText.

.. code-block:: python

   print("Fix when postman is working again")





Fetch Specific Wallet
---------------------

**Description:**

This endpoint fetches a specific customer wallet. The required fields are customer_id.

**Endpoint:**

GET   https://stagingapi.finecore.co/v1/wallets/{{customer_id}}


**Response JSON Example:**

.. code-block:: json

     {"FIX": "ADD THIS WHEN POSTMAN WORKING AGAIN"}

**Python Demonstration:**

This is an example documentation using reStructuredText.

.. code-block:: python

   import requests

   customer_id = "your-customer-id-here"  # Replace with the actual customer ID
   url = f"https://stagingapi.finecore.co/v1/wallets/{customer_id}"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)

   if response.status_code == 200:
       print("Success!")
       print(response.json())
   else:
       print("Failed with status code:", response.status_code)
       print(response.text)




Fetch All Customer Wallets
--------------------------

**Description:**

This endpoint initiates a bank transfer. The required fields are bvn, first_name, last_name, date_of_birth, phone_number, email and address.

**Endpoint:**

GET   https://stagingapi.finecore.co/v1/wallets



**Response JSON Example:**

.. code-block:: json

     {"FIX": "ADD THIS WHEN POSTMAN WORKING AGAIN"}

**Python Demonstration:**

This is an example documentation using reStructuredText.

.. code-block:: python

   import requests

   url = "https://stagingapi.finecore.co/v1/wallets"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)
