# Password Manager

A Tkinter desktop app for generating, saving, and retrieving passwords. Credentials are stored locally in a JSON file keyed by website name. Generated passwords are copied to the clipboard automatically.

---

## Features

- Generates secure randomized passwords with a mix of letters, symbols, and numbers
- Copies generated passwords to the clipboard instantly via pyperclip
- Saves credentials (website, email, password) to a local `data.json` file
- Looks up saved credentials by website name and displays them in a dialog
- Validates that website and password fields are not empty before saving
- Pre-fills the email field with a default address for faster entry
- Clears website and password fields automatically after each save

---

## Requirements

- Python 3.8 or higher
- Tkinter (included with most Python installations)
- A `logo.png` image file in the same directory as `main.py`

Install dependencies:

```bash
pip install pyperclip
```

---

## Project Structure

```
.
├── main.py            # Full Tkinter UI, password generator, save, and search logic
├── password_gen.py    # Standalone CLI password generator (no UI)
├── logo.png           # Logo image displayed in the app canvas
└── data.json          # Generated on first save; stores all credentials
```

---

## Usage

```bash
python main.py
```

A window will open with three fields: Website, Email/Username, and Password.

| Action | How |
|---|---|
| Generate a password | Click "Generate Password" — fills the field and copies to clipboard |
| Save credentials | Fill in website and password, then click "Add" |
| Look up a saved entry | Type a website name and click "Search" |

---

## Data Storage

Credentials are written to `data.json` in the working directory. The file is created automatically on the first save. Each entry is keyed by website name:

```json
{
    "github.com": {
        "email": "you@example.com",
        "password": "aB3!kX9#mZ"
    }
}
```

If a website entry already exists, it is overwritten with the new values.

---

## Password Generation

Each generated password contains:

- 8 to 10 random letters (mixed case)
- 2 to 4 random symbols from `! # $ % & ( ) * +`
- 2 to 4 random digits

Characters are shuffled before joining, so the composition is not predictable from the output.

---

## Notes

- `data.json` is stored in plain text. Do not sync it to a public repository.
- The default email pre-filled in the form can be changed by updating the `email_entry.insert` line in `main.py`.
- `password_gen.py` is a standalone CLI script that prints a generated password without launching the UI. It can be run independently for quick password generation.
