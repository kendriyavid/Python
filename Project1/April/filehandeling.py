# file = open('document.txt','a')
# file.write("Hi Harshdeep here\nThis is demo file\n")
# # print(file.read(10))
# # print(file.read(10))

# file.close()


# file=open("document.txt",'r')
# for i in file:
#     print(i)

# try:
#     f= open("document.txt",'r')
# except FileNotFoundError as msg:
#     print("file not found")
#     print(msg)
# else:
#     print(f.read())
# finally:
#     print("closing file")
#     f.close()
## wap to read a file line by line and store into a list

# fname = input("enter file name")

# def fileread(fname):
#     f = open(fname,'r')
#     return f.read().split()
# print(fileread(fname))

# ## wap a program to cout number of lines in file
# def nlines(fname):
#     f = open(fname,'r')
#     return len(f.readlines())
# print(nlines(fname))

# from collections import Counter

# def word_count(fname):
#     with open(fname, 'r') as f:
#         return Counter(f.read().split())

# print(word_count("employee.txt"))

## program to copy from one file to another

# import shutil
# shutil.copyfile('employee.txt','employee2.txt')

# import os

# def create_file(fname):
#     with open(fname, 'w') as f:
#         f.write("hello world")
#         print(fname, "created")

# def read_file(fname):
#     with open(fname, 'r') as f:
#         data = f.read()
#     print(data)  # Print the data from the file

# def append_file(fname, text):
#     with open(fname, 'a') as f:
#         f.write(text)
#         print(f"Text appended to {fname}")

# def rename_file(fname, new_name):
#     os.rename(fname, new_name)
#     print(f"{fname} renamed to {new_name}")

# # Example usage:
# create_file('example.txt')
# read_file('example.txt')
# append_file('example.txt', " More text")
# rename_file('example.txt', 'new_example.txt')

## write a program to search given string in text file

def search_string_in_file(filename, search_string):
    """Search for a given string in a file and return lines containing the string."""
    line_numbers = []
    lines_with_string = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                if search_string in line:
                    line_numbers.append(line_number)
                    lines_with_string.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        return None
    
    return line_numbers, lines_with_string

def main():
    filename = input("Enter the filename: ")
    search_string = input("Enter the search string: ")
    results = search_string_in_file(filename, search_string)

    if results:
        line_numbers, lines_with_string = results
        if line_numbers:
            print(f"The string '{search_string}' was found in the following lines:")
            for line_number, line in zip(line_numbers, lines_with_string):
                print(f"Line {line_number}: {line}")
        else:
            print(f"The string '{search_string}' was not found in the file.")
    else:
        print("No results returned, possibly due to an error.")

if __name__ == "__main__":
    main()
