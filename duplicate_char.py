#Python – Find all duplicate characters in string


def duplicate_characters(string):
    # Create an empty dictionary
    chars = {}
 
    # Iterate through each character in the string
    for char in string:
        # If the character is not in the dictionary, add it
        if char not in chars:
            chars[char] = 1
        else:
            # If the character is already in the dictionary, increment the count
            chars[char] += 1
 
    # Create a list to store the duplicate characters
    duplicates = []
 
    # Iterate through the dictionary to find characters with count greater than 1
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
 
    return duplicates
 
# Test cases
print(duplicate_characters("duplicatestringcounts"))


Another:

#Python – Find all duplicate characters in string

def find_dup_char(input):
    x=filter(lambda x: input.count(x)>=2,input)
    print(''.join(x))

if __name__=="__main__":
    input='geeksforgeeks'
    find_dup_char(input)
