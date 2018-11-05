from ..fileHandler import display, struct, ingest
import json


# if __name__ == '__main__':
class generator:

    def generate(self, root_folder_path, top_results):
        # NLP Model can be change here, including language - Spacy offers a number of options
        try:
            file_loader = ingest.FileLoader(root_folder_path, ingest.NLP('en_core_web_sm'))
        except Exception as e:
            print('Error getting to the files: ', e)

        # Create a datset model for results to be stored
        dataset = struct.Dataset()
        try:
            sorted_count_dict = file_loader.load(dataset)
        except FileNotFoundError:
            return 'File not found'
        return display.Result().get(top_results, sorted_count_dict, dataset)
