import requests
import threading
from queue import Queue

# Configurations
target_url = input("Enter the target URL (e.g., http://example.com): ").strip('/')
wordlist_path = input("Enter the path to the wordlist (e.g., directory-list-2.3-medium.txt): ").strip()
threads = int(input("Enter the number of threads (e.g., 20): "))

# Queue to store the words 
queue = Queue()

# Fuzzing
def fuzz_directory():
    while not queue.empty():
        directory = queue.get()
        url = f"{target_url}/{directory}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[+] Directory found: {url}")
        except requests.exceptions.RequestException:
            pass
        queue.task_done()

# Load the wordlist and fill queue
with open(wordlist_path, 'r') as wordlist_file:
    for line in wordlist_file:
        queue.put(line.strip())

# Threading
for _ in range(threads):
    t = threading.Thread(target=fuzz_directory)
    t.daemon = True
    t.start()

# Wait for all threads to finish 
queue.join()

print("Fuzzing complete.")
