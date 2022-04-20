"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    assert new_place.name == "Malagar"
    print(new_place.name)
    assert new_place.country == "Spain"
    print(new_place.country)
    assert new_place.priority == 1
    print(new_place.priority)
    assert not new_place.is_visited
    print(new_place.is_visited)

    # Test toggle visited status
    print("Test Toggle visited Status:")
    new_place.toggle_visited_status()
    print(new_place)
    assert new_place.is_visited
    print(new_place.is_visited)

    #Test important place
    print("Test important place:")
    new_place.is_important_place()
    print(new_place)
    assert new_place.is_important_place()


run_tests()
