class Graph:
    def __init__(self):
        self.users = {}
        self.graph = []

    def add_user(self, username):
        if username in self.users:
            print(f"User already exists")
        else:
            self.users[username] = len(self.graph)
            for row in self.graph:
                row.append(0)
            self.graph.append([0] * (len(self.graph) + 1))
        return self
    
    def remove_user(self, username):
        
        if username not in self.users:
            print(f"User does not exist")
            return
        else:
            index = self.users[username]
            
            del self.users[username]
            
            del self.graph[index]
            
            for row in self.graph:
                del row[index]
                
            for key , value in self.users.items():
                if value > index:
                    self.users[key] = value - 1
        
            
    
    

def main():
    socialmedia = Graph()
    print("Hello, there are a list of choices:")
    while True:
        user_input = int(input(" 1. Add a user to the platform.\n 2. Remove a user from the platform.\n 3. Send a friend request to another user.\n 4. Remove a friend from your list.\n 5. View your list of friends.\n 6. View the list of users on the platform.\n 7. Exit\n Please enter your choice here: "))
        if user_input == 1:
            username = input("Enter the username to add:")
            socialmedia.add_user(username)
            
        elif user_input == 2:
            username = input("Enter the username to remove:")
            socialmedia.remove_user(username)

if __name__ == "__main__":
    main()
