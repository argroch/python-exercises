# Needed a place to work out Code Academy exercises, outside of their environment.

# def anti_vowel(text):
#   result = ''
#   vowels = ['a','e','i','o','u']
#   for char in text:
#     if char.lower() not in vowels:
#       result += char
#   return result
#
# print anti_vowel("Hey look Words!")

# def censor(text, word):
#   censored = ""
#   for char in word:
#     censored += "*"
#   lst = text.split()
#   for index,item in enumerate(lst):
#     if item == word:
#       lst[index] = censored
#   return ' '.join(lst)
#
# print censor("this hack is a wack hack", "hack")

# def count(sequence, item):
#   total = 0
#   if type(item) is list:
#     for x in sequence:
#       if x in item:
#         total += 1
#   else:
#     if type(item) is str:
#       item = float(item)
#     for x in sequence:
#       if x == item:
#         total += 1
#   return total
#
# print count([2,2,2,2,5,3,2,3],[2,3])

# def remove_duplicates(lst):
#   clean_list = []
#   lst.sort()
#   for index,x in enumerate(lst):
#     if index < len(lst)-1:
#       if x != lst[index+1]:
#         clean_list.append(x)
#     else:
#         clean_list.append(x)
#   return clean_list
#
# print remove_duplicates([1,2,39,4,43,3,2,5,5,3,4,6,33,33,200,200])

def median(lst):
  lst.sort()
  if len(lst)%2 == 0:
    x = float(lst[len(lst)/2 - 1])
    y = lst[len(lst)/2]
    return (x+y)/2
  else:
    return lst[(len(lst)-1)/2]

print median([11,8,17,2,3,19])
