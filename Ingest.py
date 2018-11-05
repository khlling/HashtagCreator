import os
import spacy
import sys
import tika
from tika import parser


class FileLoader:

    def __init__(self, root_file_path, nlp):
        self.root_file_path = root_file_path
        self.nlp = nlp
        tika.initVM()

    def load(self, dataset):
        """Loads in each file within the specified root_file_path

        Returns:
            Sorted list of the count dictionary

        """
        for file_name in os.listdir(self.root_file_path):
            path = self.root_file_path + "/" + file_name
            print('path: ', path)
            content = self._extract_content(path)
            # Only process further if there is content
            if content:
                self.nlp.load(content, file_name, dataset)
        return sorted(dataset.count_dict.items(), key=lambda kv: kv[1], reverse=True)

    def _extract_content(self, file_path):
        """Uses Tika to parse and extract content from file.

        Returns:
            content

        """
        try:
            parsed = parser.from_file(file_path)
            return parsed['content']
        except Exception as inst:
            print("Unexpected error:", inst)


class NLP:

    def __init__(self, model):
        self.nlp = spacy.load(model)

    def load(self, content, file_name, dataset):
        """Loads contents of the file into NLP module. If you want to load content from another source
        use this method

        Args:
        content (str): The files content.
        file_name (str): The file name.
        dataset (Model): The dataset that is being loaded.

        Returns:
        Sanitized token, if token does not meet rules then None is returned

        """
        doc = self.nlp(content)
        self._extract_tokens(doc.sents, file_name, dataset)

    def _extract_tokens(self, sents, file_name, dataset):
        """Extracts tokens from sentences

        Args:
        sents (str): The sentences.
        file_name (str): The file name.
        dataset (Model): The dataset that is being loaded.

        """
        for sent in sents:
            # pass sentence to be tokenized
            tokens = self.nlp(sent.text)
            for token in tokens:
                token = self._apply_rules(token)
                if token:
                    self._store_token(dataset, token, file_name, sent)

    def _apply_rules(self, token):
        """Apply rules to cleanup token

        Args:
        content (str): The files content.
        file_name (str): The file name.
        dataset (Model): The dataset that is being loaded.

        """
        if not (token.is_stop or token.is_punct):
            # Strip new line characters, remove punctation, stop words and lower case
            sanitized_token = token.text.rstrip().lower()
            return sanitized_token

    def _store_token(self, dataset, token, file_name, sent):
        """Stores token

        Args:
        dataset (Model): The dataset that is being loaded.
        token (str): The files content.
        file_name (str): The file name.
        sent (str): The sentence where the token was found.

        """
        dataset.store(token, file_name, sent)

