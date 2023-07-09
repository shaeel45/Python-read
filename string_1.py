def read_file(file_name):
    """Reads in a file and returns its contents as a string.

    Args:
        file_name (str): The name (and path) of the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_name, 'r') as f:
        contents = f.read()
    print(contents)
    return contents

def read_file_into_list(file_name):
   with open('sampletext.txt','r') as file:
       print(open(file_name))

""" Reads in a file and stores each line as an element in a list.

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE

    

def write_first_line_to_file(file_contents, output_filename):
    lines = file_contents.split('\n')
    first_line = lines[0]
    with open(output_filename, 'w') as file:
        file.write(first_line)



def read_even_numbered_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    even_lines = [line for index, line in enumerate(lines) if index % 2 != 0]
    return even_lines

def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    reversed_lines = list(reversed(lines))
    print(reversed_lines)
    return reversed_lines

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()