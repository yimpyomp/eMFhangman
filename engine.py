import json
import random
import re
import os
from pitture_engine import *


# Hardcode wordlist json
def load_words():
    current_location = os.path.dirname(os.path.abspath(__file__))
    word_path = os.path.join(current_location, 'wordlist.json')
    f = open(word_path)
    raw_list = json.load(f)
    return raw_list['data']


# Get random word from list
def get_word(wordlist):
    if not isinstance(wordlist, list):
        raise Exception('Invalid wordlist provided')
    random_index = random.randrange(len(wordlist))
    return wordlist[random_index]


# Generate a string composed of underscores to represent current guess status
def generate_word_image(word):
    word_size = len(word)
    blank_word = []
    while len(blank_word) < word_size:
        blank_word.append('_')
    return blank_word


# Search given word for all instances of character existing
def find_characters(word, character):
    matching_index = []
    for match in re.finditer(character, word):
        matching_index.append(match.start())
    # Return a list containing character and indices of matches if found
    if matching_index:
        return [character, matching_index]
    # Return empty list if no results
    else:
        return matching_index


# Update word image for correct guesses
def update_word_image(current_image, match_list):
    for entry in match_list[1]:
        current_image[entry] = match_list[0]
    return current_image


def display_standing(image, bad_guesses, remaining_guesses):
    current_image = draw_stage(remaining_guesses)
    print(f'\n\n\n {current_image} \n\n'
          f'Your word:          {image} \n'
          f'Incorrect guesses:  {bad_guesses} \n'
          f'Attempts remaining: {remaining_guesses}')
    return None


def winner(image, bad_guesses, remaining_guesses):
    print(f'*********************************************************************************************************\n'
          f'Damn you fuckin won the shit out of this. \n'
          f'Your word was: {"".join(image)} \n'
          f'Your bad guesses: {bad_guesses} \n'
          f'You had {remaining_guesses} attempts remaining \n'
          f'******************************************************************************************************\n\n')
    return None


def loser(word, image, bad_guesses):
    print(f'*********************************************************************************************************\n'
          f'{full_hang} \n\n'
          f'You fuckin lost. \n'
          f'Your word was: {word} \n'
          f'Your final result: {"".join(image)} \n'
          f'Your incorrect guesses: {bad_guesses} \n'
          f'******************************************************************************************************\n\n')
    return None


def gimme_hint(word, remaining_guesses, image):
    remaining_guesses -= 1
    for character in image:
        if character == '_':
            position = image.index(character)
            image[position] = word[position]
            break
    return image, remaining_guesses


def welcome_screen():
    print(f'Welcome to my fuckin hangman thing. This shit will keep going until you hit Ctl+C. \n'
          f'If you find some bugs or something lmk. I aint tryna make buncha broke shit. \n'
          f'*******************************************************************************************************\n')
    return None


def play_hangman():
    raw_words = load_words()
    game_word = get_word(raw_words)
    #game_word = 'capable'
    attempts_remaining = 6
    word_image = generate_word_image(game_word)
    incorrect_guesses = []
    welcome_screen()
    display_standing(word_image, incorrect_guesses, attempts_remaining)
    while attempts_remaining > 0:
        user_guess = input('Enter your guess: ').lower()
        if user_guess == 'hint':
            if attempts_remaining > 1:
                print(f'Oh looks like you found this thing. You lose an attempt, and you get a letter.')
                word_image, attempts_remaining = gimme_hint(game_word, attempts_remaining, word_image)
                display_standing(word_image, incorrect_guesses, attempts_remaining)
            else:
                print('Nah yeen got that kinda coin')
        else:
            match_result = find_characters(game_word, user_guess)
            if not match_result:
                attempts_remaining -= 1
                if user_guess in incorrect_guesses:
                    print("If that didn't work the first time why the fuck do you keep trying it?")
                incorrect_guesses.append(user_guess)
            else:
                word_image = update_word_image(word_image, match_result)
            # Check to see if user has correctly guessed all words
            if '_' not in word_image:
                winner(word_image, incorrect_guesses, attempts_remaining)
                break
            display_standing(word_image, incorrect_guesses, attempts_remaining)
    if attempts_remaining == 0:
        loser(game_word, word_image, incorrect_guesses)
    return None


play_hangman()