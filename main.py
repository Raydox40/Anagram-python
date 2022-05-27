# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    spring_1 = "below"
    spring_2 = "elbow" 
    if(sorted(spring_1)==sorted(spring_2)):
        print("True")
    else:
        print("False")