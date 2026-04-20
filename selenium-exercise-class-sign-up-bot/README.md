# Gym Class Auto-Booker

A Selenium script that automatically logs into a gym booking portal and reserves the next available Tuesday and Thursday 6:00 PM classes. After booking, it navigates to the "My Bookings" page and verifies each reservation was recorded correctly.

---

## Features

- Automatically calculates the upcoming Tuesday and Thursday dates at runtime
- Logs in with stored credentials and waits for the schedule page to load
- Detects the booking state of each target class: Book, Waitlist, Already Booked, or Already Waitlisted
- Books or joins the waitlist for each qualifying class and prints a status line per action
- Navigates to "My Bookings" and cross-references each result against the initial booking scan
- Persists a Chrome profile to disk so session state can be reused across runs

---

## Requirements

- Python 3.8 or higher
- Google Chrome
- ChromeDriver (matching your Chrome version)

Install Python dependencies:

```bash
pip install selenium numpy
```

---

## Configuration

Update the constants near the top of `main.py` before running:

```python
ACCOUNT_EMAIL    = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
GYM_URL          = "https://appbrewery.github.io/gym/"
```

The script targets 6:00 PM classes on the next Tuesday and Thursday relative to the current date. No additional date configuration is needed.

---

## Usage

```bash
python main.py
```

The browser will open, log in, book the classes, then navigate to "My Bookings" for verification. The Chrome window stays open after the script finishes (`detach` mode is enabled).

---

## Example Output

```
✅ Booked: Yoga Class on Tue, Jun 03 at 6:00 PM
⏳ Joined waitlist for: Spin Class on Thu, Jun 05 at 6:00 PM

--- VERIFICATION RESULT ---
✅ Verified Booked for Yoga Class on Tue Jun 03 at 06:00 PM
✅ Verified Waitlisted for Spin Class on Thu Jun 05 at 06:00 PM
```

---

## How It Works

1. Calculates the next Tuesday and Thursday dates and builds button ID suffixes in the format `YYYY-MM-DD-1800`
2. Logs into the gym portal using the provided credentials
3. Scans all elements matching `[id^='book-button-']` and filters for Tuesday and Thursday 6 PM slots
4. Reads each button's current text to determine action: `Book Class`, `Join Waitlist`, `Booked`, or `Waitlisted`
5. Clicks each button and records the class type, date, and resulting status in a dictionary
6. Navigates to "My Bookings" and matches each found card against the dictionary by class name, date, and status
7. Prints a verified or unmatched result line for each booking card

---

## Notes

- The Chrome profile is saved to a `chrome_profile/` folder in the working directory. Delete this folder to start a fresh session.
- The `WebDriverWait` timeout is set to 2 seconds. Increase this value if the target site loads slowly.
- Credential constants are stored in plain text. For production use, load them from environment variables or a secrets manager instead.
