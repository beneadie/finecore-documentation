Transactions
============


Fetch Custom Transaction
------------------------

Fetches single transaction by specific customer

**Description:**

This endpoint initiates a bank transfer. The required fields are amount, sortCode, narration, accountNumber, accountName, and metadata.

**Endpoint:**

GET  https://stagingapi.finecore.co/v1//transactions/{customer_id}/

**Response JSON Example:**

.. code-block:: json

     {"FIX": "ADD THIS WHEN POSTMAN WORKING AGAIN"}

**Python Demonstration:**

.. code-block:: python

   import requests

   customer_id = "your-customer-id-here"  # Replace with the actual customer ID
   url = f"https://stagingapi.finecore.co/v1/transactions/customer/{customer_id}"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)

   if response.status_code == 200:
       print("Success")
       print(response.json())
   else:
       print("Failed with status code:", response.status_code)
       print(response.text)
