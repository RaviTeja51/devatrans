import json
vowels_hk_back = {"a": "\u0905", "A": "\u0906", "i": "\u0907",
                  "I": "\u0908", "u": "\u0909", "U": "\u090A", "R": "\u090B",
                  "RR": "\u0960", "lR": "\u090C", "lRR": "\u0961",
                  "e": "\u090F", "ai": "\u0910", "o": "\u0913",
                  "au": "\u0914"}


consonant_hk_back = {"k": "\u0915", "kh": "\u0916", "g": "\u0917",
                     "gh": "\u0918", "G": "\u0919", "c": "\u091A",
                     "ch": "\u091B", "j": "\u091C", "jh": "\u091D",
                     "J": "\u091E", "T": "\u091F", "Th": "\u0920",
                     "D": "\u0921", "Dh": "\u0922", "N": "\u0923",
                     "t": "\u0924", "th": "\u0925", "d": "\u0926",
                     "dh": "\u0927", "n": "\u0928", "p": "\u092A",
                     "ph": "\u092B", "b": "\u092C", "bh": "\u092D",
                     "m": "\u092E", "y": "\u092F", "r": "\u0930",
                     "l": "\u0932", "v": "\u0935", "z": "\u0936",
                     "S": "\u0937", "s": "\u0938", "h": "\u0939"}

vowel_sign_hk_back = {"A": "\u093E", "i": "\u093F", "I": "\u0940", "u": "\u0941",
                      "U": "\u0942", "R": "\u0943", "RR": "\u0944", "e": "\u0947",
                      "ai": "\u0948", "o": "\u094B", "au": "\u094C", "lR": "\u0962", "lRR": "\u0963"}

hk_special_sign_bk = {"M": "\u0902", "H": "\u0903", "~": "\u0901"}

numbers_back = {"0": "\u0966", "1": "\u0967", "2": "\u0968", "3": "\u0969",
                "4": "\u096A", "5": "\u096B", "6": "\u096C", "7": "\u096D",
                "8": "\u096E", "9": "\u096F"}

harvard_kyoto_back = []
harvard_kyoto_back.append(vowels_hk_back)
harvard_kyoto_back.append(consonant_hk_back)
harvard_kyoto_back.append(vowel_sign_hk_back)
harvard_kyoto_back.append(numbers_back)
harvard_kyoto_back.append(hk_special_sign_bk)

with open("data/hk_back_trans.json", "w") as f:
    json.dump(harvard_kyoto_back, f, indent=4)

vowels_hk = {"\u0905": "a", "\u0906": "A", "\u0907": "i", "\u0908": "I",
             "\u0909": "u", "\u090A": "U", "\u090F": "e", "\u0910": "ai",
             "\u0913": "o", "\u0914": "au", "\u090B": "R", "\u0960": "RR",
             "\u090C": "lR", "\u0961": "lRR"}

hk_special_sign = {"\u0902": "M", "\u0903": "H", "\u0901": "~"}

consonants_hk = {"\u0915": "k", "\u0916": "kh", "\u0917": "g", "\u0918": "gh", "\u0919": "G",
                 "\u091A": "c", "\u091B": "ch", "\u091C": "j", "\u091D": "jh", "\u091E": "J",
                 "\u091F": "T", "\u0920": "Th", "\u0921": "D", "\u0922": "Dh", "\u0923": "N",
                 "\u0924": "t", "\u0925": "th", "\u0926": "d", "\u0927": "dh", "\u0928": "n",
                 "\u092A": "p", "\u092B": "ph", "\u092C": "b", "\u092D": "bh", "\u092E": "m",
                 "\u092F": "y", "\u0930": "r", "\u0932": "l", "\u0935": "v", "\u0936": "z",
                 "\u0937": "S", "\u0938": "s", "\u0939": "h"}

vowel_signs_hk = {"\u093E": "A", "\u093F": "i", "\u0940": "I", "\u0941": "u",
                  "\u0942": "U", "\u0943": "R", "\u0944": "RR", "\u0947": "e",
                  "\u0948": "ai", "\u094B": "o", "\u094C": "au", "\u0962": "lR",
                  "\u0963": "lRR", "\u094F": "au"}

numbers = {"\u0966": "0", "\u0967": "1", "\u0968": "2", "\u0969": "3", "\u096A": "4", "\u096B": "5",
           "\u096C": "6", "\u096D": "7", "\u096E": "8", "\u096F": "9"}


hk_transliteration = []
hk_transliteration.append(vowels_hk)
hk_transliteration.append(consonants_hk)
hk_transliteration.append(vowel_signs_hk)
hk_transliteration.append(numbers)
hk_transliteration.append(hk_special_sign)

with open("data/hk_trans.json", "w") as f:
    json.dump(hk_transliteration, f, indent=4)

iast_vowels = {"\u0905": "a", "\u0906": "ā", "\u0907": "i", "\u0908": "ī",
               "\u0909": "u", "\u090A": "ū", "\u090B": "ṛ", "\u0960": "ṝ",
               "\u090F": "e", "\u0910": "ai", "\u0911": "o", "\u0913": "o",
               "\u0914": "au", "\u0961": "Ḹ", "\u090C": "Ḷ"}

iast_special = {"\u0902": "ṃ", "\u0903": "ḥ", "\u0901": "˜", "\u093D": "'"}

iast_constants = {"\u0915": "k", "\u0916": "kh", "\u0917": "g", "\u0918": "gh",
                  "\u0919": "ṅ", "\u091A": "c", "\u091B": "ch", "\u091C": "j",
                  "\u091D": "jh", "\u091E": "ñ", "\u091F": "ṭ", "\u0920": "ṭh",
                  "\u0921": "ḍ", "\u0922": "ḍh", "\u0923": "ṇ", "\u0924": "t",
                  "\u0925": "th", "\u0926": "d", "\u0927": "dh", "\u0928": "n",
                  "\u092A": "p", "\u092B": "ph", "\u092C": "b", "\u092D": "bh",
                  "\u092E": "m", "\u092F": "y", "\u0930": "r", "\u0932": "l",
                  "\u0935": "v", "\u0936": "ś", "\u0937": "ṣ", "\u0938": "s",
                  "\u0939": "h"}

iast_vowel_sign = {"\u093E": "ā", "\u093F": "i", "\u0940": "ī", "\u0941": "u",
                   "\u0942": "ū", "\u0943": "ṛ", "\u0944": "ṝ", "\u0947": "e",
                   "\u0948": "ai", "\u094B": "o", "\u094C": "au", "\u0962": "ḷ",
                   "\u0963": "ḹ"}

iast_vowels_bk = {"a": "\u0905", "A": "\u0905", "ā": "\u0906", "Ā": "\u0906", "i": "\u0907",
                  "I": "\u0907", "ī": "\u0908", "Ī": "\u0908", "u": "\u0909", "U": "\u0909",
                  "ū": "\u090A", "Ū": "\u090A", "ṛ": "\u090B", "Ṛ": "\u090B", "Ḷ": "\u090C",
                  "Ḹ": "\u0961", "e": "\u090F", "E": "\u090F", "ai": "\u0910", "Ai": "\u0910",
                  "o": "\u0913", "O": "\u0913", "au": "\u0914", "Au": "\u0914", "'": "\u093D"}

iast_bk_sp = {"ṃ": "\u0902", "Ṃ": "\u0902", "ḥ": "\u0903", "Ḥ": "\u0903", "˜": "\u0901"}

iast_constant_bk = {"k": "\u0915", "k": "\u0915", "kh": "\u0916", "Kh": "\u0916", "g": "\u0917",
                    "G": "\u0917", "gh": "\u0918", "Gh": "\u0918", "ṅ": "\u0919", " Ṅ": "\u0919",
                    "c": "\u091A", "C": "\u091A", "ch": "\u091B", "Ch": "\u091B", "j": "\u091C",
                    "J": "\u091C", "Jh": "\u091D", "jh": "\u091D", "ñ": "\u091E", "Ñ": "\u091E",
                    "ṭ": "\u091F", " Ṭ": "\u091F", "ṭh": "\u0920", "Ṭh": "\u0920", "ḍ": "\u0921",
                    "Ḍ": "\u0921", "ḍh": "\u0922", "Ḍh": "\u0922", "ṇ": "\u0923", "Ṇ": "\u0923",
                    "t": "\u0924", "T": "\u0924", "th": "\u0925", "Th": "\u0925", "d": "\u0926",
                    "D": "\u0926", "dh": "\u0927", "Dh": "\u0927", "n": "\u0928", "N": "\u0928",
                    "p": "\u092A", "P": "\u092A", "ph": "\u092B", "Ph": "\u092B", "b": "\u092C",
                    "B": "\u092C", "bh": "\u092D", "Bh": "\u092D", "m": "\u092E", "M": "\u092E",
                    "y": "\u092F", "Y": "\u092F", "r": "\u0930", "R": "\u0930", "l": "\u0932",
                    "L": "\u0932", "v": "\u0935", "V": "\u0935", "ś": "\u0936 ", "Ś": "\u0936",
                    "ṣ": "\u0937", "Ṣ": "\u0937", "s": "\u0938", "S": "\u0938", "h": "\u0939",
                    "H": "\u0939"}

iast_vowel_sign_bk = {"ā": "\u093E", "Ā": "\u093E", "i": "\u093F", "I": "\u093F", "ī": "\u0940",
                      "Ī": "\u0940", "u": "\u0941", "U": "\u0941", "ū": "\u0942", "Ū": "\u0942",
                      "ṛ": "\u0943", "ṝ": "\u0944", "ḷ": "\u0962", "ḹ": "\u0963", "e": "\u0947",
                      "ai": "\u0948", "o": "\u094B", "au": "\u094C"}
iast_trans = []
iast_trans.append(iast_vowels)
iast_trans.append(iast_constants)
iast_trans.append(iast_vowel_sign)
iast_trans.append(numbers)
iast_trans.append(iast_special)

iast_bk_trans = []
iast_bk_trans.append(iast_vowels_bk)
iast_bk_trans.append(iast_constant_bk)
iast_bk_trans.append(iast_vowel_sign_bk)
iast_bk_trans.append(numbers_back)
iast_bk_trans.append(iast_bk_sp)


itrans_trans = []
itrans_vowels = {"\u0905": "a", "\u0906": "A", "\u0907": "i", "\u0908": "I", "\u0909": "u",
                 "\u090A": "U", "\u090B": "RRi", "\u0960": "RRI", "\u090C": "LLi", "\u0961": "LLI",
                 "\u090F": "e", "\u0910": "ai", "\u0913": "O", "\u0914": "Ou",
                 "\u093D": ".a", "\u0950": "OM", "\u0911": ".N"}

itrans_consonants = {"\u0915": "k", "\u0916": "kh", "\u0917": "g",
                     "\u0918": "gh", "\u0919": "~N", "\u091A": "ch",
                     "\u091B": "Ch", "\u091C": "j", "\u091D": "jh",
                     "\u091E": "~n", "\u091F": "T", "\u0920": "Th",
                     "\u0921": "D", "\u0922": "Dh", "\u0923": "N",
                     "\u0924": "t", "\u0925": "th", "\u0926": "d",
                     "\u0927": "dh", "\u0928": "n", "\u092A": "p",
                     "\u092B": "ph", "\u092C": "b", "\u092D": "bh",
                     "\u092E": "m", "\u092F": "y", "\u0930": "r",
                     "\u0932": "l", "\u0935": "v", "\u0936": "sh",
                     "\u0937": "Sh", "\u0938": "s", "\u0939": "h",
                     "\u0958": "q", "\u0959": "K", "\u095A": "G",
                     "\u095B": "z", "\u095C": ".D", "\u095D": ".Dh",
                     "\u095E": "f"}

itrans_vowels_sign = {"\u093E": "A", "\u093F": "i", "\u0940": "I",
                      "\u0941": "u", "\u0942": "U", "\u0943": "RRi",
                      "\u0944": "RRI", "\u0945": ".N", "\u0947": "e",
                      "\u0948": "ai", "\u094B": "O", "\u094C": "Ou",
                      "\u0962": "LLi", "\u0963": "LLI"
                      }

itrans_sp = {"\u0901": ".N", "\u0902": "M", "\u0903": "H"}

itrans_trans.append(itrans_vowels)
itrans_trans.append(itrans_consonants)
itrans_trans.append(itrans_vowels_sign)
itrans_trans.append(numbers)
itrans_trans.append(itrans_sp)

itrans_bk = []

itrans_vowel_bk = {"a": "\u0905", "A": "\u0906", "aa": "\u0906",
                   "i": "\u0907", "I": "\u0908", "u": "\u0909",
                   "U": "\u090A", "uu": "\u090A", "RRi": "\u090B",
                   "R^i": "\u090B", "RRI": "\u0960", "R^I": "\u0960",
                   "LLi": "\u090C", "L^i": "\u090C", "LLI": "\u0961",
                   "L^I": "\u0961", "e": "\u090F", "ee": "\u090F",
                   "Ē": "\u090F", "ēē": "\u090F", "Ei": "\u0910",
                   "O": "\u0913", "oo": "\u0913", "Ō": "\u0913",
                   "ōō": "\u0913", ".a": "\u093D", ".N": "\u0911",
                   "ai": "\u0910"}

itrans_sp_bk = {"Ou": "\u0902", "M": "\u0902", "N": "\u0902",
                ".m": "\u0902", "H": "\u0903", ".N": "\u0901"}

itrans_consonants_bk = {"k": "\u0915", "kh": "\u0916", "g": "\u0917",
                        "gh": "\u0918", "~N": "\u0919", "ch": "\u091A",
                        "Ch": "\u091B", "j": "\u091C", "jh": "\u091D",
                        "~n": "\u091E", "T": "\u091F", "Th": "\u0920",
                        "D": "\u0921", "Dh": "\u0922", "N": "\u0923",
                        "t": "\u0924", "th": "\u0925", "d": "\u0926",
                        "dh": "\u0927", "n": "\u0928", "p": "\u092A",
                        "ph": "\u092B", "b": "\u092C", "bh": "\u092D",
                        "m": "\u092E", "y": "\u092F", "r": "\u0930",
                        "l": "\u0932", "v": "\u0935", "sh": "\u0936",
                        "Sh": "\u0937", "s": "\u0938", "h": "\u0939",
                        "q": "\u0958", "K": "\u0959", "G": "\u095A",
                        "z": "\u095B", ".D": "\u095C", ".Dh": "\u095D",
                        "f": "\u095E"}

itrans_vowel_bk_sign = {
    "A": "\u093E", "aa": "\u093E", "i": "\u093F",
    "I": "\u0940", "ii": "\u0940", "u": "\u0941",
    "U": "\u0942", "uu": "\u0942", "RRi": "\u0943",
    "R^i": "\u0943", "RRI": "\u0944", "R^I": "\u0944",
    "E": "\u0947", "ai": "\u0948",
    "O": "\u094B", "oo": "\u094B", "Ou": "\u094C",
    "ee": "\u0947", "Ē": "\u0947", "ēē": "\u0947",
    "LLi": "\u0962", "LLI": "\u0963", "L^i": "\u0962",
    "L^I": "\u0963"
}

itrans_bk.append(itrans_vowel_bk)
itrans_bk.append(itrans_consonants_bk)
itrans_bk.append(itrans_vowel_bk_sign)
itrans_bk.append(numbers_back)
itrans_bk.append(itrans_sp_bk)


velthuis_vowel = {
    "\u0905": "a", "\u0906": "aa", "\u0907": "i",
    "\u0908": "ii", "\u0909": "u", "\u090A": "uu",
    "\u090B": ".r", "\u0960": ".rr", "\u090C": ".l",
    "\u0961": ".ll", "\u090F": "e", "\u0910": "ai",
    "\u0913": "o", "\u0914": "au", "\u0911": "/",
    "\u093D": ".a", "\u0950": "O"}

velthuis_sp = {"\u0902": ".m", "\u0903": ".h", "\u0901": "/"}

velthuis_consonant = {"\u0915": "k", "\u0916": "kh", "\u0917": "g",
                      "\u0918": "gh", "\u0919": '"n', "\u091A": "c",
                      "\u091B": "ch", "\u091C": "j", "\u091D": "jh",
                      "\u091E": "~n", "\u091F": ".t", "\u0920": ".th",
                      "\u0921": ".d", "\u0922": ".dh", "\u0923": ".n",
                      "\u0924": "t", "\u0925": "th", "\u0926": "d",
                      "\u0927": "dh", "\u0928": "n", "\u092A": "p",
                      "\u092B": "ph", "\u092C": "b", "\u092D": "bh",
                      "\u092E": "m", "\u092F": "y", "\u0930": "r",
                      "\u0932": "l", "\u0935": "v", "\u0936": '"s',
                      "\u0937": ".s", "\u0938": "s", "\u0939": "h"
                      }

velthuis_vowel_sign = {"\u093E": "aa", "\u093F": "i", "\u0940": "ii",
                       "\u0941": "u", "\u0942": "uu", "\u0943": ".r",
                       "\u0944": ".rr", "\u0962": ".l", "\u0963": ".ll",
                       "\u0947": "e", "\u0948": "ai", "\u094B": "o",
                       "\u094C": "au"}


velthuis_vowel_bk = {
    "a": "\u0905", "aa": "\u0906", "i": "\u0907",
    "ii": "\u0908", "u": "\u0909", "uu": "\u090A",
    ".r": "\u090B", ".rr": "\u0960", ".l": "\u090C",
    ".ll": "\u0961", "e": "\u090F", "ai": "\u0910",
    "o": "\u0913", "au": "\u0914", "\u093D": ".a",
    "\u0950": "O"}

velthuis_consonant_bk = {
    "k": "\u0915", "kh": "\u0916", "g": "\u0917",
    "gh": "\u0918", '"n': '\u0919', "c": "\u091A",
    "ch": "\u091B", "j": "\u091C", "jh": "\u091D",
    "~n": "\u091E", ".t": "\u091F", ".th": "\u0920",
    ".d": "\u0921", ".dh": "\u0922", "n": "\u0923.",
    "t": "\u0924", "th": "\u0925", "d": "\u0926",
    "dh": "\u0927", "n": "\u0928", "p": "\u092A",
    "ph": "\u092B", "b": "\u092C", "bh": "\u092D",
    "m": "\u092E", "y": "\u092F", "r": "\u0930",
    "l": "\u0932", "v": "\u0935", '"s': '\u0936',
    ".s": "\u0937", "s": "\u0938", "h": "\u0939"
}

velthuis_sp_bk = {".m": "\u0902", ".h": "\u0903", "/": "\u0901"}

velthuis_vowel_sign_bk = {"aa": "\u093E", "i": "\u093F", "ii": "\u0940",
                          "u": "\u0941", "uu": "\u0942", ".r": "\u0943",
                          ".rr": "\u0944", ".l": "\u0962", ".ll": "\u0963",
                          "e": "\u0947", "ai": "\u0948", "o": "\u094B",
                          "au": "\u094C"}

velthuis = []
velthuis.append(velthuis_vowel)
velthuis.append(velthuis_consonant)
velthuis.append(velthuis_vowel_sign)
velthuis.append(numbers)
velthuis.append(velthuis_sp)

velthuis_bk = []
velthuis_bk.append(velthuis_vowel_bk)
velthuis_bk.append(velthuis_consonant_bk)
velthuis_bk.append(velthuis_vowel_sign_bk)
velthuis_bk.append(numbers_back)
velthuis_bk.append(velthuis_sp_bk)

san_vowel = ["\u0905", "\u0906", "\u0907",
             "\u0908", "\u0909", "\u090A",
             "\u090B", "\u0960", "\u090C",
             "\u0961", "\u090F", "\u0910",
             "\u0913", "\u0914", "\u0911",
             "\u093D", "\u0950"]

san_consonant = ["\u0915", "\u0916", "\u0917", "\u0918", "\u0919", "\u091A",
                 "\u091B", "\u091C", "\u091D", "\u091E", "\u091F", "\u0920",
                 "\u0921", "\u0922", "\u0923", "\u0924", "\u0925", "\u0926",
                 "\u0927", "\u0928", "\u092A", "\u092B", "\u092C", "\u092D",
                 "\u092E", "\u092F", "\u0930", "\u0932", "\u0935", "\u0936",
                 "\u0937", "\u0938", "\u0939", "\u0958", "\u0959", "\u095A",
                 "\u095B", "\u095C", "\u095D", "\u095E", "\u095F"]

san_vowel_sign = {"\u0906": "\u093E", "\u0907": "\u093F", "\u0908": "\u0940",
                  "\u0909": "\u0941", "\u090A": "\u0942", "\u090B": "\u0943",
                  "\u0960": "\u0944", "\u090F": "\u0947", "\u0910": "\u0948",
                  "\u0913": "\u094B", "\u0914": "\u094C", "\u090C": "\u0962", "\u0963": "\u0963"}


san_sp = ["\u0901", "\u0902", "\u0903"]

num = ["\u0966", "\u0967", "\u0968", "\u0969",
       "\u096A", "\u096B", "\u096C", "\u096D",
       "\u096E", "\u096F"]

sanskrit = []
sanskrit.append(san_vowel)
sanskrit.append(san_consonant)
sanskrit.append(san_vowel_sign)
sanskrit.append(num)
sanskrit.append(san_sp)

with open("data/iast_trans.json", "w") as f:
    json.dump(iast_trans, f, indent=4)

with open("data/iast_back_trans.json", "w") as f:
    json.dump(iast_bk_trans, f, indent=4)

with open("data/itrans_trans.json", "w") as f:
    json.dump(itrans_trans, f, indent=4)

with open("data/itrans_back_trans.json", "w") as f:
    json.dump(itrans_bk, f, indent=4)

with open("data/velthuis_trans.json", "w") as f:
    json.dump(velthuis, f, indent=4)

with open("data/velthuis_back_trans.json", "w") as f:
    json.dump(velthuis_bk, f, indent=4)

with open("data/sanskrit.json", "w") as f:
    json.dump(sanskrit, f, indent=4)
