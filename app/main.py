from pymongo.mongo_client import MongoClient

from api.google_vision.face_detector import FaceDetector
from pipelines.face_detector_pipeline.phases.check_best_picture import CheckBestPictureCandidate

from config.config import Config

# Phases
from pipelines.face_detector_pipeline.phases.check_centered_faces import CheckIsFaceCentered
from pipelines.face_detector_pipeline.phases.format_data import FormatData
from pipelines.face_detector_pipeline.phases.generate_mongo_docs import GenerateDocsFromMongo
from pipelines.face_detector_pipeline.phases.process_face_detector import ProcessWithFaceDetector
from pipelines.face_detector_pipeline.phases.update_database import UpdateDatabase
from pipelines.core.runner import Runner


def main():
    with MongoClient(Config.DB_HOST, Config.DB_PORT) as client:
        face_detector = FaceDetector.from_default_client()
        db_input_name = Config.SOURCE_DB_NAME
        coll_input_name = Config.SOURCE_DB_COLLECTION
        db_output_name = Config.SINK_DB_NAME
        coll_output_name = Config.SINK_DB_COLLECTION
        pipeline = (GenerateDocsFromMongo(client, db_input_name, coll_input_name)
                    | ProcessWithFaceDetector(face_detector)
                    | CheckIsFaceCentered()
                    | CheckBestPictureCandidate()
                    | FormatData()
                    | UpdateDatabase(client, db_output_name, coll_output_name))
        Runner(pipeline).run()


if __name__ == '__main__':
    main()
