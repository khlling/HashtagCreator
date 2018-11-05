# Hashtag Creator

This application was built to solve a specific challenge.


# Challenge

In the attached documents, find the most common occurring words, and the sentences where they are used to create the following table:

| Word(#)         | Documents                   | Sentences containing the word              
| ------------- | ----------------------- | ----------------------- |
| philosophy    | x, y, z | I don't have time for **philosophy**<br>Surely this was a touch of fine **philosophy**; though no doubt he had never heard there was such a thing as that.<br>Still, her pay-as-you-go **philosophy** implied she didn't take money for granted. |


## Requirements
    
- Python 3.7 (Windows - Microsoft Visual C++ 14.0 also)
- Java 7+
- virtualenv

## Technologies

 - Python 3.7
 - Spacy for NLP
 - Tika for document parsing
 - Django for web framework

## Installation

    git clone https://github.com/khlling/HastagCreator.git
    cd HashtagCreator
Linux

    virtualenv .venv && source .venv/bin/activate && pip install -r requirements.txt

Windows

    virtualenv .venv && source .venv\Scripts\activate && pip3 install -r requirements.txt

Additional Step (download a Spacy model called: "en_core_web_sm"). List of available models can be found here: https://spacy.io/models/

    python -m spacy download en_core_web_sm

## Start Server

    cd HashtagCreator/service
    python manage.py runserver 
    
## Make Requests

    Make a POST request to http://127.0.0.1:8000/hashtag/ (I suggest using Postman)
    with a JSON object in the body i.e.
    {
        "filePath": "/Users/Kevin/PycharmProjects/Test/myTestDocs",
        "noResults": 50,
        "model": "en_core_web_sm"
    }
## Results
    In the form of JSON
    [
        {
        	"word": "pear",
        	"documents": [ "doc1.txt", "doc2.txt"]
        	"sentences": [ "I like pears", "He likes pears"]
	    },
	    {
        	"word": "apple",
        	"documents": [ "doc1.txt"]
        	"sentences": [ "I like apples"]
	    }
	]
# Store venv

    pip3 freeze -l > requirements.txt 

# Structures
## Structure 1: Storing instances
| Word (string)         | Instances (Token {object}) |             
| ------------- | ----------------------- |
| "apple"     | [ {file1, sentence1 }, {file2, sentence1 }]  |
| "pear"        | [ {file2, sentence1 }]   |
| ...           | ...                          |


* Of the form (sentence index, position in sentence). If position is irrelevant, you can use an array of numbers instead & optionally remove duplicates.


## Structure 2: Storing word counts

|Count (int)| WORD (string)  |
|---|---|
| 2 | "apple" |
| 1 | "pear" |
| ...| ...|


## Design Decisions
As part of building a reusable solution that can be extended to other documents and text sources. I have made a number of design descions:

- Implement a web service. This allows any system that can make a REST request to interface with this service.
- Use of Tika means that a lot more content sources can be ingested.
- Results are not in table format but rather in JSON format so that it can be processed by other systems.
- I have chosen not to store results as this service is meant to be used as a micro-service, albeit not that micro (see scaling section)
- I toiled with applying lemmatisation. Spacy is capable of apply lemmatisation. Lemmatisation is the algorithmic process of determining the lemma of a word based on its intended meaning. This may help to improve results, at the moment 's and n't are returned as separate words instead of being part of John's or doesn't. These abbreviated words are still part of the sentence but they go towards a separate word count. However I decided not apply this as it might get confusing trying to find the corresponding word in the list of sentences once lemmatisation has occurred.

## Constraints

 - This app uses Apache Tika for document parsing. Whilst the number of files that are supported is massive, it is not exhaustive. (For more https://tika.apache.org)

## Improvements
### Binary Tree
One area of improvement that I would like to implement would be to make the count dictionary a binary search tree.

Changing a node, using pointer implementation where the instance dictionary stored the pointer to the binary search tree node would have been O(1) and sorting would have be O(nlogn). But sorting the binary search tree right at the end would have been O(n).Not sorting at all would require a dictionary so again O(n). Accessing would be O(n) for hash but O(1) for tree.

A Tree also has more options for example you wanted to extend the solution to be a live query.

### Indexing Files
Instead of handling a flat folder structure an improvement could be to index folders and sub-folders to ingest a whole folder structure. This should be done by modifying the ingest.Fileloader.load() function.

### Scaling
Although the application is reasonably quick for small numbers of files it does not scale well. For higher throughput of files and requests.

I would ideally not put the Apache Tika and Spacy libraries in service application. Indeed the python library Apache Tika is a wrapper for a Java web server running Tika. Instead I would split them apart into their own micro-services with an orchestration layer to manage RESTful calls and load. Therefore the application could be scaled horizontally much more effectively. But I have done so that it's easier to run and test the application in development mode.