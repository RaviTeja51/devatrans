""" The module `devatrans` can be used in transliterating SANSKIRT into
    IAST,Harvard-Kyoto, ITRANS, Velthuis.

    It can also be used to back transliterate from IAST,Harvard-Kyoto,
    ITRANS, Velthuis to SANSKRIT.

    The transliteration can be interportable.

     Class
     _ _ _ _
     DevaTrans : This class can be used for transliteration,
                back transliteraton, inter trans transliteration.
"""

import os
from sys import argv
from .scheme import Scheme


class DevaTrans:
    """The DevaTrans class can be used for transliteration,
       back transliteration, inter transliteration from one
       convention to another.

       Attributes
       _ _ _ _ _ _

       hk : Scheme
           The character set in Harvard-Kyoto convention used in transliteration
           of SANSKRIT to Harvard-Kyoto.

       hk_back : Scheme
               The character set  in Harvard-Kyoto convention used in back transliteration
               of Harvard-Kyoto to SANSKRIT.

       iast : Scheme
           The character set in IAST convention used in transliteration
           of SANSKIRT to IAST.

       iast_back : Scheme
               The character set in IAST convention used in back transliteration
               of IAST to SANSKIRT.

       itrans : Scheme
            The character set in ITRANS convention used in transliteration
            of SANSKIRT to ITRANS.

       itrans_back : Scheme
                The character set in ITRANS convention used in back transliteration
                of ITRANS to SANSKIRT.

       velthuis : Scheme
            The character set in VELTHUIS convention used in transliteration
            of SANSKIRT to VELTHUIS.

       velthuis_back : Scheme
                The character set in VELTHUIS convention used in back transliteration
                of VELTHUIS to SANSKIRT.

        sanskrit : SANSKIRT character set.

        encoding_schema : dict
                    A dictionary of reference's of the Scheme attributes used for quick access.


        Methods
        _ _ _ _ _ _ _ _

        transliterate(input_type, to_convention, inp_file_path=None,
                          op_file_path=None,  sentence=None)
                     Transliterates the given sentence/file from
                     SANSKIRT to the convention specified.

        back_transliterate(input_type, from_convention, inp_file_path=None,
                               op_file_path=None,  sentence=None)
                     Back transliterates the given sentence/file from
                     the specified convention to SANSKIRT.

        inter_transliterate(input_type, from_convention, to_convention, inp_file_path=None,
                                op_file_path=None,  sentence=None)
                     Inter transliterates the given sentence/file from
                     one specified convention to another.
    """

    def __init__(self):
        """ Harvard-Kyoto convention """
        self.hk = Scheme(os.path.join("data", "hk_trans.json"), "Harvard-Kyoto")
        self.hk_back = Scheme(os.path.join("data", "hk_back_trans.json"), "Harvard-Kyoto_Back")

        """ IAST convention """
        self.iast = Scheme(os.path.join("data", "iast_trans.json"), "IAST")
        self.iast_back = Scheme(os.path.join("data", "iast_back_trans.json"), "IAST_Back")

        """ ITRANS convention """
        self.itrans = Scheme(os.path.join("data", "itrans_trans.json"), "ITRANS")
        self.itrans_back = Scheme(os.path.join("data", "itrans_back_trans.json"), "ITRANS_Back")

        """ Velthuis convention """
        self.velthuis = Scheme(os.path.join("data", "velthuis_trans.json"), "Velthuis")
        self.velthuis_back = Scheme(os.path.join(
            "data", "velthuis_back_trans.json"), "Velthuis_Back")

        self.encoding_schema = {"hk": self.hk, "hk_back": self.hk_back,
                                "itrans": self.itrans,
                                "itrans_back": self.itrans_back,
                                "iast": self.iast,
                                "iast_back": self.iast_back,
                                "velthuis": self.velthuis,
                                "velthuis_back": self.velthuis_back
                                }

        """ Sanskrit characters """
        self.sanskrit = Scheme(os.path.join("data", "sanskrit.json"), "Velthuis")

    def __find_character_pos(self, sentence, from_conven):
        """This method is used to transform the characters in the
           sentence into sanskrit characters, used as a utiliy method.

           Parameters
           _ _ _ _ _ _ _ _
           sentence : str
                    The sentence to be mapped back into SANSKIRT.

           from_conven : str
                       The convention from which the sentence is to be
                       back transliterated into SANSKIRT.
            Returns:
            _ _ _ _ _
             list of characters in sanskrit original present in
                     the parameter `sentence`.
           """

        # To find out if the sub-string starting from "index" to "final_pos"
        # is present in from_conven, if substring is present then find its
        # representation in sanskrit.

        from_conven = f"{from_conven}_back"  # to map back into sanskrit
        index = 0
        sen_length = len(sentence)
        char_pos = []

        while index < sen_length:

            final_pos = 5
            char_found = False
            while final_pos >= 0 :
                # final_pos = 5 because the maximum length of
                # the characters is 5.
                # If the substring is found break from the inner loop and
                # repeat the same search again from the previously stopped index.
                if (index + final_pos) <= sen_length:
                    if (sentence[index:(index + final_pos)] in
                    self.encoding_schema[from_conven].vowels):
                        char_pos.append(
                          self.encoding_schema[from_conven].vowels[sentence[index:(index + final_pos)]])
                        char_found = True
                        index += final_pos  # updating the last stopped index
                        break

                    elif (sentence[index:(index + final_pos)] in
                      self.encoding_schema[from_conven].consonants):

                    # In case of consonant there is an additional 'h' for
                    # ख,छ,ठ,थ,फ
                        if ((index + final_pos + 1 <= sen_length)
                              and sentence[index + final_pos:(index + final_pos + 1)] == 'h'
                              and sentence[index:(index + final_pos+1)] in
                              self.encoding_schema[from_conven].consonants):
                                 final_pos += 1  # updating the last stopped index

                        char_pos.append(
                           self.encoding_schema[from_conven].consonants[sentence[index:(index + final_pos)]])
                        char_found = True
                        index += final_pos  # updating the last stopped index
                        break

                    elif (sentence[index:(index + final_pos)] in
                        self.encoding_schema[from_conven].vowel_sign):

                        char_pos.append(
                             self.encoding_schema[from_conven].vowel_sign[sentence[index:(index + final_pos)]])
                        char_found = True
                        index += final_pos  # updating the last stopped index
                        break

                    elif (sentence[index:(index + final_pos)] in
                           self.encoding_schema[from_conven].numbers):

                        char_pos.append(
                           self.encoding_schema[from_conven].numbers[sentence[index:(index + final_pos)]])
                        char_found = True
                        index += final_pos  # updating the last stopped index
                        break

                    elif (sentence[index:(index + final_pos)] in
                          self.encoding_schema[from_conven].sp):

                        char_pos.append(
                          self.encoding_schema[from_conven].sp[sentence[index:(index + final_pos)]])
                        char_found = True
                        index += final_pos  # updating the last stopped index
                        break

                final_pos -= 1

            # if no equivqlent character is found even after looking fo a
            # length of 5, it means the character dosen't exist in the
            # from_conven set, so append it to the list without making
            # any changes.
            if not char_found:
                char_pos.append(sentence[index:index+1])
                index += 1  # updating the last stopped index

        return char_pos

    def __transliterator(self, sen, to_conven):
        """This method is used to transliterate the characters in the
           `sentence` from sanskrit to characters in `to_conven`, used as a utiliy method.

           Parameters
           _ _ _ _ _ _
           sentence : str
                    The sentence to be mapped back into SANSKIRT.

           to_conven : str
                       The convention to which the sentence is to be
                        transliterated from SANSKIRT.
           Returns
           _ _ _ _ _ _ _
            string of characters in `to_conven` original present in
                     the parameter `sentence`.
           """

        line = []
        sen_length = len(sen)

        i = 0

        # Iterating through each character in the sentence.
        while i < sen_length:
            char = sen[i]

            if char in self.encoding_schema[to_conven].vowels:
                line.append(self.encoding_schema[to_conven].vowels[char])

            elif char in self.encoding_schema[to_conven].consonants:
                line.append(self.encoding_schema[to_conven].consonants[char])
                # If the current character is consonant and if the next character
                # is not either vowel or vowel sign then add 'a' to the character
                # this is done to remove halant.
                if (i+1 < sen_length and
                    (sen[i+1] not in self.encoding_schema[to_conven].vowels and
                     sen[i+1] not in self.encoding_schema[to_conven].vowel_sign and
                     sen[i+1] != "\u094D")):
                    line.append("a")

                elif i+1 == sen_length:
                    line.append("a")

            elif char in self.encoding_schema[to_conven].vowel_sign:
                line.append(self.encoding_schema[to_conven].vowel_sign[char])

            elif char in self.encoding_schema[to_conven].numbers:
                line.append(self.encoding_schema[to_conven].numbers[char])

            elif char in self.encoding_schema[to_conven].sp:
                line.append(self.encoding_schema[to_conven].sp[char])

            # halant is not added because it is added to the character
            #in the character set.
            elif char != "\u094D":
                line.append(char)

            i += 1

        return("".join(line))

    def transliterate(self, input_type, to_convention, inp_file_path=None,
                      op_file_path=None,  sentence=None):
        """This method transliterates the input which would be in SANSKIRT
           into the specified convention. If characters which are not present
           in the specified convention, they are left unchanged.

           The method works for a sentence or for a text file.

           Parameters
           _ _ _ _ _ _
           input_type : str
                 It should be either "sen" or "file", denotes the format of the input,
                 the file should be in text format.

           to_convention : str
                 It is the convention into which the input file/sentence is
                 transliterated from sanskrit.

           inp_file_path : str
                 It is the path of the text file to be transliterated(default value is None),
                 the path should be provided if the `input_type` is "file"

          op_file_path : str
                 It is the path of file(default value is None) to which the
                 transliterated text is written to, the path should be provided
                 if the `input_type` is "file".
                 If op_file_path is not provided then the transliterated text is written
                 to  location `inp_file_path`.

          sen : str
               It is the sentence to be transliterated, it should be passed
               if `input_type` is "sen".

           Raises
           _ _ _ _ _ _ _ _
            TypeError
                If to_covention is not amongst hk,iast,itrans,velthuis.
                If `input_type` is "file" and if `inp_file_path` is None.
                If `input_type` is "sen" and if `sentence` is None.
                If `input_type` is neither "sen" nor "file".

            Returns
            _ _ _ _ _ _ _ _
            If `input_type` is "sen" then the sentence which is transliterated into
            the `to_convention` is returned.

            If `input_type` is "file" then the statement
            "Tranliteration of the text completed" is returned after
            transliterating the text file into `to_convnetion`.
        """

        if to_convention not in self.encoding_schema:
            raise TypeError("Invalid 'to convention'")

        if input_type == "file":
            with open(inp_file_path, "r") as f:

                trans_txt = []
                for line in f:
                    trans_txt.append(self.__transliterator(line, to_convention))

            if op_file_path is None:
                op_file_path = inp_file_path

            with open(op_file_path, "w") as f:
                for line in trans_txt:
                    f.write(line)
            return("Tranliteration of the text completed")

        elif input_type == "sen":
            if sentence is None:
                raise TypeError("sentence should be provided  for tranliteration")
            else:
                return(self.__transliterator(sentence, to_convention))
        else:
            raise TypeError("Invalid 'input_type' argument")

    def __inter_transliterator(self, sentence, from_conven, to_conven):
        """This method inter transliterates  the `sentence` from `from_conven` to  `to_coven`,
           this method is used as utility method.

           Parameters
           _ _ _ _ _ _ _ _
           sentence : str
                sentence to be inter transliterated.
           from_conven : str
                from convention
           to_conven : str
                to convention

           Returns
           _ _ _ _ _ _ _ _
           String is returned
           The sentence after  transliterated from one convention into another.
        """

        ## IDEA: The snetence is first back transliterated into SANSKRIT
        # from `from_conven` and then it is mapped to corressponding
        #character in `to_conven`. If character is not in `to_conven`
        #than it remains unchanged and is added to the list.
        line = self.__find_character_pos(sentence, from_conven)
        line = "".join(line)
        proc_txt = []
        prev_char_consonant = False

        for char in line:

            if char in self.encoding_schema[to_conven].consonants:
                proc_txt.append(self.encoding_schema[to_conven].consonants[char])
                prev_char_consonant = True

            elif char in self.encoding_schema[to_conven].vowels:

                if prev_char_consonant and char == "\u0905": #To remove the halant.
                    proc_txt.append("a")
                else:
                    if char in self.encoding_schema[to_conven].vowel_sign:
                        proc_txt.append(self.encoding_schema[to_conven].vowel_sign[char])
                    else:
                        proc_txt.append(self.encoding_schema[to_conven].vowels[char])
                prev_char_consonant = False

            elif char in self.encoding_schema[to_conven].numbers:
                proc_txt.append(self.encoding_schema[to_conven].numbers[char])
                prev_char_consonant = False

            elif char in self.encoding_schema[to_conven].sp:
                proc_txt.append(self.encoding_schema[to_conven].sp[char])
                prev_char_consonant = False

            else:
                proc_txt.append(char)
                prev_char_consonant = False

        return("".join(proc_txt))

    def inter_transliterate(self, input_type, from_convention, to_convention, inp_file_path=None,
                            op_file_path=None,  sentence=None):
        """This method is used for transliterating the input from one
           convention to another convention.

           # NOTE: If the input should only contain the text to be
           inter transliterated, if other characters they might be
           transliterated as well.

           Parameters
           _ _ _ _ _ _ _ _
           input_type : str
                It denoted the type of input, it can only take values
                 "sen" and "file".

           from_convention : str
                It specifies the convention from which the input is inter
                transliterated into another.

           to_convention : str
                It specifies the convention into which the input is inter
                transliterated into.

           inp_file_path : str
                The location of the file which is to be inter
                transliterated into.It is should be speciifed if
                `input_type` is "file".

           op_file_path : str
                It is the path of file(default value is None) to which the
                transliterated text is written to, the path should be provided
                if the `input_type` is "file".
                If op_file_path is not provided then the transliterated text is written
                to  location `inp_file_path`.

          Raises
          _ _ _ _ _ _ _ _
              TypeError
                  If `from_convention` is not amongst hk,iast,itrans,velthuis.
                  If `to_covention` is not amongst hk,iast,itrans,velthuis.
                  If `input_type` is "file" and if `inp_file_path` is None.
                  If `input_type` is "sen" and if `sentence` is None.
                  If `input_type` is neither "sen" nor "file".
        Returns
        _ _ _ _ _ _ _ _
             If `input_type` is "sen" then the inter transliterated
             sentece is returned.
             If `input_type` is "file" then the statement
             "Inter Transliteration of the text completed" is returned.
        """
        if from_convention not in self.encoding_schema:
            raise TypeError("'from' should be in hk, iast, itrans, velthuis")

        if to_convention not in self.encoding_schema:
            raise TypeError("'to_covention' should be in hk, iast, itrans, velthuis")

        if input_type == 'file':

            if inp_file_path is None:
                raise TypeError("'inp_file_path' cannot be None")
            if op_file_path is None:
                op_file_path = inp_file_path

            trans_txt = []
            with open(inp_file_path, "r") as file:

                for line in file:
                    trans_txt.append(self.__inter_transliterator(
                        line, from_convention, to_convention))

            with open(op_file_path, "w") as file:
                for line in trans_txt:
                    file.write(line)

            return("Inter Transliteration of the text completed")

        elif input_type == 'sen':
            if sentence is None:
                raise TypeError("'sentence' should be provided")
            else:
                return(self.__inter_transliterator(sentence, from_convention, to_convention))

        else:
            raise TypeError("Invalid 'input_type'")

    def __back_transliterator(self, sentence, from_conven):
        """This method back transliterates  the `sentence` from `from_conven` to  SANSKIRT
           this method is used as utility method.

           Parameters
           _ _ _ _ _ _ _ _
           sentence : str
                sentence to be back transliterated.
           from_conven : str
                from convention

           Returns
           _ _ _ _ _ _ _ _
           String is returned
           The sentence after  transliterated from specified convention to SANSKIRT.
        """
        ## IDEA: The sentence is first mapped back to sanskrit based on `from_conven`
        #If the character is not in `from_conven` it is left unchanged and is added
        #to the list.
        sen = self.__find_character_pos(sentence, from_conven)
        prev_char_consonant = False
        trans_txt = []
        for char in sen:

            if (prev_char_consonant and (char in self.sanskrit.vowels)):
                #If prev_char_consonant is True than the last character
                #is halant remove it.
                trans_txt.pop()
                if char != "\u0905":
                #since \u0905 is अ, it does not have vowel sign so simply
                #remove halant
                    trans_txt.append(self.sanskrit.vowel_sign[char])
                prev_char_consonant = False



            elif not prev_char_consonant and char in self.sanskrit.vowels:
                prev_char_consonant = False
                trans_txt.append(char)

            elif char in self.sanskrit.consonants:
                prev_char_consonant = True
                trans_txt.append(char)
                #Append halant if current character is consonant.
                trans_txt.append("्")


            else:
                trans_txt.append(char)
                prev_char_consonant = False

        return("".join(trans_txt))

    def back_transliterate(self, input_type, from_convention, inp_file_path=None,
                           op_file_path=None,  sentence=None):
        """This method is used for back transliterating the input from one
           convention to SANSKIRT.

           # NOTE: If the input should only contain the text to be
           back transliterated, if other characters they might be
           transliterated as well.

           Parameters
           _ _ _ _ _ _ _ _
           input_type : str
                It denoted the type of input, it can only take values
                 "sen" and "file".

           from_convention : str
                It specifies the convention from which the input is inter
                transliterated into another.

           inp_file_path : str
                The location of the file which is to be inter
                transliterated into.It is should be speciifed if
                `input_type` is "file".

           op_file_path : str
                It is the path of file(default value is None) to which the
                transliterated text is written to, the path should be provided
                if the `input_type` is "file".
                If op_file_path is not provided then the transliterated text is written
                to  location `inp_file_path`.

          Raises
          _ _ _ _ _ _ _ _
              TypeError
                  If `from_convention` is not amongst hk,iast,itrans,velthuis.
                  If `input_type` is "file" and if `inp_file_path` is None.
                  If `input_type` is "sen" and if `sentence` is None.
                  If `input_type` is neither "sen" nor "file".
        Returns
        _ _ _ _ _ _ _ _
             If `input_type` is "sen" then the back transliterated
             sentece is returned.
             If `input_type` is "file" then the statement
             "Back Tranliteration of the text completed"  is returned.
        """

        if from_convention not in self.encoding_schema:
            raise TypeError("Invalid 'from convention'")

        if input_type == "file":
            with open(inp_file_path, "r") as f:

                trans_txt = []
                for line in f:
                    trans_txt.append(self.__back_transliterator(line, from_convention))

            if op_file_path is None:
                op_file_path = inp_file_path

            with open(op_file_path, "w") as f:
                for line in trans_txt:
                    f.write(line)
            return("Back Tranliteration of the text completed")

        elif input_type == "sen":
            if sentence is None:
                raise TypeError("sentence should be provided  for back tranliteration")
            else:
                return(self.__back_transliterator(sentence, from_convention))
        else:
            raise TypeError("Invalid 'input_type' argument")
