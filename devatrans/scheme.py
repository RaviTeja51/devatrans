import json
import os

class Scheme:
    """The Scheme class stores the  characters of the encoding scheme
       as vowels, consonants, vowel_sign, numbers, special characters.
    """

    def __init__(self, open_file, name):

        dir_path = os.path.abspath(os.path.dirname(__file__))

        open_file = os.path.join(dir_path, open_file)
        
        # loading the character set of the encoding scheme
        with open(open_file) as file:
            data = json.load(file)
        self.name = name
        self.vowels = data[0]
        self.consonants = data[1]
        self.vowel_sign = data[2]
        self.numbers = data[3]
        self.sp = data[4]


if __name__ == "__main__":
    MyScheme = Scheme("data/hk_trans.json")
    print(MyScheme.vowels)
