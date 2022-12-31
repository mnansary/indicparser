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
@inproceedings{alam2021large,
  title={A large multi-target dataset of common bengali handwritten graphemes},
  author={Alam, Samiul and Reasat, Tahsin and Sushmit, Asif Shahriyar and Siddique, Sadi Mohammad and Rahman, Fuad and Hasan, Mahady and Humayun, Ahmed Imtiaz},
  booktitle={International Conference on Document Analysis and Recognition},
  pages={383--398},
  year={2021},
  organization={Springer}
}
```