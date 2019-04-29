def number_of_evens(numbers):
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
    return evens

def test_are_equal(actual, expected):
    """
    Test that two values are equal. Raises AssertionError if both values are
    not equal.
    `actual` is the actual value produced
    `expected` is the value that was supposed to be produced
    """
    assert expected == actual, "Expected {0}, but got {1}".format(expected, actual)
 
def test_not_equal(a, e):
    """
    Test that two values are not equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert a != e, "Did not expect {0} but got {1}".format(a, e)
    
def test_is_in(collection, item):
    """
    Check to ensure that a given collection contains a given value. Raises
    AssertionError if `item` is not in `collection`
    `collection` is the collection to be tested
    `item` is the item that is being searched for
    """
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

# Collection of Colors:
colors = {"yellow", "green", "blue", "purple", "orange"}
   
test_are_equal(number_of_evens([1,2,3,4,5]), 2)
test_are_equal(0,0)
test_not_equal(number_of_evens([2,4,5,8]), 4)
test_not_equal(number_of_evens([1,6,8,9,20,21]), 5)
test_not_equal(2,3)
test_is_in(colors, "purple")
test_is_in(colors, "green")
test_is_in(colors, "orange")
test_not_in(colors, "white")
test_not_in(colors, "brown")
