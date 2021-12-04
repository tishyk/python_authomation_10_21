from lesson_12.examples.entry_point.module_1 import custom_sum  # correct import for entry point
# from .module_1 import custom_sum  # error on import level since we con't know where is root to be able use path to feed it from root for python


if __name__ == "__main__":
    print(f"NAME OF MODULE: {__name__}")
    print(custom_sum(5, 5))
