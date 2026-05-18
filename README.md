# GrannyHelper 👵💙

GrannyHelper is a senior-friendly command-line personal assistant for managing contacts, birthdays, notes, and reminders.

The project is designed to provide a simple and accessible way to store important personal and family information using clear text commands.

---

## What This Project Does

GrannyHelper helps users manage:

- Contacts
- Phone numbers
- Emails
- Addresses
- Birthdays
- Personal notes
- Tags for notes
- Upcoming birthday reminders

The app works directly in the terminal and uses simple commands such as:

```text
add John 4165551234
phone John
add-birthday John 12.05.1990
add-note John Call every Sunday
birthdays 7
exit
```

---

## Why This Project Exists

Many personal assistant apps are overloaded with complex interfaces. GrannyHelper focuses on simplicity and usability.

The goal of this project is to create a basic assistant that can help older users store and find important information using a simple command-line interface.

This project also demonstrates practical Python development skills, including:

- Object-oriented programming
- Modular project structure
- Data validation
- Local data persistence
- Command-line application design
- Automated testing with pytest
- GitHub Actions CI
- Technical documentation

---

## Tech Stack

- Python
- Object-Oriented Programming
- Command-Line Interface
- File-based data persistence
- pytest
- GitHub Actions
- Git & GitHub

---

## Required Packages

The project uses a small number of Python packages.

### App packages

These packages are required to run GrannyHelper:

| Package          | Purpose                               |
| ---------------- | ------------------------------------- |
| `colorama`       | Adds colored messages in the terminal |
| `prompt-toolkit` | Improves command-line input           |
| `setuptools`     | Supports Python package installation  |

They are listed in:

```text
requirements.txt
```

### Developer packages

These packages are used for testing and development:

| Package  | Purpose              |
| -------- | -------------------- |
| `pytest` | Runs automated tests |

They are listed in:

```text
requirements-dev.txt
```

---

## Project Structure

```text
GrannyHelper/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── COMMANDS.md
├── source/
│   ├── __init__.py
│   ├── command_handlers/
│   │   ├── __init__.py
│   │   ├── handlers.py
│   │   └── input_error.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── address.py
│   │   ├── addressbook.py
│   │   ├── birthday.py
│   │   ├── field.py
│   │   ├── name.py
│   │   ├── notes.py
│   │   ├── phone.py
│   │   ├── record.py
│   │   ├── storage.py
│   │   └── user_email.py
│   └── main.py
├── tests/
│   └── test_models.py
├── .gitignore
├── helper.py
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── requirements-dev.txt
└── setup.py
```

---

## How to Run GrannyHelper

Follow these steps to run the bot on your computer.

---

### 1. Clone the repository

```bash
git clone https://github.com/DenysTryshkin/GrannyHelper.git
cd GrannyHelper
```

---

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

---

### 3. Activate the virtual environment

On macOS / Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

After activation, you should see `(.venv)` in the terminal.

Example:

```text
(.venv) user@computer GrannyHelper %
```

---

### 4. Install required packages

Install the packages needed to run the bot:

```bash
python -m pip install -r requirements.txt
```

---

### 5. Install developer packages

This step is needed if you want to run tests:

```bash
python -m pip install -r requirements-dev.txt
```

---

### 6. Run the bot

Run GrannyHelper from the project root:

```bash
python -m source.main
```

Important: do not run the app like this:

```bash
python source/main.py
```

Running the file directly may cause import errors because the app uses package-style imports from the `source` package.

---

## How to Use the Bot

After starting the app, you will see:

```text
Please, enter a command:
```

At this point, enter GrannyHelper commands, not terminal commands.

Example commands:

```text
hello
help
add John 4165551234
phone John
exit
```

To close the bot, type:

```text
exit
```

or:

```text
close
```

---

## Example Workflow

Start the app:

```bash
python -m source.main
```

Then enter these commands inside the bot:

```text
hello
add John 4165551234
add-email John john@example.com
add-birthday John 12.05.1990
add-note John Call every Sunday
phone John
birthdays 7
help
exit
```

---

## Main Commands

| Command          | Description                                     | Example                                   |
| ---------------- | ----------------------------------------------- | ----------------------------------------- |
| `hello`          | Start interacting with the assistant            | `hello`                                   |
| `help`           | Show available commands                         | `help`                                    |
| `add`            | Add a new contact with a phone number           | `add John 4165551234`                     |
| `phone`          | Show a contact phone number                     | `phone John`                              |
| `change-phone`   | Change a contact phone number                   | `change-phone John 4165551234 6475559999` |
| `delete-phone`   | Delete a phone number from a contact            | `delete-phone John 4165551234`            |
| `add-email`      | Add an email to a contact                       | `add-email John john@example.com`         |
| `change-email`   | Change a contact email                          | `change-email John new@example.com`       |
| `delete-email`   | Delete a contact email                          | `delete-email John`                       |
| `add-birthday`   | Add a birthday to a contact                     | `add-birthday John 12.05.1990`            |
| `show-birthday`  | Show a contact birthday                         | `show-birthday John`                      |
| `birthdays`      | Show upcoming birthdays within a number of days | `birthdays 7`                             |
| `add-address`    | Add an address to a contact                     | `add-address John Toronto`                |
| `change-address` | Change a contact address                        | `change-address John Ottawa`              |
| `delete-contact` | Delete a contact                                | `delete-contact John`                     |
| `find`           | Search contacts                                 | `find John`                               |
| `add-note`       | Add a note to a contact                         | `add-note John Call every Sunday`         |
| `change-note`    | Change a contact note                           | `change-note John Call every Monday`      |
| `delete-note`    | Delete a contact note                           | `delete-note John`                        |
| `search-note`    | Search notes by keyword                         | `search-note Sunday`                      |
| `add-tags`       | Add tags to a contact note                      | `add-tags John #family #important`        |
| `exit` / `close` | Save data and close the app                     | `exit`                                    |

For a full command reference, see:

```text
docs/COMMANDS.md
```

---

## Run Tests

To run the automated tests, first install developer dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Then run:

```bash
python -m pytest
```

Expected result:

```text
6 passed
```

---

## GitHub Actions CI

This project includes a GitHub Actions workflow that automatically runs tests on push and pull request events.

Workflow file:

```text
.github/workflows/ci.yml
```

---

## Roadmap

Planned improvements:

- Add SQLite or PostgreSQL database support
- Add Telegram bot integration
- Add a notification system
- Add multi-user support
- Improve error handling and validation
- Add a simple web interface
- Expand automated test coverage

---

## What This Project Demonstrates

- Python fundamentals
- Object-oriented programming
- Modular project architecture
- Data validation
- Local data persistence
- Command-line application design
- Automated testing with pytest
- GitHub Actions CI
- Technical documentation
- Git/GitHub workflow
- User-centered thinking

---

## Author

**Denys Tryshkin**

- GitHub: [github.com/DenysTryshkin](https://github.com/DenysTryshkin)
- LinkedIn: [linkedin.com/in/denys-tryshkin](https://www.linkedin.com/in/denys-tryshkin/)
