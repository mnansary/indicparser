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


* extracting grapheme root, consonant diacritics and vowel diacritics

```python
comps=gp.process(text,return_graphemes=False)
print("Components:",comps)
```
> Components: [' ', ' ', 'শ', 'া', 'ট', 'ি', 'ক', 'া', 'প', ' ', ' ', ' ', 'ম', 'া', 'র']

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
> dict_keys(['bangla', 'malyalam', 'tamil', 'gujrati', 'panjabi', 'odiya', 'hindi'])

* malformed text detection examples
```python
gp.process("পাশ্র্বের")
```
> Malformed text-পাশ্র্বের possible text:পার্শ্বের

```python
gp=graphemeParser("panjabi")
gp.process("ਕੋਲਡਡਿੰ੍ਰਕਸ")
```

> Malformed text-ਕੋਲਡਡਿੰ੍ਰਕਸ possible text:ਕੋਲਡਡਿ੍ਰੰਕਸ

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