def test_check_return_value_for_name_property(john_asiat):
    assert john_asiat.name == "John"


def test_check_return_value_for_age_property(john_negro):
    assert john_negro.age == 23


def test_check_return_value_for_gender_property(john_asiat):
    assert john_asiat.gender == "male"
