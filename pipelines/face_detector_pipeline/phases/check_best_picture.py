from pipelines.core.pipeline import Pipeline


class CheckBestPictureCandidate(Pipeline):
    def __init__(self, best_ratio=0, candidate_doc_id=None):
        self.best_ratio = best_ratio
        self.candidate_doc_id = candidate_doc_id
        super(CheckBestPictureCandidate, self).__init__()

    def map(self, doc):
        # Skipping docs without centered faces
        if not any(face['is_center'] for face in doc['faces']):
            return doc
        image_model = doc['__model']
        new_faces = []
        for face in doc['faces']:
            face_data = face['face_data']
            face_width = face_data.bottom_right_corner.x - face_data.top_left_corner.x
            face_height = face_data.bottom_right_corner.y - face_data.top_left_corner.y
            face['ratio'] = image_model.get_ratio_to_rect(face_width, face_height)
            if face['ratio'] > self.best_ratio and face['is_center']:
                doc['best_candidate'] = True
                doc['to_update'] = self.candidate_doc_id
                self.best_ratio = face['ratio']
                self.candidate_doc_id = doc['_id']
            new_faces.append(face)
        doc['faces'] = new_faces
        return doc
