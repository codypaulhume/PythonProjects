import hashlib
import os

# This program takes in the word list and the shapass file and opens the file
# It then iterates through the wordlist and passes it through the hash function
# Finally, the program compares all the hashed values with shapass 

def main():
    wordlist = open("abridged_rockyou.txt", "r")
    givenPass = open("chume1-shapass", "r")

    ans = givenPass.read()
    
    for x in wordlist:
        password = x
        # Strip is important to remove "\n" after the word
        wordHash = compute_hash(x.strip())
        print(wordHash)
        if ans == wordHash:
            print("\n")
            print("Password: " + password)
            print("Hash: " + wordHash)
            print("\n")
            break
        
def compute_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    main()