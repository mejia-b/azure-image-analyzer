import azure.functions as func
import logging
import os
from azure.storage.blob import BlobServiceClient

def main(myblob: func.InputStream):
    logging.info(f"Processing file: {myblob.name}")

        # Retrieve the connection string from environment variables
    connection_string = os.getenv('AzureWebJobsStorage')
    
    # Create BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Example: List containers in the storage account
    containers = blob_service_client.list_containers()
    for container in containers:
        logging.info(f"Container found: {container['name']}")
    
    # image processing