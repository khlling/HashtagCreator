import Ingest
import Display
import Models

if __name__ == '__main__':
    # The number of results displayed can be changed here
    top_results = 5
    # NLP Model can be change here, including language - Spacy offers a number of options
    file_loader = Ingest.FileLoader('./test docs', Ingest.NLP('en_core_web_sm'))
    # Create a datset model for results to be stored
    dataset = Models.Dataset()
    sorted_count_dict = file_loader.load(dataset)
    Display.Grid().create(top_results, sorted_count_dict, dataset)
