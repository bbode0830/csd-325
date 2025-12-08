#display the nummber of beer bottles on the wall
num_left = int(input("Please enter the number of bottles:"))

#make a loop that subtracts one bottle and displays the number left
while num_left > 1:
    print(f"{num_left} bottles of beer on the wall, {num_left}"
          " bottles of beer.")
    num_left = num_left-1
    print(f"Take one down and pass it around, {num_left} bottles"
          " of beer on the wall.\n")

#when there is 1 bottle left, pass it around and buy more
print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down and pass it around, 0 bottles of beer on the wall")
print("\nTime to buy more bottles of beer.")