# Family Assistant Bot  

A smart assistant designed to help your loved ones, especially grandparents, easily remember and access important family information.  

---

## 🚀 Installation  

Install the project via `pip` inside the project folder:  

```bash
pip install .

✨ Features
Manage contacts: add, update, and delete phone numbers, emails, addresses, and birthdays
Track upcoming birthdays within a chosen number of days
Add, update, and delete notes for each contact
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
change [name] [old phone] [new phone]	Update an existing phone number
phone [name]	Show all phone numbers for a contact
delete [name] [phone number]	Delete a phone number
add-birthday [name] [DD.MM.YYYY]	Add a birthday
show-birthday [name]	Show a contact’s birthday
birthdays [days]	Show upcoming birthdays within [days]
add-email [name] [email]	Add an email address
change-email [name] [email]	Replace existing email with a new one
delete-email [name]	Delete email for the contact
remove-contact [name]	Fully remove a contact
add-address [name] [address]	Add a home address
change-adress [name] [new address]	Update a home address (note: spelling matches code)
find [query]	Search across all contacts
add-note [name] [note]	Add a note (each contact has one note)
change-note [name] [new note]	Update a contact’s note
delete-note [name]	Delete a contact’s note
search-note [query]	Search within all notes
add-tags [name] [#tag1 #tag2 ...]	Add tags to a note (replaces note content with tags list)

🧩 Example Use Cases
Remind your grandmother about upcoming birthdays
Store family members’ addresses, phone numbers, and emails
Keep a single note per contact (e.g., “Allergic to nuts” or “Loves gardening”)
Tag notes with labels like #health or #holiday for easier search
