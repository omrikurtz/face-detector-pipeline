from pipelines.core.pipeline import Pipeline


class Runner:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def run(self):
        if isinstance(self.pipeline, Pipeline):
            try:
                for _ in self.pipeline:
                    pass
            except RuntimeError as e:
                return True
            else:
                return False
        else:
            raise TypeError(
                f"Input pipeline is not a pipeline but an object of type {type(self.pipeline)}")
