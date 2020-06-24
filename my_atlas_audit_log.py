#!/usr/bin/env python3

import requests
import settings
import time
import datetime
from timeit import default_timer as timer
import sys
from requests.auth import HTTPDigestAuth
import os

####
# Start script
####
start = timer()
print("============================")
print("  Get My Atlas Audit Logs   ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():
    # Get a response from the MongoDB Atlas API
    # Grab the MongoDB Atlas Audit Log
    headers = {
        "Accept": "application/gzip"
    }

    response = requests.get(AUDIT_LOG_API_URL, auth=HTTPDigestAuth(PUBLIC_API_KEY, PRIVATE_API_KEY), headers=headers)

    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    audit_log_filename = "mongodb_audit_log_" + time_stamp

    if response.ok:
        with open(os.path.join(sys.path[0] + "/" + audit_log_filename + ".gz"), "wb") as f:
            print('Writing MongoDB Atlas Audit Log.')
            f.write(response.content)

    else:
        print('Invalid response! ' + str(response.content))
        sys.exit('Exiting!')


####
# Constants loaded from .env file
####
AUDIT_LOG_API_URL = settings.AUDIT_LOG_API_URL
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
