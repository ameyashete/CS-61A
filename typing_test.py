""" Typing Test implementation """

from utils import *
from ucb import main
# BEGIN Q1-5

#Q1


def lines_from_file(path):
    with open(path, "r") as x:
      text =  [strip(s, chars=None) for s in readlines(x)]
      return text

def new_sample(path, i):
    assert i >= 0 
    return lines_from_file(path)[i]

#Q2 

def analyze(sample_paragraph, typed_string, start_time, end_time):
    speed_and_accuracy = []
    def words_per_minute(typed_string):
        no_characters = len(typed_string) / 5
        seconds_characters = no_characters / (end_time - start_time)
        return seconds_characters * 60

    def accuracy_percentage(typed_string, sample_paragraph):
        i = 0 
        correct = 0 
        l_sample = split(sample_paragraph)
        l_typed = split(typed_string) 
        if l_typed == [] or l_sample == []:
            return 0.0
        while i < min(len(l_typed), len(l_sample)):
            if l_typed[i] == l_sample[i]:
                correct += 1
            i += 1
        return correct / (min(len(l_typed), len(l_sample))) * 100    

    speed_and_accuracy.append(words_per_minute(typed_string))
    speed_and_accuracy.append(accuracy_percentage(typed_string, sample_paragraph))
    return speed_and_accuracy

# Q3

def pig_latin(string):
    list_sample = [string]
    vowels = ["a", "e", "i", "o", "u"]
    i = 0
    character = 0
    while i < len(list_sample):
        if list_sample[i][0] in vowels:
            return list_sample[i] + "way"
        elif list_sample[i][0] not in vowels:
            index_character = 0
            for character in list_sample[i]:
                index_character += 1
                if character in vowels:
                    return list_sample[i][index_character-1:] + list_sample[i][:index_character-1] + "ay"
        i += 1
    list_sample = string + "ay"
    return list_sample

# Q4 

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    elif user_input not in words_list:
        new_array = [(x, score_function(user_input, x)) for x in words_list]
        new_min = min(new_array, key=lambda y: y[1])
        return new_min[0]
# Q5 

def swap_score(string_1, string_2):
    if not string_1 or not string_2:
        return 0
    elif string_1 == string_2:
        return 0
    else:
        if string_1[0] != string_2[0]:
            return 1 + swap_score(string_1[1:], string_2[1:])
        elif string_1[0]  == string_2[0]:
            return swap_score(string_1[1:], string_2[1:])

#swap_score(string_1[i + 1:], string_2[i + 1:])

# This function should have a while loop for the min length of each string. For example, "thin" and
# "thinner" should only have the 4 letters from "thin". You must also use the recursion function from
# lab 05 which slices the word and checks for which of the words are the same. The lab 05 recursion 
# returns the string of characters that need to be added but we can just return the len(string_chars_to_add)





# END Q1-5

# Question 6



def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if not word1: # Fill in the condition
        # BEGIN Q6
        return len(word2)
        # END Q6
    elif not word2: # Feel free to remove or add additional cases
        # BEGIN Q6
        return len(word1)
        # END Q6
    elif word1[-1] == word2[-1]:
        change = 0 
    else:
        change = 1
    add_char = score_function(word1[:-1], word2) + 1
    substitute_char = score_function(word1[:-1], word2[:-1]) + change
    remove_char = score_function(word1, word2[:-1]) + 1

    min_result = min(add_char, substitute_char, remove_char)
    return min_result

# END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8

# Q7 
def score_function_accurate(word1, word2):
    if not word1: 
        return len(word2)
    elif not word2: 
        return len(word1)
    elif word1[-1] == word2[-1]:
        return score_function_accurate(word1[:-1], word2[:-1])
    else:
        add_char = score_function_accurate(word1[:-1], word2) + 1
        substitute_char = score_function_accurate(word1[:-1], word2[:-1]) + KEY_DISTANCES[word1[-1], word2[-1]]
        remove_char = score_function_accurate(word1, word2[:-1]) + 1
        min_result = min(add_char, substitute_char, remove_char)
    return min_result
# Q8
cache = {}
def score_function_final(word1, word2):
    search_pair = (word1, word2)
    rev_search_pair = (word2, word1)
    if search_pair in cache:
        return cache[search_pair]
    if rev_search_pair in cache:
        return cache[rev_search_pair]
    if not word1: 
        cache[search_pair] = len(word2)
        cache[rev_search_pair] = len(word2)
        return len(word2)
    elif not word2: 
        cache[search_pair] = len(word1)
        cache[rev_search_pair] = len(word1)
        return len(word1)
    elif word1[-1] == word2[-1]:
        recur_call = score_function_final(word1[:-1], word2[:-1])
        cache[word1[:-1], word2[:-1]] = recur_call
        cache[word2[:-1], word1[:-1]] = recur_call
        return recur_call
    else:
        add_char = score_function_final(word1[:-1], word2) + 1
        remove_char = score_function_final(word1, word2[:-1]) + 1
        substitute_char = score_function_final(word1[:-1], word2[:-1]) + KEY_DISTANCES[word1[-1], word2[-1]]

    min_result = min(add_char, substitute_char, remove_char)
    cache[search_pair] = min_result
    cache[rev_search_pair] = min_result
    return min_result

# END Q7-8























