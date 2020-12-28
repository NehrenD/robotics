import json


class Parameters(dict):

    @classmethod
    def load_from_file(cls, file_name):
        with open(file_name) as json_file:
            d = json.load(json_file)
        return Parameters(d)

    def __init__(self, *args, **kwargs):
        super(Parameters, self).__init__(*args, **kwargs)
        self.__dict__ = self
