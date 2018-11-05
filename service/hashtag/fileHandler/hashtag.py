from ..fileHandler import display, struct, ingest


class Generator:

    def __init__(self):
        # Create a datset model for results to be stored
        self._dataset = struct.Dataset()

    def generate(self, root_folder_path, top_results, model):
        """Generates the dataset and hashtags with the passed in args
        Args:
        root_folder_path (str): The root folder on which we want to create the dataset from
        top_results (int): The number of results to return
        model (str): The NLP model we want to use - in this case only en_core_web_sm, but more can be manually addedc

        Returns:
            The results as a list with objects inside

        """
        try:
            # NLP Model can be change here, including language - Spacy offers a number of options
            # Language pack or model can be changed on the fly through REST request
            file_loader = ingest.FileLoader(root_folder_path, ingest.NLP(model))
            sorted_count_dict = file_loader.load(self._dataset)
        except FileNotFoundError:
            return 'File not found'
        return display.Result().parse(top_results, sorted_count_dict, self._dataset)
