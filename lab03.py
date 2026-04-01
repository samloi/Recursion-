def int_division(num, div):
    if (num - div) < 0:
        return 0
    return 1 + int_division(num - div, div)

def get_even_ints(int_list):
    if int_list == []:
        return []
    else: 
        if int_list [0] % 2 == 0:
            first_element = [int_list[0]]
            remaining_even_ints = get_even_ints(int_list[1:])
            return first_element + remaining_even_ints
        else: 
            return get_even_ints(int_list[1:])
        

def count_vowels(text):
    if text == "": 
        return 0
    if text[0].lower() in 'aeiou':
        vowel_countnow = 1
        leftover_vowel = count_vowels(text[1:])
        total_vowels = vowel_countnow + leftover_vowel
        return total_vowels
    else: 
        return count_vowels(text[1:])


def reverse_str(text):
    if not text: 
        return ""
    else: 
        reversed_rest = reverse_str(text[1:])
        reversed_text = reversed_rest + text[0]
        return reversed_text
    
def remove_seq(text, seq):
    if text == "":
        return ""
    if text.startswith(seq):
        return remove_seq(text[len(seq):],seq)
    else: 
        first_character = text[0]
        remaining_seq = remove_seq(text[1:],seq)
        return first_character + remaining_seq


