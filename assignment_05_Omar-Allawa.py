class Node:
    def __init__(self , name , family_name , birthdate):
        self.right = None
        self.left = None
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate

def main():
    print ("Hello , there are a list of choices:")
    user_input = int(input(" 1. Add Family Member\n 2. Display Sorted Birthdays\n 3. Find Relationship\n 4. Visualize Family Tree\n 5. Count Same First Names\n 6. Exit\n please enter you choice here : "))
    
if __name__ == "__main__":
    main()
   