import re

def adds_to_ten(a_string):
  for number in range(0, len(a_string)):
    letter = a_string[number]
    try:
      number = int(letter)

    except:
      print(a_string[number:number+3:1], number, a_string[number-1], letter*3)
      print(a_string[number:number+3:1] == letter*3 and a_string[number+4] != letter and a_string[number-1] != letter)

def find_3_letters_between(a_string):
  for number in range(0, len(a_string) - 4):
    letter = a_string[number]
    matches = a_string[number:number+3:1] == letter*3 and a_string[number+4] == letter and a_string[number-1] != letter
    print(matches)


find_3_letters_between('ababaaab')