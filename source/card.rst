Card
====

Initialize Card
---------------

This documentation will guide you through the features and usage of finecore.

.. toctree::
   :maxdepth: 3
   :caption: Contents:
      index
      introduction
      bankdetails


**Endpoint:**

 - POST https://stagingapi.finecore.co/v1/cards/initialize

**Description:**
 - This endpoint initializes a card for a business. The required fields are ``businessId``, ``cardNumber``, and ``currency``.

**Request JSON Example:**

.. code-block:: json

    {
      "businessId": "8b2c6c2b-c675-4110-4cc1-08dcb0b55c6f",
      "cardNumber": "5078720022504707",
      "currency": "USD"
    }
