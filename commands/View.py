from core.Elastic import Elastic
from tabulate import tabulate


class View(Elastic):
    """
    Return information of indexes from ElasticSearch server.

    For more please visit https://www.elastic.co/guide/en/elasticsearch/reference/current/cat-indices.html

    - health - health status used to limit returned indices.
    - status - type of index that wildcard patterns can match.
    - index - name of index.
    - uuid - uuid of index.
    - pri - if true, the response only includes information from primary shards.
    - rep - count of replica.
    - docs.count - documents count.
    - docs.deleted - count of deleted documents.
    - store.size - store size taken by primary & replica shards.
    - pri.store.size - store size taken only by primary shards.
    """

    def __init__(self):
        super().__init__()
        self.head = [
            'health',
            'status',
            'index',
            'uuid',
            'pri',
            'rep',
            'docs.count',
            'docs.deleted',
            'store.size',
            'pri.store.size']

    def to_list(self, indices: dict) -> list:
        """
        Format dict to list of list data from index.

        :param indices: dict of indexes
        :return: list of list data
        """
        return [index.values() for index in indices]

    def run(self):
        indices = self.get_indices()

        if not indices:
            return print('Indexes not found')

        data = self.to_list(indices)
        print(tabulate(data, headers=self.head, tablefmt="simple_grid"))
