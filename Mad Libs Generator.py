
# Mad Libs Generator

'''
A simple program to use strings and inputs.

1. take user in put for specific types of words (nouns, verbs, adverbs,)
2. add those inputs into a chosen string
3. return sentence to console
'''



# MAD LIB 1
ml_sentence1 = "\nAter hiding the painting in his {0} for two years, it became {1} and tried to sell it to a/an {2} in Florence, but was caught.\n"
ml_sentence1_dict = {"noun1" : " ", "adjective1" : " ", "noun2" : " "}


# user input
ml_sentence1_dict['noun1'] = input("\nPlease enter a noun: ").lower()
ml_sentence1_dict['adjective1'] = input("Please enter an adjective: ").lower()
ml_sentence1_dict['noun2'] = input("Please enter another noun: ").lower()

print(ml_sentence1.format(ml_sentence1_dict['noun1'], ml_sentence1_dict['adjective1'], ml_sentence1_dict['noun2']))


# MAD LIB 2

ml_sentence2 = "\nHello, my name is Astronaut {0}. I am on my way to Planet {1}.\nI will be gone for {2} days. I am very {3} about the trip but I will miss my {4}."
ml_sentence2part2 = "\nI have heard that the atmosphere there is {0}. Luckily, my {1} packed me a jacket to keep me {2}."
ml_sentence2part3 = "\nWhen I land on the planet, I will {0} for joy. I am {1} to walk on another planet.I could not be more {2} for this trip!\n"
ml_sentence2_dict = {"name1" : " ", "sillyword1" : " ", "number1" : " ", "adjective1" : " ", "noun2" : " ", "adjective2" : " ", "relative1" : " ", "adjective3" : " ", "verb1" : " ", "adjective4" : " ", "adjective5" : " "}


# user input
print ("There are 11 words to enter.")
ml_sentence2_dict['name1'] = input("\nPlease enter a name: ").title()
ml_sentence2_dict['sillyword1'] = input("Please enter a silly word: ").title()
ml_sentence2_dict['number1'] = input("Please enter a number: ").lower()
ml_sentence2_dict['adjective1'] = input("Please enter an adjective: ").lower()
ml_sentence2_dict['noun2'] = input("Please enter noun: ").lower()
ml_sentence2_dict['adjective2'] = input("Please enter another adjective: ").lower()
ml_sentence2_dict['relative1'] = input("Please enter a relative: ").lower()
ml_sentence2_dict['adjective3'] = input("Please enter another adjective: ").lower()
ml_sentence2_dict['verb1'] = input("Please enter a verb: ").lower()
ml_sentence2_dict['adjective4'] = input("Please enter another adjective: ").lower()
ml_sentence2_dict['adjective5'] = input("Please enter another adjective: ").lower()

print(ml_sentence2.format(ml_sentence2_dict['name1'], ml_sentence2_dict['sillyword1'], ml_sentence2_dict['number1'], ml_sentence2_dict['adjective1'], ml_sentence2_dict['noun2']))
print(ml_sentence2part2.format(ml_sentence2_dict['adjective2'], ml_sentence2_dict['relative1'], ml_sentence2_dict['adjective3']))
print(ml_sentence2part3.format(ml_sentence2_dict['verb1'], ml_sentence2_dict['adjective4'], ml_sentence2_dict['adjective5']))
