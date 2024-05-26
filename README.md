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

* **Cite our work**
```bibtext
@inproceedings{ansary-etal-2024-unicode-normalization,
    title = "{U}nicode Normalization and Grapheme Parsing of {I}ndic Languages",
    author = "Ansary, Nazmuddoha  and
      Adib, Quazi Adibur Rahman  and
      Reasat, Tahsin  and
      Sushmit, Asif Shahriyar  and
      Humayun, Ahmed Imtiaz  and
      Mehnaz, Sazia  and
      Fatema, Kanij  and
      Rashid, Mohammad Mamun Or  and
      Sadeque, Farig",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1479",
    pages = "17019--17030",
    abstract = "Writing systems of Indic languages have orthographic syllables, also known as complex graphemes, as unique horizontal units. A prominent feature of these languages is these complex grapheme units that comprise consonants/consonant conjuncts, vowel diacritics, and consonant diacritics, which, together make a unique Language. Unicode-based writing schemes of these languages often disregard this feature of these languages and encode words as linear sequences of Unicode characters using an intricate scheme of connector characters and font interpreters. Due to this way of using a few dozen Unicode glyphs to write thousands of different unique glyphs (complex graphemes), there are serious ambiguities that lead to malformed words. In this paper, we are proposing two libraries: i) a normalizer for normalizing inconsistencies caused by a Unicode-based encoding scheme for Indic languages and ii) a grapheme parser for Abugida text. It deconstructs words into visually distinct orthographic syllables or complex graphemes and their constituents. Our proposed normalizer is a more efficient and effective tool than the previously used IndicNLP normalizer. Moreover, our parser and normalizer are also suitable tools for general Abugida text processing as they performed well in our robust word-based and NLP experiments. We report the pipeline for the scripts of 7 languages in this work and develop the framework for the integration of more scripts.",
}
```
