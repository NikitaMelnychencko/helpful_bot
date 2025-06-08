from services.NotebookServices import NotebookServices


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

welcome_bunner = """
 █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗    ██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║       ██████╔╝██║   ██║   ██║
██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║       ██╔══██╗██║   ██║   ██║
██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║       ██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝

"""

commands = """
  Commands:
  ---------
  1. hello
  2. add <username> <phone>
  3. change <username> <phone>
  4. phone <username>
  5. all
  6. close, exit
  ---------
"""

def main():
    contacts = NotebookServices()
    print(welcome_bunner)
    print("Welcome to the assistant bot!")
    print(commands)


    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match  (command):
            case "hello":
                print("How can I help you?")
            case "add":
                contacts.add_contact(args)
            case "change":
                contacts.change_contact(args)
            case "phone":
                contacts.get_contact(args[0])
            case "all":
                contacts.get_all_contacts()
            case "exit" | "close":
                print("Good bye!")
                break
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
