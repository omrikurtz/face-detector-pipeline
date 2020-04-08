from pipelines.core.pipeline import Pipeline


class UpdateDatabase(Pipeline):
    def __init__(self, db, db_name, collection):
        self.db = db
        self.db_name = db_name
        self.collection = collection
        super(UpdateDatabase, self).__init__()

    def map(self, doc):
        output = self.db[self.db_name][self.collection]
        # Check the to_update attribute for updating the database
        if doc.get('to_update', None) is not None:
            output.find_one_and_update({'_id': doc['to_update']}, {'$set': {'is_best_picture': False}})
        doc.pop('to_update', None)
        output.insert_one(doc)
