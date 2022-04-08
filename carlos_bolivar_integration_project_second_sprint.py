#Carlos Bolivar
#This program is supposed to be a quiz
#No websites were used, and nobody helped me
#I consider every code is obvious
player_score = 0

print('HELLO,', end = ' ')
print('WELCOME TO THIS QUIZ\nLETS BEGIN\nGENERAL KNOW','LEDGE QUIZ', sep = '')
print('QUESTION 1')
first_question = input('What is the capital of United States?\n')
if first_question == 'washington' or first_question == 'Washington' or first_question == 'washington d.c.' or first_question == 'Washington D.C.':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 2')
second_question = input('How much is 23 + 15?\n')
if second_question == '38' or second_question != '37':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 3')
third_question = input('Is Venezuela located in America?\n')
if third_question == 'yes':
    print('Correct!')
    player_score += 1
elif third_question == 'Yes':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 4')
fourth_question = input('How much is 10 * 10\n')
if fourth_question == '100':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 5')
fifth_question = input('How many continents are there in the world?\n')
if fifth_question == '5' or fifth_question == 'five' or fifth_question == 'Five':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 6')
sixth_question = input('What is the result of 2**4?\n')
if sixth_question == '16':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 7')
seventh_question = input('Is Africa a country?\n')
if seventh_question == 'no' or seventh_question == 'No' or seventh_question == 'NO':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 8')
eight_question = input('How much is 520 - 225?\n')
if eight_question == '295':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 9')
nine_question = input('What language is spoken in Mexico?\n')
if nine_question == 'spanish' or nine_question == 'Spanish' and not nine_question == 'mexican':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 10')
ten_question = input('How much is 297 / 3?\n')
if ten_question == '99':
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 11')
eleven_question = int(input('Type a number higher than -1\n'))
if eleven_question >= 0:
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('QUESTION 12')
twelve_question = int(input('Type a number between 351,781 and 451,791\n'))
if twelve_question >= 351781 and twelve_question <= 451791:
    print('Correct!')
    player_score += 1
else:
    print('Incorrect')

print('\nCONGRATULATIONS! YOU HAVE FINISHED THE QUIZ.')
if player_score > 6:
    print("Well done! Final score: {} / 12".format(player_score))
else:
    print("You need to improve! Final score: {} / 10".format(player_score))

print("\nExtra numbers to meet requirements:")
print(17//4, 25%6, 'hello'*5)

for x in range(0,6):
    print('1,2,3,4,5')

x = 1
while x < 6:
    print(x)
    x += 1

#'**' is used to set an exponent to a number
#'*' is used for multiplication
#'/' is used for division
#'//' it rounds down to the nearest whole number
#'%' it returns the remainder of dividing the left hand operand by right hand operand
#'+' as numeric operator is used for addition
#'-' is used for substraction
#',' is used to set an space between strings
#'+' as string operator is used to join strings