def get_starting_number():
    while True: 
        answer = input("How many bottles of beer on the wall? ")
        if answer.isdigit() and int(answer) >= 1:
            return int(answer)
        print("Please enter a valid entry")

def sing(starting_bottles):
    '''
    Based on user's input, sing the rhyme. 
    '''
    bottles = starting_bottles

    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottle = bottles - 1
            if next_bottle == 1:
                word = "bottle"
            else:
                word = "bottles"
            print(f"Take one down, pass it around, {next_bottle} {word} of beer on the wall.\n")
        bottles = bottles - 1