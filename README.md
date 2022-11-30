# 💎 CerebroIndexator
[![Supported python versions](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)
[![Code style](https://img.shields.io/badge/code%20style-PEP8-blue)](https://peps.python.org/pep-0008/)
[![Supported elasticsearch versions](https://img.shields.io/badge/elasticsearch-8.5.1-yellow)](https://pypi.org/project/elasticsearch/)
[![Coverage status](https://img.shields.io/badge/coverage-0%25-red)](https://coverage.readthedocs.io/en/6.5.0/)

This application allows you to create, delete and view information about indexes of ElasticSearch. 
Also, you can parse and upload your json documents to ElasticSearch server.

## Basic capabilities

| Features       | Status | What is necessary?                               |
|----------------|--------|--------------------------------------------------|
| Create         | ✅      | index name, collection, mappings, config         |
| Delete         | ✅      | index name                                       |
| View           | ✅      | -                                                |
| Recovery       | ❌      | index name, collection, mappings, config         |
| Package create | ❌      | list of index name, collection, mappings, config |

## Installing Linux (Ubuntu)
```bash
git clone https://github.com/ElveeBolt/CerebroIndexator.git
cd CerebroIndexator
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt
```

## Usage

Before use CerebroIndexator you must have this path structure:
```bash
databases
|-- index_0001
    |-- collection_0.json
    |-- collection_1.json
    |-- mappings.json
    |-- config.json
|-- index_0002
|-- index_0003
|-- CerebroIndexator
```

Edit settings in <code>settings.py</code> to connect your ElasticSearch server
```python
# ElasticSearch settings
ELASTIC_HOST = 'https://10.0.0.2:9200'
ELASTIC_FINGERPRINT = 'A0:C4:DA:D7:AD:B2:7B:D9:AA:48:AC:91:3E:0E:9E:0F:05:80:2B:EC:75:80:C9:27:43:52:49:04:8D:6E:3A:DB'
ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = 'O11J4soaIrTTUUQhT9Vp'
```

## Run app
```bash
python main.py
```

## Author
Developed and maintained by [ElveeBolt](https://github.com/ElveeBolt).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.