'''
Created on Jan. 23, 2024

@author: sebbe
'''
def decrypt(shift, code): 
    '''
    Takes a string and a value to shift it by and returns the decrypted caeser cipher
    '''
    aList = []
    code = code.lower() #Turns the code into lowercase, Important since capital and lowercase have different unicode values
    for char in code:
        if ord(char) >= 97 and ord(char) <= 122: #this is to account for special characters outside the alphabet
            uni_char_int = ord(char) - 97 # I substract 97 since it makes it so a is 0 and z is 25 meaning I can use %26 later
            original_int = ((uni_char_int - shift) % 26) + 97 # this provides the character before the encryption, %26 allows it to loop around if it goes past z and + 97 accounts for the -97 from earlier
            aList.append(chr(original_int))
        else :
            aList.append(char)
            
    return "".join(aList)

    
def get_input_file():
    '''
    Asks the user to input the name of a text file and if the input ends with '.txt' returns the file name
    eg.
    inputting secretMessage1.txt would return 'secretMessage1.txt'
    while inputting secret would ask the user for a valid file name again
    '''
    user_input = input("Please provide a valid text file name: ")
    while not user_input.endswith(".txt"):
        user_input = input("Invalid filename extension. Please provide a valid text file name: ")
    return user_input

def main():
    file_name = get_input_file() 
    with open(file_name, "r") as file: 
        lines = file.readlines()
        
    for i in range(len(lines)): #removes all new line and whitespace characters that are at the ends of the file
        lines[i] = lines[i].strip()
    
    print("The decrypted message is: ")
    print(decrypt(int(lines[0]),lines[1]))
if __name__ == "__main__" :
    main()