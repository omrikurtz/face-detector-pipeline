from models.image import ImageModel
from pipelines.core.pipeline import Pipeline


class GenerateDocsFromMongo(Pipeline):
    def __init__(self, db, db_name, collection):
        self.db = db
        self.db_name = db_name
        self.collection = collection
        super(GenerateDocsFromMongo, self).__init__()

    def generator(self):
        for doc in self.db[self.db_name][self.collection].find():
            # Send a data object representing our doc as a dict
            # This allows for some cool manipulations on-the-fly over the pipeline
            doc_output = {'_id': doc['_id'], '__data': doc['image'], 'best_candidate': False, 'faces': []}
            doc_output['__model'] = ImageModel.from_bytes(doc_output['_id'], doc_output['__data'])
            yield doc_output
