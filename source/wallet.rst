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

This endpoint credits a customer wallet. The required fields are amount, customer_id and metadata. The request can have success or fail if the account owner doesn't have the funds.

**Endpoint:**

POST  https://stagingapi.finecore.co/v1/wallets/credit

**Request JSON Example:**

.. code-block:: json

     { "amount": 200,
        "customer_id": "bec56c05-1257-47b0-9d4b-46a6c256999a",
        "metadata": {
        "reason": "for test example" }
        }

**Response JSON Example (Successful):**

.. code-block:: json

    {
        "statusCode": 201,
        "status": "success",
        "data": {
            "id": "4a4854af-cf94-4726-9520-8adb1c33c051",
            "reference": "TXN-1739183107-2655d05c960c2369",
            "currency": "NGN",
            "environment": "SANDBOX",
            "balance_after": 200,
            "balance_before": 0,
            "merchant_id": "d0c70a28-1023-484e-849f-3fb41cee743b",
            "metadata": "eyJyZWFzb24iOiAidG8gdGVzdCBmb3IgZG9jcyJ9",
            "amount": 200,
            "status": "COMPLETED",
            "destination": null,
            "description": null,
            "type": "CREDIT",
            "category": "CREDIT_CUSTOMER_WALLET"
        }
    }


**Response JSON Example (Fail):**

.. code-block:: json

    {
        "statusCode": 400,
        "status": "error",
        "error": {
            "message": "insufficient merchant wallet balance"
        }
    }
    {
        "statusCode": 400,
        "status": "error",
        "error": {
            "message": "insufficient merchant wallet balance"
        }
    }



**Python Demonstration:**

This is an example documentation using reStructuredText.

.. code-block:: python

    import requests
    import json

    url = "https://stagingapi.finecore.co/v1/wallets/credit"
    api_key = "your-api-key-here"  # Replace with your actual API key

    payload = {
        "amount": 200,
        "customer_id": "bec56c05-1257-47b0-9d4b-46a6c256999a",
        "metadata": {
            "reason": "for test example"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))




Fetch Specific Wallet
---------------------

**Description:**

This endpoint fetches a specific customer wallet. The required fields are customer_id.

**Endpoint:**

GET   https://stagingapi.finecore.co/v1/wallets/{{customer_id}}


**Response JSON Example:**

.. code-block:: json

   {
       "statusCode": 200,
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
           "user_id": "bec56c05-1257-47b0-9d4b-46a6c256999a"
       }
   }


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





Fetch All Customer Wallets
--------------------------

**Description:**

This endpoint initiates a bank transfer. The required fields are bvn, first_name, last_name, date_of_birth, phone_number, email and address.

**Endpoint:**

GET   https://stagingapi.finecore.co/v1/wallets



**Response JSON Example (note it will be a lot longer):**

.. code-block:: json

    {
        "statusCode": 200,
        "status": "success",
        "data": [
            {
                "id": "b8d3d89c-df8e-4612-bbe4-580832d67650",
                "mode": "",
                "email": "bentesting2024@finecore.co",
                "status": "ACTIVE",
                "bankName": "Xpresswallet",
                "bankCode": "100040",
                "walletId": "00000000-0000-0000-0000-000000000000",
                "customerId": "cc7cea08-4ed5-48cf-85dc-38ef9006c984",
                "walletType": "",
                "accountName": "Ben Testing",
                "accountNumber": "4484980045",
                "bookedBalance": 0,
                "availableBalance": 0,
                "accountReference": "LuAYnJgWcYRVtQpvQAzBBf2qDxqjHLQgqHBE"
            },
            {
                "id": "e0aec692-0de0-4857-b448-471645f46ebd",
                "mode": "",
                "email": "bentesting@finecore.co",
                "status": "ACTIVE",
                "bankName": "Xpresswallet",
                "bankCode": "100040",
                "walletId": "00000000-0000-0000-0000-000000000000",
                "customerId": "bec56c05-1257-47b0-9d4b-46a6c256999a",
                "walletType": "",
                "accountName": "Ben Testing",
                "accountNumber": "4458333576",
                "bookedBalance": 0,
                "availableBalance": 0,
                "accountReference": "RiJeIfh5MaM1SNGXKkDFWanwRm4iVpKbHfIc"
            }
        ]
    }


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
