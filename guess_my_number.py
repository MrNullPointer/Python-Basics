say = input("Please think of a number between 0 and 100")

start = 0.0 
end  = 100.0
ans = (start + end)/2

print("Is your secret number", str(ans))

direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while True:
    if direction == 'c' or direction == 'C':
        print("Game over. Your secret number was", str(ans))
        break
    elif direction == 'h' or direction == 'H':
        end = ans
        ans = (start + end)/2
        print("Is your secret number", str(ans))
        direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif direction == 'l' or direction == 'L':
        start = ans
        ans = (start + end)/2
        print("Is your secret number", str(ans))
        direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print("Sorry, I did not understand your input.")
        direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
