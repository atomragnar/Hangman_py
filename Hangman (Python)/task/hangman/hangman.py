# Write your code here
import random
import re

letter_not_word = "That letter doesn't appear in the word.\n"
game_begins = 'H A N G M A N\n'
final_message = 'Thanks for playing!'
game_menu = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
enter_lowercase_letter = 'Please, enter a lowercase letter from the English alphabet.'
enter_single_letter = 'Please, input a single letter.'
already_guessed = "You've already guessed this letter.\n"
prompt_survived = 'You survived!'
prompt_lost = 'You lost!'
prompt_correct_guess = 'You guessed the word '

words = ['python', 'java', 'swift', 'javascript']
stats = [0, 0]


def get_input(list_hidden_word):
    pattern = '[a-z]'
    while True:
        print(*list_hidden_word, sep='')
        input_letter = input('Input a letter:')
        if re.search(pattern, input_letter) and len(input_letter) == 1:
            return input_letter
        else:
            input_check(input_letter)


def input_check(input_letter):
    if len(input_letter) == 1:
        print(enter_lowercase_letter + '\n')
    else:
        print(enter_single_letter + '\n')


def get_hidden_word(chosen_word):
    hidden = list()
    for x in range(len(chosen_word)):
        hidden.insert(x, '-')
    return hidden


def win_condition(list_hidden_word):
    for x in range(len(list_hidden_word)):
        if list_hidden_word[x] == '-':
            return False
    return True


def check_letter(list_word, list_hidden_word, input_letter):
    no_match = True
    for x in range(len(list_word)):
        if input_letter == list_word[x]:
            list_hidden_word[x] = list_word[x]
            no_match = False
    return no_match


def contains_letter(list_hidden_word, input_letter):
    for x in range(len(list_hidden_word)):
        if list_hidden_word[x] == input_letter:
            return True
    return False


def user_input_check(word, hidden_word, letter, attempts, guess_set):
    if guess_set.__contains__(letter):
        print(already_guessed)
    else:
        if check_letter(word, hidden_word, letter):
            print(letter_not_word)
            attempts -= 1
    guess_set.add(letter)
    return attempts


def print_win_text(hidden_word):
    correct_word = ""
    correct_word = correct_word.join(hidden_word)
    print(prompt_correct_guess + correct_word + '!')
    print(prompt_survived)
    print()


def game_loop(list_stats, list_words):
    attempts = 8
    game_lost = True
    guess_set = set()
    n = random.randrange(4)
    word = list(list_words[n])
    hidden_word = get_hidden_word(word)

    while attempts > 0:

        letter = get_input(hidden_word)

        attempts = user_input_check(word, hidden_word, letter, attempts, guess_set)

        if win_condition(hidden_word):
            print_win_text(hidden_word)
            game_lost = False
            list_stats[0] += 1
            break

    if game_lost:
        list_stats[1] += 1
        print(prompt_lost)


def display_stats(list_stats):
    print('You won: ' + str(list_stats[0]) + ' times')
    print('You lost: ' + str(list_stats[1]) + ' times')


print(game_begins)
game_on = True

while game_on:

    mode = input(game_menu)

    if mode == 'play':
        print()
        game_loop(stats, words)
    elif mode == 'results':
        display_stats(stats)
    elif mode == 'exit':
        game_on = False




