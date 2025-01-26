import os



# Create a file and write data to it
def create_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        print(f"File '{filename}' created.")
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")



# Read a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"Contents of '{filename}':\n{content}")
    except OSError:
        print(f"Error: File '{filename}' not found.")




# Search for files in a directory based on a keyword
def search_files(directory, keyword):
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}': {files}")
        matching_files = [f for f in files if keyword in f]
        print(f"Files matching '{keyword}': {matching_files}")
    except OSError:
        print(f"Error: Directory '{directory}' not found.")





# Search for a specific file in the file system
def search_specific_file(directory, target_file):
    try:
        files = os.listdir(directory)
        print(f"Searching in '{directory}'...")
        if target_file in files:
            print(f"File '{target_file}' found in '{directory}'.")
            return True
        else:
            print(f"File '{target_file}' not found in '{directory}'.")
            return False
    except OSError:
        print(f"Error: Directory '{directory}' not found.")
        return False






# Export a file to another directory
def export_file(filename, target_directory):
    try:
        # Ensure the target directory exists
        if target_directory not in os.listdir():
            os.mkdir(target_directory)
        target_file = f"{target_directory}/{filename.split('/')[-1]}"
        with open(filename, 'r') as src:
            content = src.read()
        with open(target_file, 'w') as dst:
            dst.write(content)
        print(f"File '{filename}' exported to '{target_file}'.")
    except OSError as e:
        print(f"Error exporting file '{filename}': {e}")




# Test cases:

# Create a directory if it doesn't exist
try:
    os.mkdir("my_files")
except OSError:
    print("Directory 'my_files' already exists.")

# Create files
create_file("my_files/animals.txt", "cats\ndogs\n")
create_file("my_files/major.txt", "computer science\nelectrical engineering\n")

# Read files
read_file("my_files/animals.txt")
read_file("my_files/major.txt")

# Search for files with a keyword
search_files("my_files", "major")

# Search for a specific file
found = search_specific_file("my_files", "animals.txt")
if found:
    print("The specific file search was successful!")

# Export a file to another directory
export_file("my_files/animals.txt", "exported_files")

