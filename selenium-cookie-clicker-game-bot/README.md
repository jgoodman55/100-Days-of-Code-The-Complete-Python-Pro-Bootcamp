# Cookie Clicker Bot

A Selenium bot that plays Cookie Clicker autonomously for a set duration. It clicks the big cookie continuously, monitors available upgrades, and always purchases the highest-priced unlocked upgrade to maximize cookies per second.

---

## Features

- Selects the English language on startup automatically
- Clicks the big cookie in a continuous loop for a configurable duration
- Scans for unlocked and enabled upgrades after each click
- Purchases the most expensive available upgrade using NumPy's `argmax`
- Prints the final cookies-per-second rate on exit
- Leaves the browser open after the run completes

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

Two values at the top of `main.py` can be adjusted before running:

```python
duration = 5 * 60   # Total run time in seconds (default: 5 minutes)
URL      = "https://ozh.github.io/cookieclicker/"
```

---

## Usage

```bash
python main.py
```

The browser will open Cookie Clicker, dismiss the language modal, and begin clicking. After the duration expires, the final cookies-per-second value is printed and the browser closes.

---

## Example Output

```
Loop started. It will run for 5 minutes.
Best upgrade: Cursor  x1  15
Best upgrade: Grandma  x1  100
Best upgrade: Cursor  x7  112
...
cookies/second : 4.5
```

---

## How It Works

1. Opens the Cookie Clicker URL and clicks the English language option
2. Locates the big cookie element and enters a timed `while` loop
3. On each iteration, clicks the cookie and reads the current cookie count
4. Finds all elements matching `.product.unlocked.enabled` (available upgrades)
5. Parses the price from each upgrade, strips commas, and converts to integers
6. Uses `np.argmax` to identify the highest-priced upgrade and clicks it
7. Skips the upgrade step silently if no prices can be parsed
8. After the loop exits, reads and prints the cookies-per-second display value

---

## Notes

- The bot targets the highest-priced upgrade rather than the most cost-efficient one. For a more optimized strategy, consider purchasing the upgrade with the best cookies-per-second-per-cost ratio instead.
- The `WebDriverWait` poll frequency is set to 5 seconds inside the loop, which limits how fast the cookie is clicked. Lower this value for a faster run.
- The Chrome window stays open after the script exits (`detach` mode is enabled).
