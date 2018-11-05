class Token:

    def __init__(self, file, sent):
        self._file = file
        self._sent = sent

    @property
    def file(self):
        return self._file

    @property
    def sent(self):
        return self._sent


class Dataset:

    def __init__(self):
        # Create a datset model for results to be stored
        self._token_dict = {}
        self._count_dict = {}

    def store(self, word, file_name, sent):
        """Stores the passed in token, if it's already been seen then append to record. Otherwise create a new entry

        Args:
        token (str): The files content.
        file_name (str): The fileHandler name.
        sent (Model): The sentence it was found.

        """
        if word not in self._token_dict:
            # Create token dictionary item
            self._token_dict[word] = [Token(file_name, sent.text)]
            self._count_dict[word] = 1
        else:
            # Add item to token dictionary
            self._token_dict[word].append(Token(file_name, sent.text))
            self._count_dict[word] += 1

    def get_sentences(self, word):
        """Get the sentences that a word was found in across dataset

        Args:
        word (str): The word that is being searched upon.

        Returns:
        A flattened list of sentences the word was found in.
        """
        sentences = []
        for token in self._token_dict[word]:
            if token.sent not in sentences:
                sentences.append(token.sent)
        return sentences

    def get_documents(self, word):
        """Get the documents that a word was found in across dataset

        Args:
        word (str): The word that is being searched upon.

        Returns:
        A flattened list of document names the word was found in.

        """
        documents = []
        for token in self._token_dict[word]:
            if token.file not in documents:
                documents.append(token.file)
        return documents

    @property
    def count_dict(self):
        return self._count_dict
