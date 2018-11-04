# Hastag Creator

This application was built to solve a specific challenge.


# Challenge

In the attached documents, find the most common occurring words, and the sentences where they are used to create the following table:

| Word(#)         | Documents                   | Sentences containing the word              
| ------------- | ----------------------- | ----------------------- |
| philosophy    | x, y, z | I don't have time for **philosophy**<br>Surely this was a touch of fine **philosophy**; though no doubt he had never heard there was such a thing as that.<br>Still, her pay-as-you-go **philosophy** implied she didn't take money for granted. |


## Technologies

 - Python 3.7
 - Spacy for NLP

## Installation

    git clone
    cd HashtagCreator
    virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

# Run

    venv/bin/python HashtagCreator.py
    
# Store venv

    pip freeze > requirements.txt

# Structures

## Structure 1: Sentences


+--------------------------------------+
|                ARRAY                 |
+--------------------------------------+
| "Something bad will happen."         |
| "I like apple flavour more."         |
| "Ughhh pear, why pear?"              |
| "No apple I guess."                  |
| "Well that sucks."                   |
| "Tell me about it, I miss my apple." |
+--------------------------------------+


=======================================
Structure 2: Locations of words        
=======================================

+----------------------------------------------+
|                 DICTIONARY                   |
+---------------+------------------------------+
| WORD (string) | INSTANCES (array of tuples*) |
+---------------+------------------------------+
| "apple"       | [ (1, 2), (3, 1), (5, 7) ]   |
| "pear"        | [ (2, 1), (2, 3) ]           |
| ...           | ...                          |
+---------------+------------------------------+

* Of the form (sentence index, position in sentence). If position is irrelevant, you can use an array of numbers instead & optionally remove duplicates.


## Structure 3: Storing word counts

|Count (int)| WORD (string)  |
|--|--|
| 3 | "apple" |
| 2 | "pear" |

