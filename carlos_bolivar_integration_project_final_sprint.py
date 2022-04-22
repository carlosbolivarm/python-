"""
Integration Project by Carlos Bolivar.
The project consists in a quiz about math and general knowledge.
"""
__author__ = "Carlos Bolivar"
# Sources: Course Website, W3Schools, Paulo Drefahl.
# I consider every code is obvious
import time


def display_points(player_score):
    """
    This function is used to display the amount of correct answers gotten.
    :param player_score:
    """
    print('\nCONGRATULATIONS! YOU HAVE FINISHED THE QUIZ.')
    print("Loading scores...")

# I used this to display numbers from 1 to 4, with gap of one second.
    for i in range(1, 5):
        time.sleep(1)
        print(i, "...")

# I used this to give a final message to the user based on their results
    if player_score >= 7:
        print("Well done! Final score: {} / 12".format(player_score))
    else:
        print("You need to improve! Final score: {} / 12".format(player_score))


def main():
    """
    This is the main function, this functions runs the program.
    :return:
    """
    player_score = 0
    print('HI THERE!', end=' ')
    print("WELCOME TO THIS QUIZ\nLET'S BEGIN!\nGENERAL KNOW", "LEDGE QUIZ",
          sep='')

    print('QUESTION 1')
    first_question = input('What is the capital of United States?\n')
    if first_question == 'washington' or first_question == \
            'Washington' \
            or first_question == 'washington d.c.' \
            or first_question == 'Washington D.C.':
        print('Correct!')
        player_score += 1
    else:
        print('Incorrect')

    print('QUESTION 2')
    second_question = input('How much is 23 + 15?\n')
    if second_question == '38':
        print('Correct!')
        player_score += 1
    elif second_question != '38':
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
    fifth_question = input('How many continents are there in the world '
                           'based on the ONU?\n')
    if fifth_question == '5' or fifth_question == 'five' or \
            fifth_question == 'Five':
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
    if seventh_question == 'no' or seventh_question == 'No' or \
            seventh_question == 'NO':
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
    if nine_question == 'spanish' or nine_question == 'Spanish' and not \
            nine_question == 'mexican':
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

# I used while, try, and except, to avoid the program to crash if entered a
# string
    keep_running = True
    while keep_running:
        try:
            print('QUESTION 11')
            eleven_question = float(input('Type a number higher than -1\n'))
            if eleven_question > -1:
                print('Correct!')
                player_score += 1
            else:
                print('Incorrect')
            keep_running = False
        except ValueError:
            print("Invalid Input, try again.")

# I used while, try, and except to avoid the program to crash if entered a
# string
    keep_running = True
    while keep_running:
        try:
            print('QUESTION 12')
            twelve_question = int(input('Type a whole number between 351 '
                                        'and 791\n'))
            if 351 <= twelve_question <= 791:
                print('Correct!')
                player_score += 1
            else:
                print('Incorrect')
            keep_running = False
        except ValueError:
            print('Invalid Input, try again.')

    display_points(player_score)

    print("\nExtra numbers to meet requirements:")
    print(17 // 4, 25 % 6, 'hello' * 5)


main()
# '**' is used to set an exponent to a number
# '*' is used for multiplication
# '/' is used for division
# '//' it rounds down to the nearest whole number
# '%' it returns the remainder of dividing the left-hand operand by
# right-hand operand
# '+' as numeric operator is used for addition
# '-' is used for subtraction
# ',' is used to set a space between strings
# '+' as string operator is used to join strings
