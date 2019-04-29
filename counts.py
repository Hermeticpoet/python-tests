# def count_upper_case(message):
#     count = 0
#     for c in message:
#         if c.isupper():
#             count += 1
#         return count
        
# def count_upper_case(message):
#     return sum([1 for c in message if c.isupper()])
        
# assert count_upper_case(" ") == 0, "Empty String"
# assert count_upper_case("A") == 1, "One Upper Case"
# assert count_upper_case("a") == 0, "One Lower Case"
# assert count_upper_case("&*^%$doesitwork") == 0, "Special Characters"
# assert count_upper_case("nothing uppercase in here") == 0, "No uppercase letters"
# assert count_upper_case("BIG deal with 3 uppercase letters") == 3, "Three Uppercase letters"

# print("All the tests passed")

def even_number_of_evens(numbers):
    return False

assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")