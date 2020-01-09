# devatrans

This is a simple tool to **transliterate** SANSKRIT text  to IAST, Harvard-Kyoto, ITRANS, Velthuis convention. It can also be used to **back transliterate** from IAST, Harvard-Kyoto, ITRANS, Velthuis convention to Sanskrit. It is can be used to **inter transliterate** from one convention to another.


### It works with:
              International Alphabet of Sanskrit Transliteration(IAST)
              Indian language transliteration(ITRANS)
              Harvard-Kyoto(HK)
              Velthuis

## Code Example
____

```python
from devatrans import DevaTrans

#create DevaTrans object.
dt = DevaTrans()
```

transliteration of a sentence.
```python
trans = dt.transliterate(input_type = "sen", to_convention = "hk", sentence = "नारायणं")
print(trans)
#output: nArAyaNaM
```

transliteration of a text file.
```python
dt.transliterate(input_type = "file", to_convetion = "iast", inp_file_path = "path_to_inp_file",
                  op_file_path = "path_to_out_file")
```    

back transliteration of a sentence.
```python
back_trans = dt.back_transliterate(input_type = "sen", from_convention = "hk", sentence = "nArAyaNaM")
print(back_trans)
#output: नारायणं
```

back transliteration of a text file.
```python
dt.back_transliterate(input_type = "file", from_convention = "itrans",
                inp_file_path = "path_to_inp_file",op_file_path = "path_to_out_file")                 
```

inter transliteration of a sentence
```python
inter_trans = dt.inter_transliterate(input_type = "sen", from_convention = "hk",
                               to_convention = "velthuis", sentence = "nArAyaNaM")
```

inter transliteration of a text file.
```python
dt.inter_transliterate(input_type = "file", from_convention = "itrans",to_convention = "iast",
                      inp_file_path = "path_to_inp_file",op_file_path = "path_to_out_file")
 ```



## Installation
_ _ _ _
`pip install devatrans`

## How to use?
_ _ _ _ _
```python
transliterate(input_type, to_convention, inp_file_path=None,
                      op_file_path=None,  sentence=None)
 ```

 >The  `input_type` can  either  be  "sen"  or  "file",  if  the  `input_type`  is file  then
 >`inp_file_path`  should  be  provided, the `op_file_path` is optional,
 >` if not specified the  transliterated text is  written  back  to  `inp_file_path`.
 >
 > Use  this  method  to  transliterate text  from `SANSKRIT` to `IAST`, `ITRANS`, `HARVARD-KYOTO`, `VELHTUIS`.
 >
 > If  characters  which  are  not  part  of  the  convention  are  encoutered  they  are   left  unchanged.

 ```python
 inter_transliterate(input_type, from_convention, to_convention, inp_file_path=None,
                            op_file_path=None,  sentence=None)
 ```

 > The  `input_type` can  either  be  "sen"  or  "file",  if  the  `input_type`  is file  then
 > `inp_file_path`  should   be   provided,  the  `op_file_path` is optional,
 > ` if not specified the  transliterated text is  written  back  to  `inp_file_path`.
 >
 > Use  this  method to transliterate text  from one convetion to another.
 >
 > If characters which are not part of the convention are encoutered they are  left  unchanged.

 ```python
 back_transliterate(input_type, from_convention, inp_file_path=None,
                           op_file_path=None,  sentence=None):
 ```
 >The  `input_type` can  either  be  "sen"  or  "file",  if  the  `input_type`  is file  then
 >`inp_file_path`  should  be  provided, the `op_file_path` is optional,
 >` if not specified the  transliterated text is  written  back  to  `inp_file_path`.
 >
 > Use  this  method  to  back transliterate text  from  `IAST`, `ITRANS`, `HARVARD-KYOTO`, `VELHTUIS` to `SANSKRIT`.
 >
 > If  characters  which  are  not  part  of  the  convention  are  encoutered  they  are   left  unchanged.


 **`to_convention`, `from_convnetion` can take only take values `hk`, `iast`, `itrans`, `velthuis`**

 ## Contribute
 _ _ _ _ _ _
 * Currently only `.txt` format is supported, it could be extended to PDF and other file formats.
 * Other conventions like Sanskrit Library Phonetic Basic (SLP1), WX notation could be included.

 # Reference
 _ _ _ _
 TY  - BOOK
AU  - Nair, Jayashree
AU  - Sadasivan, Anand
PY  - 2019/03/30
SP  -
T1  - A Roman to Devanagari Back-Transliteration Algorithm based on Harvard-Kyoto Convention
ER  -

## Issue
_ _ _ _ _
If a bug encountered please open the issuse [here](https://github.com/RaviTeja51/devatrans/issues).\
My mail ravitejtasubilli@gmail.com
