# Hastag Creator

This application was built to solve a specific challenge.


# Challenge

In the attached documents, find the most common occurring words, and the sentences where they are used to create the following table:

| Word(#)         | Documents                   | Sentences containing the word              
| ------------- | ----------------------- | ----------------------- |
| philosophy    | x, y, z | I don't have time for **philosophy**<br>Surely this was a touch of fine **philosophy**; though no doubt he had never heard there was such a thing as that.<br>Still, her pay-as-you-go **philosophy** implied she didn't take money for granted. |


## Requirements
    
- Python 3.7
- Java 7+


## Technologies

 - Python 3.7
 - Spacy for NLP
 - Tika for document parsing
 
## Constraints

 - This app uses Apache Tika for document parsing. Whilst the number of files that are supported is massive, it is not exhaustive.

## Installation

    git clone https://github.com/khlling/HastagCreator.git
    cd HashtagCreator
    virtualenv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Run

    venv/bin/python HashtagCreator.py
    
# Store venv

    pip3 freeze -l > requirements.txt 

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
|---|---|
| 3 | "apple" |
| 2 | "pear" |

#Design Considerations

#Improvements
### Binary Tree
One area of improvement that I would like to implement would be to make the count dictionary a binary tree.

Changed a node, using pointer implementation it would have been O(1) and sorting would have be O(nlogn). but sorting right at the end would have been O(n).

Not sorting at all would require a hashmap so again O(n). Accessing would be O(n) for hash but O(1) for tree.

A Tree also has more options - like if you wanted to extend the solution to become an api it'd be self-contained?

### Indexing Files
Instead of handling a flat folder structure I would like to index folders and sub-folders to ingest a folder structure.