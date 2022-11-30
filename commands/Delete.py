from core.Elastic import Elastic


class Delete(Elastic):
    """
    Deleting an index deletes its documents, shards, and metadata.

    Index are deleted if name of index is exists in ElasticSearch server.

    For more please visit https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-index.html
    """

    def __init__(self):
        super().__init__()

    def format_command(self, command: str) -> str:
        """
        Formatted command
        - remove spaces from start and end string
        - format string to lowercase

        :param command: string of command
        :return: formatted command
        """
        return command.strip().lower()

    def run(self):
        index = input('Enter index name:')

        if not self.is_exists(index):
            return print('Index not found')

        command = input(f'Are you sure to remove {index} index?\nYes / No')
        command = self.format_command(command)

        if command == 'yes':
            self.delete_index(index)
            print(f'Success delete {index}')
