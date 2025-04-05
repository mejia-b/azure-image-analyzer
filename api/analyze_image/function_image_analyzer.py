import azure.functions as func
import logging

def main(myblob: func.InputStream):
    logging.info(f"Processing file: {myblob.name}")

    # image processing