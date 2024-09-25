# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.
# take in list
def report_long_words(word_list):
  words_ten_plus = get_only_ten_plus(word_list)
  hyphen_filter = get_only_fullwords(words_ten_plus)
  morethan_fifteen = cut_add_ellip(hyphen_filter)
  return list_to_string(morethan_fifteen)

# if the word is NOT larger than 10, get rid
def get_only_ten_plus(word_list):
  return [word for word in word_list if len(word) >= 10]

# if the word contains hyphen(-) do NOT add to the list
def get_only_fullwords(word_list):
  return [word for word in word_list if "-" not in word]

# if the word is longer than 15, cut to 15 and add ellipsis(...)
def cut_add_ellip(word_list):
  for i in range(len(word_list)):  # Iterate over indices
      if len(word_list[i]) > 15:
          word_list[i] = word_list[i][:15] + "..."
  return word_list

# MAP, Turn list into to string/sentance with commas
def list_to_string(word_list):
  output_string = "These words are quite long: " 
  word_string = ', '.join([str(word) for word in word_list])
  return output_string + word_string
  
#
# My tests
#

print("")
print("Function: get_only_ten_plus")
print(get_only_ten_plus(['hello', 'nonbiological', 'Kay', 'this-is-a-long-word', 'antidisestablishmentarianism']))

print("")
print("Function: get_only_fullwords")
print(get_only_fullwords(['hello', 'nonbiological', 'Kay', 'this-is-a-long-word', 'antidisestablishmentarianism']))

print("")
print("Function: cut_add_ellip")
print(cut_add_ellip(['hello', 'nonbiological', 'Kay', 'this-is-a-long-word', 'antidisestablishmentarianism']))

print("")
print("Function: list_to_string")
print(list_to_string(['hello', 'nonbiological', 'Kay', 'this-is-a-long-word', 'antidisestablishmentarianism']))

#
# Pre-written tests
#

print("")
print("Function: report_long_words")

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py