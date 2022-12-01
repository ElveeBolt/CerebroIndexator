from settings import *
from elasticsearch import Elasticsearch, exceptions, helpers


class Elastic:
    def __init__(self):
        self._client = self.get_client()

    def get_client(self):
        """
        Connect to ElasticSearch server

        :return: ElasticSearch client
        """
        return Elasticsearch(
            hosts=ELASTIC_HOST,
            ssl_assert_fingerprint=ELASTIC_FINGERPRINT,
            basic_auth=(
                ELASTIC_USERNAME,
                ELASTIC_PASSWORD))

    def get_indices(self):
        """
        Get indices info

        :return: info indices
        """
        return self._client.cat.indices(format='json')

    def create_index(self, index: str, mappings: dict):
        """
        Create index with mappings

        :param index: index name
        :param mappings: index mappings
        :return:
        """
        return self._client.indices.create(index=index, mappings=mappings)

    def delete_index(self, index: str):
        """
        Remove index

        :param index: index name
        :return:
        """
        try:
            self._client.indices.delete(index=index)
        except exceptions.NotFoundError:
            return print('Index not found')

    def is_exists(self, index: str) -> bool:
        """
        Check information about whether a particular index exists

        :param index: index name
        :return: bool of exists
        """
        return self._client.indices.exists(index=index)

    def put_documents(self, index: str, documents: list):
        """
        Put documents packages. Size of packages is equals
        PACKAGES_SIZE from settings.py

        :param index: index name
        :param documents: list of documents
        :return:
        """
        return helpers.bulk(client=self._client, index=index, actions=documents)
