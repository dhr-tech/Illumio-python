# Illumio-python
Python based automation for Illumio
API information can fetched from https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/REST-APIs/out/en/index-en.html?

<img width="311" height="162" alt="image" src="https://github.com/user-attachments/assets/659089e3-fb85-489b-87cc-7cbf326bdea0" />



API and Organisation ID can be fetched from PCE as shown below.

<img width="1158" height="466" alt="image" src="https://github.com/user-attachments/assets/bd49f298-9356-41b0-a16f-48e8c2c5e17c" />

# Limitations

Illumio limits synchronous responses to 500 entries. If the dataset is larger, the PCE:

Does not return the data immediately
1.  Starts a background job
2.  Tells you where to check later

This is called an asynchronous response.
https://product-docs-repo.illumio.com/Tech-Docs/Core/25.4/REST-APIs/out/en/rest-apis-25-4/asynchronous-get-collections/async-job-operations.html

<img width="316" height="206" alt="image" src="https://github.com/user-attachments/assets/5d1f5698-936b-4911-89ba-f6ca485dab40" />
