from lab03 import int_division, get_even_ints, count_vowels, remove_seq, reverse_str

def test_int_divison():
    assert int_division(0, 3) == 0
    assert int_division(6, 2) == 3
    assert int_division(32, 4) == 8
    assert int_division(45, 5) == 9
    assert int_division(15, 7) == 2

def test_get_even_ints():
    assert get_even_ints([1,2,3,4,5]) == [2,4]
    assert get_even_ints([1,5,9]) == []
    assert get_even_ints([2,4,6]) == [2,4,6]
    assert get_even_ints([]) == []
    assert get_even_ints([1,2,3,4,5,6,7,8,9,10]) == [2, 4, 6, 8, 10]

def test_count_vowels():
    assert count_vowels("Hello, People!") == 5
    assert count_vowels("") == 0
    assert count_vowels("Is This A String")  == 4
    assert count_vowels("AEIOUaeiou") == 10
    assert count_vowels ("AHifehufiAUIs") == 8

def test_reverse_string(): 
    assert reverse_str("") == ""
    assert reverse_str("s") == "s"
    assert reverse_str("firefighter") == "rethgiferif"
    assert reverse_str("racecar") == "racecar"
    assert reverse_str("CMPSC9") == "9CSPMC"

def test_remove_seq(): 
    assert remove_seq("ababcc", "abc") == "abc" 
    assert remove_seq("apple", "ap") == "ple"
    assert remove_seq("banana", "na") == "ba"
    assert remove_seq("ssss" , "s") == ""
    assert remove_seq("asdfg", "hjk") == "asdfg"
                    