#!/usr/bin/env python3

import requests
import settings
import time
from timeit import default_timer as timer
import sys
from requests.auth import HTTPDigestAuth
import json
import os

####
# Start script
####
start = timer()
print("============================")
print("  Get Backups from Atlas    ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():
    # Get a response from the MongoDB Atlas API
    # This example is interacting with the MongoDB Atlas Continuous Backup API
    # snapshotId should obviously be pointing to one of your snapshots
    data = {
        "delivery": {
            "expirationHours": "1",
            "maxDownloads": "1",
            "methodName": "HTTP"
        },
        "snapshotId": "5d717f0fcaad095fef784a50"
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(BACKUPS_API_URL, auth=HTTPDigestAuth(PUBLIC_API_KEY, PRIVATE_API_KEY),
                             data=json.dumps(data), headers=headers)

    if response.ok:
        json_response = response.json()

        process_response(json_response)

    else:
        print('Invalid response! ' + str(response.content))
        sys.exit('Exiting!')


def process_response(json_response):
    print("Process response...")

    # parse json response
    results = json_response.get('results')
    delivery = results[0].get('delivery')
    status = delivery.get('statusName')

    # check that the download is ready
    if status == 'READY':
        print('Ready to download snapshot.')
        download_url = delivery.get('url')
        print('Downloading from url: ' + download_url)

        # download the snapshot and save it to a local directory
        snapshot_download = requests.get(download_url)
        with open(os.path.join(sys.path[0] + "/myBackupSnapshot.tar.gz"), "wb") as f:
            print('Writing snapshot backup file.')
            f.write(snapshot_download.content)


####
# Constants loaded from .env file
####
BACKUPS_API_URL = settings.BACKUPS_API_URL
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
