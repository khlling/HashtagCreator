import fnmatch
import Models
import os
import spacy


class FileLoader:

    def __init__(self, root_file_path, nlp):
        self.root_file_path = root_file_path
        self.nlp = nlp

    def load(self):
        """Loads in each file within the specified root_file_path

        Returns:
            The ingested dataset model

        """
        # create a datset model for results to be stored
        dataset = Models.Dataset()
        for file_name in os.listdir(self.root_file_path):
            print('Ingesting: ', file_name)
            # Find all files matching .txt
            if fnmatch.fnmatch(file_name, '*.txt'):
                path = self.root_file_path + "/" + file_name
                f = open(path, "r")
                # Check that the file can be read
                if f.mode == "r":
                    self.nlp.load(f.read(), file_name, dataset)
        return dataset


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

    # Extract and store tokens
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

