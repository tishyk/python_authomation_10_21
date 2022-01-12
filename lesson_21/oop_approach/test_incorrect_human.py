# """Incorrect bad example since single state for all tests"""
# from copy import deepcopy
#
# from lesson_21.human import Human
#
#
# class TestHumanSuite:
#     def setup_class(self):
#         self.human = Human("John", 23, "male")
#
#     def setup(self):
#         print("Setup was called")
#
#
#     def test_check_name_property_return_value(self):
#         assert self.human.name == "John"
#
#     def test_check_age_after_grow(self):
#         self.human.grow()
#         assert self.human._Human__age == 24
#
#     def test_check_age_property_return_value(self):
#         assert self.human.age == 23
#
#     def test_check_gender_property_return_value(self):
#         assert self.human.gender == "male"
#
#
#     def teardown(self):
#         print("Teardown was called")
#
#     def teardown_class(self):
#         print("class teardown was called")
