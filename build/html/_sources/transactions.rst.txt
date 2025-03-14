Transactions
============



Fetch All Transactions for One Customer
---------------------------------------


**Description:**

This endpoint fetches all transactions by a specific customer.

**Endpoint:**

GET  https://api.finecore.co/v1/transactions/customer/:customer_id

**Response JSON Example:**

.. code-block:: json

   {
      "statusCode": 200,
      "status": "success",
      "data": [
         {
            "id": "a0d95df4-b004-4c38-95b8-b9308d0340c1",
            "user_id": "2da3424b-1d1e-4155-a65e-d2347c37a73c",
            "reference": "TXN-1736446870-9572309761397768",
            "currency": "NGN",
            "environment": "SANDBOX",
            "status": null,
            "amount": 200,
            "balance_after": 1000,
            "balance_before": 800,
            "metadata": "eyJyZWFzb24iOiAiZm9yIGNvbXBsZXRpb24gb2YgdGFzayJ9",
            "type": "CREDIT",
            "category": "CREDIT_CUSTOMER_WALLET",
            "total_items": 3
         },
         {
            "id": "f94d933c-75c3-42c5-8f6c-ceb7e64f8d80",
            "user_id": "2da3424b-1d1e-4155-a65e-d2347c37a73c",
            "reference": "TXN-1736445802-9e8bc1decbdc2178",
            "currency": "NGN",
            "environment": "SANDBOX",
            "status": null,
            "amount": 0,
            "balance_after": 800,
            "balance_before": 600,
            "metadata": null,
            "type": "CREDIT",
            "category": "CREDIT_CUSTOMER_WALLET",
            "total_items": 3
         }
        ]
   }



**Python Demonstration:**

.. code-block:: python

   import requests

   customer_id = "2da3424b-1d1e-4155-a65e-d2347c37a73c"  # example customer ID
   url = f"https://api.finecore.co/v1/transactions/customer/{customer_id}"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)

**Glossary of fields:**

* id

  - Identification number for the transaction.

  - Intended for bank and developers.

* user_id

  - The identification number of the consumer.

* metadata

  - Additional data.

  - Will be encrypted after being sent.

* reference

  - Another transaction identification number but meant for consumers.

* environment

  - Will only be "LIVE" or "SANDBOX".

* type

  - Transaction type. Can only be credit right now.

* total_items

  - Total number of items involved in transaction.




Fetch Customer Specific Transaction
-----------------------------------

**Description:**

This endpoint fetches a single transaction by specific customer

**Endpoint:**

GET  https://api.finecore.co/v1/transactions/customer/:customer_id/:reference

**Response JSON Example:**

.. code-block:: json

    {
        "statusCode": 200,
        "status": "success",
        "data": {
            "id": "509eae9c-9373-486d-b25d-0c46994b66f9",
            "user_id": "2da3424b-1d1e-4155-a65e-d2347c37a73c",
            "reference": "TXN-1736445726-87dc1349d8f78a0a",
            "currency": "NGN",
            "environment": "SANDBOX",
            "status": null,
            "balance_after": 600,
            "balance_before": 400,
            "metadata": null,
            "type": "CREDIT",
            "category": "CREDIT_CUSTOMER_WALLET"
        }
    }


**Python Demonstration:**

.. code-block:: python

   import requests

   transactionreference = "TXN-1736446870-9572309761397768" #example transaction reference
   customer_id = "2da3424b-1d1e-4155-a65e-d2347c37a73c"  # example customer ID
   url = f"https://api.finecore.co/v1/transactions/customer/{customer_id}/{transactionreference}"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)

**Glossary of fields:**

* id

  - Identification number for the transaction.

  - Intended for bank and developers.

* user_id

  - The identification number of the consumer.

* metadata

  - Additional data.

  - Will be encrypted after being sent.

* reference

  - Another transaction identification number but meant for consumers.

* environment

  - Will only be "LIVE" or "SANDBOX".

* type

  - Transaction type. Can only be credit right now.

* total_items

  - Total number of items involved in transaction.
