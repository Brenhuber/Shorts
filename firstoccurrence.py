def find_first(filename, search_term):
    with open(filename, 'r') as file:
        content = file.read()
        position = content.find(search_term)
        return position if position != -1 else None

def is_file(filename):
    if filename.endswith(".txt"):
        return True
    else:
        print("Incorrect file type! Enter a proper file format.")
        return False

def main():
    contin = True
    while contin:
        filename = input("Enter file name: ")
        if is_file(filename):
            contin = False
            seeking = input("Enter the word or character you are looking for: ")
            position = find_first(filename, seeking)
            if position is not None:
                print(f"The first occurrence is at position {position}")
            else:
                print("The search term was not found in the file.") 
            break       
main()