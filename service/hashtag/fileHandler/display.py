class Result:

    def parse(self, top_results, count_dict, dataset):
        """Parses the results into the right format

        Args:
        top_results (int): The number of results to be displayed
        count_dict (Dictionary): The dictionary which maps words to count
        dataset (Dataset {object}): The file's dataset object

        Returns:
            Results as a list of objects

        """
        results = []
        # Don't exceed count_dict index
        total = top_results if len(count_dict) > top_results else len(count_dict)
        for i in range(0, total):
            word = count_dict[i][0]
            results.append({
                'word': word,
                'documents': dataset.get_documents(word),
                'sentences': dataset.get_sentences(word)
            })
        return results


