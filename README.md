# indicparser
Grapheme Parser for indic languages 

# Installaton

```python
pip install indicparser
```
# Useage
* initializing the parser

```python
from indicparser import graphemeParser
gp=graphemeParser("bangla")
```
* extracting graphemes

```python
text="  শাটিকাপ   মার"
graphemes=gp.process(text)
print("Graphemes:",graphemes)
```
> Graphemes: [' ', ' ', 'শা', 'টি', 'কা', 'প', ' ', ' ', ' ', 'মা', 'র']

* extracting graphemes but merging spaces and clearing initial and ending space
```python
graphemes=gp.process(text,merge_spaces=True)
print("Graphemes (space corrected):",graphemes)
```
> Graphemes (space corrected): ['শা', 'টি', 'কা', 'প', ' ', 'মা', 'র']

* treatment of numbers and puntucation and english is also available by default

```python
text="এটাকি 2441139 ? না ভাই wrong number"
graphemes=gp.process(text,merge_spaces=True)
print("Graphemes:",graphemes)
```
> Graphemes: ['এ', 'টা', 'কি', ' ', '2', '4', '4', '1', '1', '3', '9', ' ', '?', ' ', 'না', ' ', 'ভা', 'ই', ' ', 'w', 'r', 'o', 'n', 'g', ' ', 'n', 'u', 'm', 'b', 'e', 'r']

* available languages

```python
from indicparser import languages
languages.keys()
```
> dict_keys(['bangla', 'malyalam', 'tamil', 'gujrati', 'panjabi', 'odiya', 'hindi','nagri'])


# Normalization
* For best results use normalized text before parsing
* An example bangla unicode normalizer can be found [here](https://pypi.org/project/bnunicodenormalizer/)

# ABOUT
* Authors: [Bengali.AI](https://bengali.ai/)

* **Cite Bengali.AI multipurpose grapheme dataset paper**
```bibtext
@misc{ansary2023abugida,
      title={Abugida Normalizer and Parser for Unicode texts}, 
      author={Nazmuddoha Ansary and Quazi Adibur Rahman Adib and Tahsin Reasat and Sazia Mehnaz and Asif Shahriyar Sushmit and Ahmed Imtiaz Humayun and Mohammad Mamun Or Rashid and Farig Sadeque},
      year={2023},
      eprint={2306.01743},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
