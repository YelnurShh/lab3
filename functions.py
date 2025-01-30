def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
Ints = [2, 3, 4, 5, 0, 0, 7]
print(unique_elements(Ints))


import random  

def guess_the_number():
  
    number_to_guess = random.randint(1, 20)
    
    print("Hello! What is your name?")
    name = input() 
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    
    attempts = 0
    while True:
        try:
            guess = int(input()) 
            attempts += 1
            
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")


guess_the_number()


def histogram(lst):
    for num in lst:
        print('*' * num)
MyList=[2,4,6,7,3]
print(histogram(MyList))