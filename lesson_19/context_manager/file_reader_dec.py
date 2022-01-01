from contextlib import contextmanager


@contextmanager
def read_file(path: str) -> str:
    file = open(path)

    return file.read()
