from alive_progress import alive_bar
from core.Elastic import Elastic
from core.Core import Core
from settings import *


class Create(Elastic, Core):
    """
    To create an index, the following data is required:

    - name - index name
    - config.json - file of config database
    - mapping.json - file of mappings index
    - collection_... - file with list documents to upload

    After the name is entered, an index will be created using mapping.
    Next, the parsing of files with documents will begin and their further upload to the ElasticSearch server.

    Previously, the documents will be supplemented with data from config.json and loading datetime.
    """

    def __init__(self):
        super().__init__()

    def run(self):
        index = input('Enter index name:')

        if self.is_exists(index):
            return print('Index are creating')

        path = self.is_path_exists(index)

        if not path:
            return print('Index path not found')

        mappings = self.read_json(path['mappings'])
        config = self.read_json(path['config'])
        self.create_index(index=index, mappings=mappings)
        collection_count = len(path['collections'])

        with alive_bar(collection_count, force_tty=True, bar='smooth', length=20) as bar:
            for collection in path['collections']:
                data = self.read_json(collection)
                size = len(data)
                documents = []
                for i, item in enumerate(data, start=1):
                    document = self.update_document(
                        document=item, config=config)
                    documents.append(document)

                    if i % PACKAGE_SIZE == 0 or i == size:
                        self.put_document_bulk(
                            index=index, documents=documents)
                        documents.clear()

                bar()

        print('Success')
