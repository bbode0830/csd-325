'''
Ben Bode
12/14/2025
module 2.2 - debugging a program from a previous class
'''

#welcome user and state purpose of program
def welcome_user():
    print('This program converts miles to kilometers.')
    print('For your reference 1 mile = 1.609 kilometers.')

#convert miles to kilometers
def convert_mi_km(miles):
    return miles*1.609

def main():
    welcome_user()
    mi_driven = float(input('please enter the number of miles driven:\n'))
    km = convert_mi_km(mi_driven)
    print(f'You drove {mi_driven:.2f} miles or {km:.2f} kilometers.')

#run the main function only if the program is being used
#as a stand alone program
if __name__ == '__main__':
    main()