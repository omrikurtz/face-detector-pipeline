from pipelines.core.pipeline import Pipeline


class FormatData(Pipeline):
    def map(self, doc):
        # Cleanup fields that start with __, which are pipeline-private (not for serialization)
        doc = {k: doc[k] for k in doc if not k.startswith('__')}
        # Change key name to conform to the specified format
        doc['is_best_picture'] = doc.pop('best_candidate')
        faces_formatted = []
        for face in doc['faces']:
            face_data = face['face_data']
            width = face_data.bottom_right_corner.x - face_data.top_left_corner.x
            height = face_data.bottom_right_corner.y - face_data.top_left_corner.y
            face_features = [height, width, face_data.top_left_corner.x, face_data.top_left_corner.y]
            faces_formatted.append(face_features)
        doc['faces'] = faces_formatted
        return doc
