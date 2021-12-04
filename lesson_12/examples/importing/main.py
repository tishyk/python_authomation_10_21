# from lesson_12.examples.importing.ariphmetic import main as ariphmetic  # bad example with iport all module
# from lesson_12.examples.importing.logical import main as logical  # bad example with import all module
# import lesson_12.examples.importing.ariphmetic.main as main  # bad example with import all module
from lesson_12.examples.importing.ariphmetic.main import custom_sum  # good example with import only function from module


# print(ariphmetic.cusom_sum(5, 5))
# print(logical.is_greater(5, 6))

# main.custom_sum()