class ReadFile:
    def __init__(
        self,
        filename_path: str,
    ):
        self.filename_path = filename_path
        with open(filename_path, "r") as reader:
            print(reader.read())
