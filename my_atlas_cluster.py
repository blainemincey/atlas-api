#!/usr/bin/env python3

import requests
import settings
import time
from timeit import default_timer as timer
import sys
from requests.auth import HTTPDigestAuth
import socket

####
# Start script
####
start = timer()
print("============================")
print("  Get My Atlas Cluster      ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():
    # Get a response from the MongoDB Atlas API
    # This example is interacting with the MongoDB Atlas Cluster API
    response = requests.get(CLUSTERS_API_URL, auth=HTTPDigestAuth(PUBLIC_API_KEY, PRIVATE_API_KEY))

    if response.ok:
        json_response = response.json()

        process_response(json_response)

    else:
        print('Invalid response! ' + str(response.content))
        sys.exit('Exiting!')


def process_response(json_response):
    print("Process response...")
    print(json_response)
    print('\n')

    # parse json response
    uris = json_response.get('mongoURI')
    # remove the first part of the mongodb uri
    format_uris = uris.replace('mongodb://', '')

    # remove the port
    final_uris = format_uris.replace(':27017', '')

    # split on the comman
    split_uris = final_uris.split(',')

    # loop thru results
    for uri in split_uris:
        print('Get IP for: ' + str(uri))
        ip = socket.gethostbyname(uri)
        print(ip)
        print('\n')

####
# Constants loaded from .env file
####
CLUSTERS_API_URL = settings.CLUSTERS_API_URL
PUBLIC_API_KEY = settings.PUBLIC_API_KEY
PRIVATE_API_KEY = settings.PRIVATE_API_KEY
PROJECT_ID = settings.PROJECT_ID

####
# Main
####
if __name__ == '__main__':
    main()

####
# Indicate end of script
####
end = timer()
print("\nEnding " + time.asctime())
print('====================================================')
print('Total Time Elapsed (in seconds): ' + str(end - start))
print('====================================================')
