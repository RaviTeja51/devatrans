import unittest
from devatrans import DevaTrans
class TestDevTrans(unittest.TestCase):

    """To test if transliteraton of  sanskrit is working"""
    def test_transliterate_sentence(self):
        #print("Testing transliterate")
        assert DevaTrans().transliterate("sen","hk",sentence = "छ") == "cha", "it is not working"


    """To test if input is english"""
    def test_transliterate_eng(self):
        #print("Testing transliterate when non sanskrit is given")
        assert DevaTrans().transliterate("sen","hk",sentence = "cool") == "cool", "it is not working"

    def test_transliterate_file(self):
        #print("Testing transliterate when non sanskrit is given")
        assert DevaTrans().transliterate("file","hk",inp_file_path = "data/s.txt",op_file_path = "data/f.txt") == "Tranliteration of the text completed", "it is not working"


    def test_back_transliterate(self):
        #print("Checking back transliteration")
        #print(DevaTrans().back_transliterate("sen","hk",sentence = "li"))
        assert DevaTrans().back_transliterate("sen","hk",sentence = "cha") =="छ", "re-check the algorithm"


    def test_inter_transliterate(self):

        assert DevaTrans().inter_transliterate("sen",from_convention = "hk",to_convention = "iast",sentence = "ch") =="ch", "re-check the algorithm"

    def test_inter_transliterate_txt(self):
        assert DevaTrans().inter_transliterate("file","hk","velthuis",inp_file_path = "data/f.txt",op_file_path = "data/g.txt") == "Inter Transliteration of the text completed", "it is not working"

    def test_back_transliterate_txt(self):
        assert DevaTrans().back_transliterate("file","hk",inp_file_path = "data/f.txt",op_file_path = "data/h.txt") == "Back Tranliteration of the text completed", "it is not working"



if __name__ == '__main__':
    unittest.main()
