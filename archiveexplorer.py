import os
from tqdm import tqdm
#Finding file
def find_file(file_name, start_dir):
    for root, _, files in tqdm(os.walk(start_dir), desc="Searching files", unit="directory"):
        if file_name in files:
            return os.path.join(root, file_name)
    return None
#First 10 lines
def print_first_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file]
            print("First 10 lines of the file:")
            for line in lines[:10]:
                print(line)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
#UX
def main():
    while True:
        file_name = input("Enter the file name: ")
        start_dir = '/'
        path = find_file(file_name, start_dir)

        if path:
            print(f"File found at: {path}")
            print_first_lines(path)
        else:
            print(f"File '{file_name}' not found.")
        
        again = input("Do you want to search for another file? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Ending application...")
            break
#Checks execution
if __name__ == "__main__":
    main()
