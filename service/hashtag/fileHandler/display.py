from tabulate import tabulate


class Result:

    def get(self, top_results, count_dict, dataset):
        table = []
        results = []
        # Don't exceed count_dict index
        total = top_results if len(count_dict) > top_results else len(count_dict)
        for i in range(0, total):
            word = count_dict[i][0]
            table.append([word, dataset.get_documents(word), dataset.get_sentences(word)])
            results.append({
                'word': word,
                'documents': dataset.get_documents(word),
                'sentences': dataset.get_sentences(word)
            })
        # self._grid(table)
        return results

    def _grid(self, table):
        headers = ["Word(#)", "Documents", "number"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))


