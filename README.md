# Atlas-Api
Repo for scripts to interface with the MongoDB Atlas API.
Please refer to the [MongoDB Atlas API](https://docs.atlas.mongodb.com/api/)
documentation for additional details.  Please be sure to configure MongoDB
Atlas for API Access before using the scripts in this project.

## Requirements
You will need to install the following using Python3/pip3:
* requests
* dotenv

In the root directory of this project, be sure to copy .env.example
to .env.  Make the appropriate modifications based on your environment
and API access.

## Billing API
my_atlas_billing.py interfaces with the Invoices API as documented
in the [MongoDB Atlas Invoices API](https://docs.atlas.mongodb.com/reference/api/invoices/)
documentation.

## Backups API
This specifically is requesting a restore job based on a specific snapshot.  This downloads
it to a local directory.
my_atlas_backups.py interfaces with the Continuous Backup API as documented
in the [MongoDB Atlas Backups API](https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-get-one/)
documentation.

