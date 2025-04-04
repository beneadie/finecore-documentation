Bank Transfer
=============


Bank Transfer
-------------

**Description:**

This endpoint initiates a bank transfer. The required fields are amount, sortCode, narration, accountNumber, accountName, and metadata.

**Endpoint:**

POST https://api.finecore.co.finecore.co/v1/transfers/bank

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

   url = "https://api.finecore.co/v1/transfers/bank"
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
  - The endpoint below will show you how to obtain the number for the matching bank partner.

* accountNumber

  - This is the account number in the banks system.

* environment

  - This will only ever be "LIVE" and "SANDBOX".

* destination

  - This is desitnation address is a combination of the accountNumber and sortCode.


Get Bank Code List
------------------

**Description:**

This endpoint fetches a list of bank codes that our defined by one of our 3rd party partners. You will need the bank code to enter in the sortCode field in the bank transfer endpoint.

**Endpoint:**

GET https://api.finecore.co/v1/transfers/banks


**Response JSON Example:**

.. code-block:: json

     {"success":true,
     "message":"Successfully fetched list of banks",
     "data":[{"code":"110005","name":"3LINE CARD MANAGEMENT LIMITED"},{"code":"110072","name":"78 FINANCE COMPANY LIMITED"},{"code":"090629","name":"9JAPAY MICROFINANCE BANK"},{"code":"120001","name":"9 PAYMENT SERVICE BANK"},{"code":"050005","name":"AAA FINANCE AND INVESTMENT COMPANY LIMITED"},{"code":"070010","name":"ABBEY MORTGAGE BANK"},{"code":"090270","name":"AB MICROFINANCE BANK"},{"code":"090260","name":"ABOVE ONLY MICROFINANCE BANK"},{"code":"288037","name":"ABSA BANK GHANA LIMITED"},{"code":"090640","name":"ABSU MICROFINANCE BANK"},{"code":"090424","name":"ABUCOOP MFB"},{"code":"090545","name":"ABULESORO MICROFINANCE BANK"},{"code":"090197","name":"ABU MICROFINANCE BANK"},{"code":"090202","name":"ACCELEREX NETWORK LIMITED"},{"code":"000014","name":"ACCESS BANK"},{"code":"000005","name":"ACCESS(DIAMOND) BANK"},{"code":"100013","name":"ACCESS MONEY"},{"code":"100052","name":"ACCESS YELLO \u0026 BETA"},{"code":"090134","name":"ACCION MICROFINANCE BANK"},{"code":"090483","name":"ADA MFB"},{"code":"090160","name":"ADDOSSER MICROFINANCE BANK"},{"code":"090268","name":"ADEYEMI COLLEGE STAFF MICROFINANCE BANK"},{"code":"090155","name":"ADVANS LA FAYETTE  MICROFINANCE BANK"},{"code":"090614","name":"AELLA MICROFINANCE BANK"},{"code":"090292","name":"AFEKHAFE MICROFINANCE BANK"},{"code":"090518","name":"AFEMAI MFB"},{"code":"100028","name":"AG MORTGAGE BANK"},{"code":"090371","name":"AGOSASA MICROFINANCE BANK"},{"code":"090698","name":"AKALABO MFB"},{"code":"090608","name":"AKPO MICROFINANCE BANK"},{"code":"090561","name":"AKUCHUKWU MICROFINANCE BANK"},{"code":"090531","name":"AKU MICROFINANCE BANK"},{"code":"090133","name":"AL-BARAKAH MICROFINANCE BANK"},{"code":"090259","name":"ALEKUN MICROFINANCE BANK"},{"code":"090297","name":"ALERT MICROFINANCE BANK"},{"code":"090277","name":"AL-HAYAT MICROFINANCE BANK"},{"code":"090131","name":"ALLWORKERS MICROFINANCE BANK"},{"code":"090548","name":"ALLY MICROFINANCE BANK"},{"code":"090169","name":"ALPHA KAPITAL MICROFINANCE BANK"},{"code":"000037","name":"ALTERNATIVE BANK LIMITED"},{"code":"090394","name":"AMAC MICROFINANCE BANK"},{"code":"090180","name":"AMJU UNIQUE MICROFINANCE BANK"},{"code":"090116","name":"AMML MICROFINANCE BANK"},{"code":"090610","name":"AMOYE MICROFINANCE BANK"}]}


**Python Demonstration:**

.. code-block:: python

   import requests
   import json

   url = "https://api.finecore.co/v1/transfers/banks"
   api_key = "your-api-key-here"  # Replace with your actual API key

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.get(url, headers=headers)


Verify Bank Account Details
---------------------------

**Description:**

This endpoint is a testing mecahnism to ensure that the bank account details entered are valid.

**Endpoint:**

POST https://api.finecore.co/v1/transfers/account


**Request JSON Example:**

.. code-block:: json

     {
     "sortCode": "000013",
     "accountNumber": "1700263070"
     }

**Response JSON Example:**

.. code-block:: json

     {"success":true,
     "message":"Successfully fetch account detail",
     "data":{"bankCode":"000013","accountName":"SIMI MICHELLE","accountNumber":"1700263070"}}

**Python Demonstration:**

.. code-block:: python

   import requests
   import json

   url = "https://api.finecore.co/v1/transfers/account"
   api_key = "your-api-key-here"  # Replace with your actual API key

   payload = {
       "sort_code": "000013",
       "account_number": "1700263070"
   }

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.post(url, headers=headers, data=json.dumps(payload))

**Glossary of fields:**

* sort_code (sortCode)

  - This is the bank identification number.

* account_number (accountNumber)

  - This is the account number in the banks system.


User Transfer to Bank Account
-----------------------------

**Description:**

This endpoint allows a user to transfer money out of their wallet to their bank account. The required fields are amount, sortCode, narration, accountNumber, accountName, metadata and customerId.

**Endpoint:**

POST https://api.finecore.co.finecore.co/v1/transfers/bank/customer

**Request JSON Example:**

.. code-block:: json

     { "amount": 50,
     "sortCode": "000013",
     "narration": "Customer transfer",
     "accountNumber": "0167421242",
     "accountName": "Emmanuel Obagunwa",
     "customerId": "0e72df4b-c0c1-4874-8f3d-d35ae5a6a60c",
     "metadata": {"key": "value"} }


**Response JSON Example:**

.. code-block:: json

     {  "success": true,
        "message": "You have successfully make a transfer",
        "data": {
            "id": "40cd2b51-e26d-42a7-b347-f9d181df58e2",
            "reference": "TXN-1743150834-d528cb706bcd4a68",
            "currency": "NGN",
            "environment": "SANDBOX",
            "balance_after": 550,
            "balance_before": 600,
            "merchant_id": "6f5c63ce-f525-4442-be11-a401658396d7",
            "metadata": "eyJ2YXQiOiAwLjc1LCAiYW1vdW50IjogNTAsICJjaGFyZ2VzIjogMTAsICJiYW5rTmFtZSI6ICJHVEJBTksgUExDIiwgInNvcnRDb2RlIjogIjAwMDAxMyIsICJuYXJyYXRpb24iOiAiQ3VzdG9tZXIgdHJhbnNmZXIiLCAiYWNjb3VudE5hbWUiOiAiRW1tYW51ZWwgT2JhZ3Vud2EiLCAidG90YWxBbW91bnQiOiA2MC43NSwgImFjY291bnROdW1iZXIiOiAiMDE2NzQyMTI0MiIsICJ3YWxsZXRBY2NvdW50TmFtZSI6ICJTYW1zb24gRWRpZSIsICJhZGRpdGlvbmFsTWV0YWRhdGEiOiB7ImtleSI6ICJ2YWx1ZSJ9fQ==",
            "amount": 50,
            "status": "success",
            "destination": "0167421242/000013",
            "description": "Transfer of NGN50.00 to Emmanuel Obagunwa (0167421242/GTBANK PLC)/100040250328083356422632670862",
            "type": "DEBIT",
            "category": "BANK_TRANSFER"} }

**Python Demonstration:**

.. code-block:: python

   import requests
   import json

   url = "https://api.finecore.co/v1/transfers/bank/customer"
   api_key = "your-api-key-here"  # Replace with your actual API key

   payload = { "amount": 50,
      "sortCode": "000013",
      "narration": "Customer transfer",
      "accountNumber": "0167421242",
      "accountName": "Emmanuel Obagunwa",
      "customerId": "0e72df4b-c0c1-4874-8f3d-d35ae5a6a60c",
      "metadata": {"key": "value"}
    }

   headers = {
       "Content-Type": "application/json",
       "X-API-Key": api_key
   }

   response = requests.post(url, headers=headers, data=json.dumps(payload))

**Glossary of fields:**

* All previous fields are the same as the Bank Transfer endpoint

* customerId (Customer ID)

  - This number of the specific customer and can be found in the Fetch All Wallets endpoint.
