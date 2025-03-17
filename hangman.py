import random

def choose_word():
    words_with_hints = {
        'python': 'A popular programming language.',
        'hangman': 'A classic word-guessing game.',
        'programming': 'The process of writing computer code.',
        'developer': 'A person who writes and maintains software.',
        'challenge': 'Something that tests your ability.',
        'algorithm': 'A step-by-step procedure for solving a problem.',
        'function': 'A reusable block of code.',
        'variable': 'A storage location in programming.',
        'loop': 'A construct for repeating code.',
        'condition': 'A statement that evaluates to true or false.',
        'exception': 'An error that occurs during program execution.',
        'dictionary': 'A collection of key-value pairs.',
        'iteration': 'The process of looping through elements.',
        'recursion': 'A function that calls itself.',
        'syntax': 'Rules that define correct programming structure.',
        'debugging': 'The process of finding and fixing errors.',
        'compiler': 'A tool that translates code into machine language.',
        'interpreter': 'A program that executes code line by line.',
        'inheritance': 'A key concept in object-oriented programming.',
        'polymorphism': 'A concept allowing methods to take different forms.'
    }
    word = random.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word]
    return word, hint

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word, hint = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    
    print("Welcome to Hangman!")
    print(f"Hint: {hint}")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! {attempts} attempts remaining.")
        else:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                return
    
    print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
