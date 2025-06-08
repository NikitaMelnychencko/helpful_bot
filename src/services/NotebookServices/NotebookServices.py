class NotebookServices:
  def __init__(self):
    self.contacts = {}

  def add_contact(self, args):
    name, phone = args
    self.contacts[name] = phone
    return print(f"Contact {name} added.")


  def check_contact(self, name):
    if name in self.contacts:
      return True
    else:
      return False


  def change_contact(self, args):
    name, phone = args
    if not self.check_contact(name):
      print(f"Contact {name} not found.")
      answer = input("Create new contact? (y/n)")
      if answer.lower() == "y":
        self.add_contact(args)
      else:
        self.contacts[name] = phone
        return print(f"Contact {name} changed.")

  def get_contact(self, name):
    if not self.check_contact(name):
      return print(f"Contact {name} not found.")

    return print(f"Contact {name}: {self.contacts[name]}")

  def get_all_contacts(self):
    return print(self.contacts)
