import Ingest
import Display

if __name__ == '__main__':
    # The number of results displayed can be changed here
    top_results = 5
    # NLP Model can be change here, including language - Spacy offers a number of options
    file_loader = Ingest.FileLoader('./test docs', Ingest.NLP('en_core_web_sm'))
    dataset = file_loader.load()
    sorted_count_dict = sorted(dataset.count_dict.items(), key=lambda kv: kv[1], reverse=True)
    Display.Grid().create(top_results, sorted_count_dict, dataset)

