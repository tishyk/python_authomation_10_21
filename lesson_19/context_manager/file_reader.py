class FileReader:
    def __init__(self, file_name: str, mode: str = None) -> None:
        self.__file_name = file_name
        self.__mode = mode if mode else "r"
        self.__io_wrapper = None

    def read(self) -> str:
        return self.__io_wrapper.read()

    def __enter__(self):
        self.__io_wrapper = open(self.__file_name, self.__mode)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.__io_wrapper.close()


if __name__ == "__main__":
    with FileReader("lesson_20/context_manager/text.txt") as file:
        print(file.read())
