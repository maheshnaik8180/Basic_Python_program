"""given user input replace the word """
"""using length function calculate length"""

try:
    username = str(input("Enter Name: "))
    length = len(username)
    if length >= 3:
       print(f"hello {username}, How are you?")
    else:
        print("username should be minimum 3 character")

except Exception:
        print("Exception occured")
