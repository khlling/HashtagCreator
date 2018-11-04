from tabulate import tabulate


class Grid:
    _table = []

    def create(self, top_results, count_dict, dataset):
        headers = ["Word(#)", "Documents", "number"]

        for i in range(0, top_results):
            word = count_dict[i][0]
            self._table.append([word, dataset.get_documents(word), dataset.get_sentences(word)])

        print(tabulate(self._table, headers, tablefmt="fancy_grid"))
