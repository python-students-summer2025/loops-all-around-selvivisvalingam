def get_starting_number():
    '''
    Ask user to input how many bottles of beer to start the rhyme using while loops.
    '''
    while True: 
    # ask user to input how many bottles of beer on the wall
        answer = input("How many bottles of beer on the wall? ")
    # validate/return that user input is a digit and above 1
        if answer.isdigit() and int(answer) >= 1:
            return int(answer)
        else:
            print("Please enter a valid entry")

def sing(starting_bottles):
    '''
    Based on input, start the rhyme using while loops with accumulator (counter).
    '''
    bottles = starting_bottles # start counter

    while bottles > 0:
        if bottles == 1: # special case for 1 bottle
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else: # regular, plural case
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottle = bottles - 1
            # decide between "bottle" and "bottles" based on counter
            if next_bottle == 1:
                word = "bottle"
            else:
                word = "bottles"
            print(f"Take one down, pass it around, {next_bottle} {word} of beer on the wall.\n")
        bottles = bottles - 1 # decrease counter