#!/usr/bin/env python3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
API_URL = os.getenv('API_URL')
PUBLIC_API_KEY = os.getenv('PUBLIC_API_KEY')
PRIVATE_API_KEY = os.getenv('PRIVATE_API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')
CLUSTER_NAME_1 = os.getenv('CLUSTER_NAME_1')
CLUSTER_NAME_2 = os.getenv('CLUSTER_NAME_2')

print("Setting loaded from .env file.")
