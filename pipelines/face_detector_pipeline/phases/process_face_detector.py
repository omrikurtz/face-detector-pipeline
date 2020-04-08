from api.google_vision.face_detector import FaceDetector # For type-hinting only
from pipelines.core.pipeline import Pipeline


class ProcessWithFaceDetector(Pipeline):
    def __init__(self, fd: FaceDetector):
        self.fd = fd
        super(ProcessWithFaceDetector, self).__init__()

    def map(self, doc):
        image_model = doc['__model']
        faces = self.fd.get_faces_from_image(image_model)
        doc['faces'] = [{'face_data': face} for face in faces]  # The dicts will be normalized to lists as required
        return doc
