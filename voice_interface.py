# text_interface.py

def get_user_input():
    user_input = input("Enter a command: ")
    return user_input

def process_user_input(user_input):
    # Process the user input here
    # For example, you can use if-else statements or a dictionary to map commands to actions
    if user_input == "hello":
        return "Hello! How can I assist you today?"
    elif user_input == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "I didn't understand your command. Please try again."

def main():
    while True:
        user_input = get_user_input()
        response = process_user_input(user_input)
        print(response)

if __name__ == '__main__':
    main()