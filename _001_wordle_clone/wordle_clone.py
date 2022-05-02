
from rich.prompt import Prompt
from rich.console import Console
from random import choice
from word_list import wordle_list

SQUARES = { 'right_place': '🟩', 'right_letter': '🟨', 'wrong_letter': '⬛' }
WELCOME_MESSAGE = f'\n[white on black]Welcome to Wordle [/]\n'
PLAYER_INSTRUCTIONS = "You may start guessing\n"
GUESS_STATEMENT = "\nEnter your guess"
ALLOWED_GUESSES = 6

def right_place(letter):
    return f'[black on green]{letter}[/]'

def right_letter(letter):
    return f'[black on yellow]{letter}[/]'

def wrong_letter(letter):
    return f'[black on white]{letter}[/]'

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []

    # loop through the current guess
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += right_place(letter)
            wordle_pattern.append(SQUARES['right_place'])
        elif letter in answer:
            guessed += right_letter(letter)
            wordle_pattern.append(SQUARES['right_letter'])
        else:
            guessed += wrong_letter(letter)
            wordle_pattern.append(SQUARES['wrong_letter'])

    return ''.join(guessed), ''.join(wordle_pattern)

def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    
    # Game over
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    console = Console()
    chosen_word = choice(wordle_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)
