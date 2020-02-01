#**************Bisection search square root *********///

#num = 25
#epsilon = 0.01
#step = 0.01
#start = 1.0
#end = num
#totalSteps = 0
#ans = (start + end) /2

#while abs(ans**2 - num) >= epsilon:
#    if(ans**2 > num):
#        end = ans
#        ans = (start + end)/2
#        totalSteps += 1
#    else:
#        start = ans
#        ans = (start + end)/2
#        totalSteps += 1

#print ("number of guesses are: ", str(totalSteps))

#print(str(ans), "is close to square root of ", str(num))

#**************Bisection search cube root *********///

#num = 27
#epsilon = 0.00001
##step = 0.01
#start = 1.0
#end = num
#totalSteps = 0
#ans = (start + end) /2

#while abs(ans**3 - num) >= epsilon:
#    if(ans**3 > num):
#        end = ans
#        ans = (start + end)/2
#        totalSteps += 1
#    else:
#        start = ans
#        ans = (start + end)/2
#        totalSteps += 1

#print ("number of guesses are: ", str(totalSteps))

#print(str(ans), "is close to cube root of ", str(num))