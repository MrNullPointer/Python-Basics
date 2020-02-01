
#iteration = 0

#while iteration < 5:
#    for i in "hello":
#        if iteration%2 == 0:
#            break
#    iteration += 1

#******Find the cube root using guesses****#

#cube = int (input("Please enter a number to find the cube root!!: "))
#guess = 0.0
#increment = 0.0001
#guessNumber = 0
#proximity = 0.001

#while abs(cube - guess**3) > proximity:
#    guess += increment
#    guessNumber += 1

#print("The number guessed is :", str(guess))

#if abs(guess**3 - cube) >= proximity:
#    print("Failed!!", "Number of iterations are: ", str(guessNumber))
#else: print ("The cube root of", str(cube), "is close to:", str(guess))


#******Find the square root using guesses****#
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))