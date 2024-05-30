import tkinter as tk

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Contacts dictionary to store name and number pairs
        self.contacts = {}

        # Labels, Entry boxes, and Buttons
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.number_label = tk.Label(root, text="Number:")
        self.number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.number_entry = tk.Entry(root)
        self.number_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", bg="#3697f5", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.display_button = tk.Button(root, text="Display Contacts", bg="#fe9037",command=self.display_contacts)
        self.display_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.clear_button = tk.Button(root, text="Clear",bg="#f44336", command=self.clear_fields)
        self.clear_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name and number:
            self.contacts[name] = number
            self.result_label.config(text="Contact added: {} - {}".format(name, number))
        else:
            self.result_label.config(text="Please enter both name and number.")

    def display_contacts(self):
        if self.contacts:
            contacts_list = "\n".join(["{} - {}".format(name, number) for name, number in self.contacts.items()])
            self.result_label.config(text=contacts_list)
        else:
            self.result_label.config(text="No contacts added yet.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.result_label.config(text="")

# Create main window
root = tk.Tk()
app = ContactBookApp(root)

# Run the main event loop
root.mainloop()
