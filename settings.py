"""
Settings file
"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ENCODING = 'UTF-8'
MAPPINGS = 'mappings.json'
CONFIG = 'config.json'
COLLECTION_PREFIX = 'collection'

# Format date to update document
DATETIME_FORMAT = '%d.%m.%Y %H:%M'

PACKAGE_SIZE = 10000

# ElasticSearch settings
ELASTIC_HOST = 'https://10.0.0.2:9200'
ELASTIC_FINGERPRINT = 'A0:C4:DA:D7:AD:B2:7B:D9:AA:48:AC:91:3E:0E:9E:0F:05:80:2B:EC:75:80:C9:27:43:52:49:04:8D:6E:3A:DB'
ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = 'O11J4soaIrTTUUQhT9Vp'
