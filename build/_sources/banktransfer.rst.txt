Bank Transfer
=============


Bank Transfer
-------------

**Description:**

This endpoint initiates a bank transfer. The required fields are amount, sortCode, narration, accountNumber, accountName, and metadata.

**Endpoint:**

POST https://stagingapi.finecore.co/v1/transfers/bank

**Request JSON Example:**

.. code-block:: json

     { "amount": 100,
     "sortCode": "000013",
     "narration": "Testing",
     "accountNumber": "1700263070",
     "accountName": "Obagunwa Emmanuel",
     "metadata": { "reason": "testing" } }

**Response JSON Example:**

.. code-block:: json

     { "statusCode": 201, "status": "success",
      "data": { "id": "3ae42594-c8a0-477f-a782-f1dc88f6414f",
       "reference": "TXN-1739183528-3ec9eab0cd83a820",
       "currency": "NGN",
       "environment": "SANDBOX",
       "balance_after": 10550,
       "balance_before": 10650,
       "merchant_id": "d0c70a28-1023-484e-849f-3fb41cee743b",
       "metadata": "eyJ2YXQiOiAwLCAiYW1vdW50IjogMTAwLCAiY2hhcmdlcyI6IDAsICJiYW5rTmFtZSI6ICJHVEJBTksgUExDIiwgInNvcnRDb2RlIjogIjAwMDAxMyIsICJuYXJyYXRpb24iOiAiVGVzdGluZyIsICJhY2NvdW50TmFtZSI6ICJPYmFndW53YSBFbW1hbnVlbCIsICJ0b3RhbEFtb3VudCI6IDEwMCwgImFjY291bnROdW1iZXIiOiAiMTcwMDI2MzA3MCIsICJ3YWxsZXRBY2NvdW50TmFtZSI6ICJGaW5lY29yZSBUZWNobm9sb2d5IExpbWl0ZWQiLCAiYWRkaXRpb25hbE1ldGFkYXRhIjogeyJyZWFzb24iOiAidGVzdGluZyJ9fQ==",
       "amount": 100,
       "status": "success",
       "destination": "1700263070/000013",
       "description": "Transfer of NGN100.00 to Obagunwa Emmanuel (1700263070/GTBANK PLC)/100040250210103208470558721501",
       "type": "DEBIT",
       "category": "BANK_TRANSFER" } }

**Python Demonstration:**

.. code-block:: python

   import requests
   import json

   url = "https://stagingapi.finecore.co/v1/transfers/bank"
   api_key = "your-api-key-here"  # Replace with your actual API key

   payload = {
       "amount": 100,
       "sortCode": "000013",
       "narration": "Testing",
       "accountNumber": "1700263070",
       "accountName": "Obagunwa Emmanuel",
       "metadata": {
           "reason": "testing"
       }
   }

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.post(url, headers=headers, data=json.dumps(payload))

**Glossary of fields:**

* sortCode

  - This is the bank identification number.

* accountNumber

  - This is the account number in the banks system.

* environment

  - This will only ever be "LIVE" and "SANDBOX".

* destination

  - This is desitnation address is a combination of the accountNumber and sortCode.
