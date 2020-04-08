from pipelines.core.pipeline import Pipeline


class CheckIsFaceCentered(Pipeline):
    def map(self, doc):
        image_model = doc['__model']
        width, height = image_model.center
        # Some next level shit. Just kidding, merely dictionary compositions
        doc['faces'] = [dict(item, **{'is_center': self.is_center(item['face_data'], width, height)}) for item in
                        doc['faces']]
        return doc

    @staticmethod
    def is_center(face, width, height):
        face_x_range = (face.top_left_corner.x, face.bottom_right_corner.x)
        face_y_range = (face.top_left_corner.y, face.bottom_right_corner.y)
        return face_x_range[0] < width < face_x_range[1] and face_y_range[0] < height < face_y_range[1]
