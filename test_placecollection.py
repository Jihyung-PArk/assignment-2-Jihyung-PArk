"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place





def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    # TODO: Add more sorting tests
    # Test sorting places by name
    print("Test sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    # Test sorting places by country
    print("Test sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    # Test sorting places by visit
    print("Test sorting - visit:")
    place_collection.sort("is_visited")
    print(place_collection)



    # TODO: Test saving places (check CSV file manually to see results)
    # Test saving places
    print("Test saving places:")
    place_collection.save_places('places.csv')
    print(place_collection)
    assert place_collection.places

    # TODO: Add more tests, as appropriate, for each method
    # Test get number of unvisited places
    print("Test number of unvisited places:")
    place_collection.get_num_of_unvisited()
    assert place_collection.get_num_of_unvisited()


run_tests()
