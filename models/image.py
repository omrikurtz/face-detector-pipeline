import io
# My shitty IDE marks this import as an error. ?!?
from PIL import Image


class ImageModel:
    def __init__(self, uid: str, image: Image):
        self.uid = uid
        self.image = image
        pass

    @classmethod
    def from_bytes(cls, uid, data):
        image = Image.open(io.BytesIO(data))
        return cls(uid, image)

    @property
    def size(self):
        width, height = self.image.size
        return width, height

    @property
    def center(self):
        width, height = self.image.size
        return width / 2, height / 2

    def get_bytes(self):
        img_bytes = io.BytesIO()
        self.image.save(img_bytes, format=self.image.format)
        return img_bytes.getvalue()

    @property
    def area(self):
        width, height = self.image.size
        return width * height

    def get_ratio_to_rect(self, rect_width, rect_height):
        """
        Return the area-ratio of this image to some rectangle (perhaps another image)
        :param rect_width: Rectangle width in pixels
        :param rect_height: Rectangle height in pixels
        """
        return (rect_width * rect_height) / self.area
