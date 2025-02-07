Bank Details
============

Initiate Bank Details
---------------------

.. toctree::
   :maxdepth: 3
   :caption: Contents:
     index
     introduction
     card
     merchant
     bankdetails



**Endpoint:**

 - POST https://stagingapi.finecore.co/v1/transactions/bank-details/initiate

**Description:**
 - This endpoint initiates a bank details transaction for a business. The required fields are ``businessId``, ``amount``, ``description``, ``customer``, ``accountNumber``, and ``bankCode``.

**Request JSON Example:**

.. code-block:: json

    {
      "businessId": "8b2c6c2b-c675-4110-4cc1-08dcb0b55c6f",
      "amount": 1000,
      "description": "ALATpay Checkout Payment",
      "customer":
          {
               "email": "jane.joe@email.com",
               "phone": "+23480000000001",
               "firstName": "Jane",
               "lastName": "+23480000000001",
               "metadata": "string"
          },
     "accountNumber": "0126038165",
     "bankCode": "035"

    }
