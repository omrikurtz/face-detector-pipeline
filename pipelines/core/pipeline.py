"""
A class for representing Unix-like pipes for our data pipeline.
This class is the base class for the other pipelines.
We chain together different pipeline objects just like we do on Unix-like systems. Isn't it fun?!
This will help us process the data-pipeline objects efficiently and conservatively.
We can easily implement caching, persisting and other neat features with this skeleton
"""


class Pipeline(object):
    def __init__(self):
        self.source = None

    def __iter__(self):
        return self.generator()

    def generator(self):
        while True:
            value = self.source.__next__()
            if self.filter(value):
                yield self.map(value)

    def __or__(self, other):
        """
        This one's tricky! You might call it abuse, I call it kinda elegant.
        Implementing __or__ in this manner lets us conform to Unix-like pipes syntax for our data pipeline.
        For instance, lets say we have 2 phases of processings, and a database insert phase, we can write it as:
        first_phase | second_phase | put_to_database_phase
        :param other: The next pipeline phase.
        :return: The other pipeline, so we can chain the phases together
        """
        other.source = self.generator()
        return other

    def filter(self, value):
        # This is here just for the record, no pun intended. I didn't actually implement any filters
        return True

    def map(self, value):
        return value
