import os
import json
from datetime import datetime
from settings import *


class Core:
    def __init__(self):
        pass

    def is_path_exists(self, path: str) -> dict | None:
        """
        Check if directory name exists and generate
        dict of mappings, config and collection path

        :param path: directory path
        :return: dict of mappings, config and collection path or None
        """
        path = os.path.join(BASE_DIR, path)

        if not os.path.exists(path):
            return

        data = {
            'mappings': os.path.join(path, MAPPINGS),
            'config': os.path.join(path, CONFIG),
        }

        collections = self.get_collection_files(path)
        if collections:
            data['collections'] = collections

        return data

    def get_collection_files(self, path: str) -> list:
        """
        Get list of collection file in path

        :param path:
        :return: list of file
        """
        files = os.listdir(path)
        return [os.path.join(path, file) for file in files if file.split('_')[0] == COLLECTION_PREFIX]

    def update_document(self, document: dict, config: dict) -> dict:
        """
        Update current document.
        Add current date and index database name
        Remove key '_id' if exists

        :param document: dict document
        :param config: config of database
        :return: dict of new document
        """

        if document.get('_id'):
            document.pop('_id')

        dict = {
            'date': datetime.now().strftime(DATETIME_FORMAT),
            'database': config['database']
        }

        document.update(dict)
        return document

    def read_json(self, path: str) -> dict:
        """
        Read json file of path

        :param path: path of mapping
        :return: dict of mapping
        """
        with open(file=path, mode='r', encoding=ENCODING) as file:
            data = json.load(file)

        return data
