secret_word = "alvin"
guess = ""
limit = 3
count = 1

while guess != secret_word and count <= limit:
    guess = input("Enter the secret word: ")
    count += 1

if guess == secret_word:
    print("Congratulations. You guessed the seceret word")
else:
    print("Game over!")