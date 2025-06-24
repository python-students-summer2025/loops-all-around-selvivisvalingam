def get_starting_number():
    '''
    Ask user to input how many bottles of beer to start the rhyme.
    '''
    # ask user to input how many bottles of beer on the wall
    answer = input("How many bottles of beer on the wall? (must be a whole number above 1) ")
    # validate/return that user input is a digit and above 1
    if answer.isdigit() and int(answer) >= 1:
        return int(answer)
    else:
        # if input entered in invalid, ask user to try again
        print("Please enter a valid entry")
        return get_starting_number()

def sing(starting_bottles):
    '''
    Based on input, start the rhyme using for loops.
    '''
    # Use for loop to count down from the starting number
    for bottles in range(starting_bottles, 0, -1):
        if bottles == 1: # special case for last bottle (singular)
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else: 
            # regular case for plural bottles
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottle = bottles - 1 # decrease counter
            # Decide whether to print 'bottle' or 'bottles' based on next number
            if next_bottle == 1:
                word = "bottle"
            else: 
                word = "bottles"
            # print the next line and continue this pattern
            print(f"Take one down, pass it around, {next_bottle} {word} of beer on the wall.\n")
