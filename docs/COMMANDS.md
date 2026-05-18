# GrannyHelper Commands

This document describes the main commands available in the GrannyHelper command-line assistant.

---

## General Commands

| Command          | Description                 | Example |
| ---------------- | --------------------------- | ------- |
| `help`           | Show available commands     | `help`  |
| `hello`          | Show greeting message       | `hello` |
| `exit` / `close` | Save data and close the app | `exit`  |

---

## Contact Commands

| Command          | Description                           | Example                                   |
| ---------------- | ------------------------------------- | ----------------------------------------- |
| `add`            | Add a new contact with a phone number | `add John 4165551234`                     |
| `phone`          | Show phone number for a contact       | `phone John`                              |
| `change-phone`   | Change a contact phone number         | `change-phone John 4165551234 6475559999` |
| `delete-phone`   | Delete a phone number from a contact  | `delete-phone John 4165551234`            |
| `delete-contact` | Delete a contact                      | `delete-contact John`                     |
| `find`           | Search for a contact                  | `find John`                               |

---

## Email Commands

| Command        | Description            | Example                             |
| -------------- | ---------------------- | ----------------------------------- |
| `add-email`    | Add email to a contact | `add-email John john@example.com`   |
| `change-email` | Change contact email   | `change-email John new@example.com` |
| `delete-email` | Delete contact email   | `delete-email John`                 |

---

## Birthday Commands

| Command           | Description                                     | Example                           |
| ----------------- | ----------------------------------------------- | --------------------------------- |
| `add-birthday`    | Add birthday to a contact                       | `add-birthday John 12.05.1990`    |
| `change-birthday` | Change birthday for a contact                   | `change-birthday John 15.06.1991` |
| `show-birthday`   | Show birthday for a contact                     | `show-birthday John`              |
| `birthdays`       | Show upcoming birthdays within a number of days | `birthdays 7`                     |

---

## Address Commands

| Command          | Description              | Example                      |
| ---------------- | ------------------------ | ---------------------------- |
| `add-address`    | Add address to a contact | `add-address John Toronto`   |
| `change-address` | Change contact address   | `change-address John Ottawa` |

---

## Notes Commands

| Command       | Description             | Example                              |
| ------------- | ----------------------- | ------------------------------------ |
| `add-note`    | Add a note to a contact | `add-note John Call every Sunday`    |
| `change-note` | Change a contact note   | `change-note John Call every Monday` |
| `delete-note` | Delete a contact note   | `delete-note John`                   |
| `search-note` | Search notes by keyword | `search-note Sunday`                 |
| `add-tags`    | Add tags to a note      | `add-tags John #family #important`   |

---

## Example Workflow

```text
add John 4165551234
add-email John john@example.com
add-birthday John 12.05.1990
add-note John Call every Sunday
phone John
birthdays 7
help
exit
```
