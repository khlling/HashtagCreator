from ..fileHandler import display, struct, ingest


class generator:

    def generate(self, root_folder_path, top_results, model):
        """Generates the dataset and hashtags with the passed in args
        Args:
        root_folder_path (str): The root folder on which we want to create the dataset from
        top_results (int): The number of results to return
        model (str): The NLP model we want to use - in this case only en_core_web_sm, but more can be manually added

        Returns:
            The results as a list with objects inside

        """
        try:
            # NLP Model can be change here, including language - Spacy offers a number of options
            # Language pack or model can be changed on the fly through REST request
            file_loader = ingest.FileLoader(root_folder_path, ingest.NLP(model))
        except Exception as e:
            print('Error getting to the files: ', e)

        # Create a datset model for results to be stored
        dataset = struct.Dataset()
        try:
            sorted_count_dict = file_loader.load(dataset)
        except FileNotFoundError:
            return 'File not found'
        return display.Result().parse(top_results, sorted_count_dict, dataset)
