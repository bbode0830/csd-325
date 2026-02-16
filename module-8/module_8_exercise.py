'''
Ben Bode
2/14/2026
Assignment 8.2
CSD 325
working with JSON files: loading, editing, and dumping
'''

import json

with open ('Student.json') as input_file:
    data = json.load(input_file)

#main program
def main():
    
    #print the json file
    print_class_list()
    print('This is the JSON file without adding any class data.\n')

    #add new data and display it
    my_data = {'F_Name': 'Ben', 'L_Name': 'Bode', 'Student_ID': 238943, 'Email': 'benjaminb@cra-school.org'}
    data.append(my_data)
    print('This is the updated class data:')
    print_class_list()

    #rewrite the file to include the new student data
    with open('Student.json', 'w') as output_file:
        json.dump(data, output_file)
    output_file.close()
    print('\nThe JSON file was updated!')

    

if __name__ == '__main__':
    main()


#print function for the json file
def print_class_list():
    
    count = 0

    for item in data:
        count+=1
        #make each object in the list into a dictionary to reference certain values in it
        dictionary = item

        #print the values in the correct format
        print(f'{count}. {dictionary['L_Name']}, {dictionary["F_Name"]}: ID = {dictionary['Student_ID']}, '
             f'Email = {dictionary['Email']}')