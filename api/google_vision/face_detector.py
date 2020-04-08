from google.cloud import vision
from google.cloud.vision import types
from models.image import ImageModel
from api.extracted_component import ExtractedRect


class FaceDetector:
    def __init__(self, client: vision.ImageAnnotatorClient):
        self.client = client

    @classmethod
    def from_default_client(cls):
        client = vision.ImageAnnotatorClient()
        return cls(client)

    def get_faces_from_image(self, image: ImageModel):
        content = image.get_bytes()
        # IDEs freak out on this, because this is loaded dynamically
        google_image = types.Image(content=content)
        results = self.client.face_detection(image=google_image).face_annotations
        faces = []
        for result in results:
            vertices = result.fd_bounding_poly.vertices
            # According to the google vision API, the vertices on index 1 is the top right corner
            face = ExtractedRect(vertices, *vertices)
            faces.append(face)
        return faces
