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
