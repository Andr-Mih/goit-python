from abc import abstractmethod, ABC
import json
import pickle

class Serializ(ABC):

    @abstractmethod
    def serial_to_file(self, *args, **kwargs):
        raise NotImplementedError

class SerializJson(Serializ):

    def __init__(self, data):
        self.data = data

    def serial_to_file(self, file_name):
        with open(file_name, 'wb') as fh:
            json.dump(self.data, fh)

class SerializBin(Serializ):

    def __init__(self, data):
        self.data = data
    
    def serial_to_file(self, file_name):
        with open(file_name, 'wb') as fh:
            pickle.dump(self.data, fh)
           



a = SerializBin({1: 'wer', 2: '34'})
a.serial_to_file('file.bin')
b = SerializBin({1: 'wer', 2: '33'})
b.serial_to_file('file.json')

