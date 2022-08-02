import random
import hangman_words
import hangman_art
end_game = False

word_random = random.choice(hangman_words.word_list)

lives = 6
display = []
char_used = []
print(word_random)

print(hangman_art.logo)

for char in range(0, len(word_random)):
    display.append('_')


while not end_game:
    guess = input("Guess a letter: ").lower()
    
    
    for position in range(0, len(word_random)):
        letter = word_random[position]
        if letter == guess:
            display[position] = letter
    if guess in char_used:
        print("You've alredy used this word")
    elif guess not in display:
        print(f"You guessed {guess} ,that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        print("***You lose***")
        end_game = True
    if '_' not in display:
        end_game = True
        print("***You Win***")
    print(display)
    char_used.append(guess)
    print(hangman_art.stages[lives])