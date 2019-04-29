def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, but got {1}".format(expected, actual)
 
def test_not_equal(a, e):
    assert a != e, "Did not expect {0} but got {1}".format(a, e)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)
    
test_are_equal(number_of_evens([1,2,3,4,5]), 2)