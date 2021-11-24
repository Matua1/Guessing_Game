#Guessing Game Version1
#25/11/21
#Matua Halafihi
import random
#Target variable to store a random target number.
target = random.randint(1, 100)
# guess variable to store user input
guess = int(input("Please guess the number: "))

if guess == target:  # Check that the user's guess is the same as the target 
print("Congratulations! You got the number!")
elif guess < target: # Check that the user's guess is lower than the target
    print("Your guess is too low.")
  elif guess > target: # Check that the user's guess is higher than the target
    print("Your guess was too high! ")
  else:  # In case something goes wrong
    print("Something went wrong")