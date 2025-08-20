# Family Assistant Bot  

A smart assistant designed to help your loved ones, especially grandparents, easily remember and access important family information.  

---

### Installation:
Installation is straightforward via pip in project folder:
```
pip install .
```

### List of all functions:
- Add,change and delete contacts, phone numbers, emails, home address, birthdays of loved ones
- Calculate birthdays in the next days
- Add, change and delete notes
- Search for any saved data.
- Seach through the notes with any word or tags

### Used libraries (see requirements.txt):
- colorama
- prompt-toolkit


### Basic syntax:
- "hello"                                            to start using personal assistant;
- "exit"                                             to close the personal assistant;
- "add [name] [phone number]"                        to add contact;
- "change-phone [name] [old phone] [new phone]"      to change contact number;
- "all"                                              to get all contacts;
- "phone [name]"                                     to get contacts phone numbers;
- "delete-phone [name] [number]"                     to delete phone number";
- "add-birthday [name] [DD.MM.YYYY]"                 to add contacts birthday date";
- "show-birthday [name]"                             to show contacts birthday date;
- "birthdays [days]"                                 to show all birthdays for the following [days];
- "add-email [name] [email]"                         to add contacts email;
- "change-email [name] [email]"                      to change contacts email;
- "delete-email [name]"                              to delete contacts email;
- "delete-contact [name]"                            to delete contact from adress book fully;
- "add-address [name] [address in any format]"       to add home address;
- "change-adress [name] [new address in any format]" to change home address;
- "find [any word, digit or symbol]"                 to find all the matches in the contacts;
- "add-note [name] [note in any format]"             to add note to contact;
- "change-note [name] [new note in any format]"      to change note to contact;
- "delete-note [name]"                               to delete contacts note;
- "search-note [any word, digit or symbol]"          to search in contacts notes;
- "add-tags [name] [any word with # prefix]"         to tags to contacts notes;
=======
# GrannyHelper
A smart assistant designed to help your loved ones, especially grandparents, easily remember and access important family information.

🚀 Installation
Install the project via pip inside the project folder:

pip install .

✨ Features
Manage contacts: add, update, and delete phone numbers, emails, addresses, and birthdays
Track upcoming birthdays within a chosen number of days
Create, update, and delete notes for each contact
Search across all saved data (contacts, notes, tags)
Organize notes with custom tags

📚 Dependencies
All dependencies are listed in requirements.txt:
colorama
prompt-toolkit

💻 Basic Commands
Command Example	Description
hello	Start the assistant
exit	Exit the assistant
add [name] [phone number]	Add a new contact with phone number
change-phone [name] [old phone] [new phone]	Update an existing phone number
all	Show all contacts
phone [name]	Get phone numbers of a contact
delete-phone [name] [number]	Delete a phone number
add-birthday [name] [DD.MM.YYYY]	Add a birthday
show-birthday [name]	Show a contact’s birthday
birthdays [days]	Show upcoming birthdays within [days]
add-email [name] [email]	Add an email address
change-email [name] [email]	Change an email address
delete-email [name]	Delete an email address
delete-contact [name]	Fully remove a contact
add-address [name] [address]	Add a home address
change-address [name] [new address]	Update a home address
find [query]	Search across all contacts
add-note [name] [note]	Add a note to a contact
change-note [name] [new note]	Update a contact’s note
delete-note [name]	Delete a contact’s note
search-note [query]	Search through notes
add-tags [name] [#tag]	Add tags to a contact’s note

🧩 Example Use Cases
Remind your grandmother about upcoming birthdays
Store family members’ addresses and phone numbers
Keep track of important notes with tags like #health or #holiday
