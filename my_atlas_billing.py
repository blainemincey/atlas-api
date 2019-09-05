#!/usr/bin/env python3

import requests
import settings
import time
from timeit import default_timer as timer
import sys
from requests.auth import HTTPDigestAuth
from decimal import Decimal

####
# Start script
####
start = timer()
print("============================")
print("  Get Billing from Atlas     ")
print("============================")
print("Starting " + time.asctime() + "\n")


####
# Main start function
####
def main():

    # Get a response from the MongoDB Atlas API
    # This example is interacting with the MongoDB Atlas Billing API
    response = requests.request("GET", INVOICES_API_URL, auth=HTTPDigestAuth(PUBLIC_API_KEY, PRIVATE_API_KEY))

    if response.ok:
        json_response = response.json()

        process_response(json_response)

    else:
        print('Invalid response! ' + str(response.content))
        sys.exit('Exiting!')


def process_response(json_response):
    print("Process response...")

    # Loop thru line items JSON
    line_items = json_response.get('lineItems')
    for item in line_items:
        # get the groupId (i.e. the projectId in Atlas)
        project = item.get('groupId')
        if project == PROJECT_ID:
            cluster_name = item.get('clusterName')

            # Grab the values based on cluster name for your project
            if cluster_name == CLUSTER_NAME_1:

                sku = item.get('sku')
                dollars = item.get('unitPriceDollars')
                cents = item.get('totalPriceCents')

                print("== " + cluster_name + " ==")
                print("Sku: " + sku)
                print("Dollars: " + str(dollars))
                print("Cents:" + str(cents))
                print("===================")

            if cluster_name == CLUSTER_NAME_2:

                sku = item.get('sku')
                dollars = item.get('unitPriceDollars')
                cents = item.get('totalPriceCents')

                print("== " + cluster_name + " ==")
                print("Sku: " + sku)
                print("Dollars: " + str(dollars))
                print("Cents:" + str(cents))
                print("===================")


####
# Constants loaded from .env file
####
INVOICES_API_URL = settings.INVOICES_API_URL
PUBLIC_API_KEY = settings.PUBLIC_API_KEY
PRIVATE_API_KEY = settings.PRIVATE_API_KEY
PROJECT_ID = settings.PROJECT_ID
CLUSTER_NAME_1 = settings.CLUSTER_NAME_1
CLUSTER_NAME_2 = settings.CLUSTER_NAME_2

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
