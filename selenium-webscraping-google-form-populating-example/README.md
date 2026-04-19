# Zillow Property Scraper and Form Submitter

Scrapes rental property listings from a Zillow clone and automatically submits each listing (address, price, and URL) to a Google Form using Selenium. Built with Python, Requests, BeautifulSoup, and Selenium WebDriver.

---

## Features

- Scrapes property address, price, and listing URL from the target page
- Retries failed HTTP requests with configurable backoff
- Reuses a single Chrome WebDriver session across all form submissions
- Targets the Google Form submit button by `aria-label` to avoid navigation conflicts
- Waits for a confirmation element before moving to the next submission
- Supports headless or visible browser mode

---

## Requirements

- Python 3.8 or higher
- Google Chrome
- ChromeDriver (matching your Chrome version)

Install Python dependencies:

```bash
pip install requests beautifulsoup4 selenium
```

---

## Project Structure

```
.
└── main.py       # All scraping and form submission logic
```

---

## Configuration

At the top of `main.py`, update these two constants to point at your target page and form:

```python
ZILLOW_URL   = "https://appbrewery.github.io/Zillow-Clone"
GOOGLE_FORM  = "https://forms.gle/UFFPE1hV5qDkmfTZ7"
```

To run the browser invisibly, change the `create_driver` call in the main block:

```python
driver = create_driver(headless=True)
```

---

## Usage

```bash
python main.py
```

The script will:

1. Fetch the Zillow clone page and parse all property cards
2. Open Chrome and navigate to the Google Form
3. Fill in the address, price, and link fields for each property
4. Click Submit and wait for the confirmation message
5. Pause briefly between submissions, then repeat for all properties
6. Quit the browser when finished (or if an error occurs)

Sample output:

```
Found 12 properties. Submitting forms...

[1/12] 183 Corsair Alley, New Hampshire — $1,399
  Submitted
[2/12] 54 Browning Street, Nevada — $2,050
  Submitted
...

Done.
```

---

## Key Functions

| Function | Description |
|---|---|
| `fetch_with_retry` | GET request with configurable retry count and backoff |
| `get_address` | Extracts and cleans the address from a property card |
| `get_price` | Extracts the price using a regex pattern |
| `get_link` | Extracts the listing URL from a property card |
| `create_driver` | Initializes a Chrome WebDriver with optional headless mode |
| `fill_and_submit_form` | Navigates to the form, populates fields, submits, and confirms |

---

## Notes

- The script targets input fields by `input[type="text"]` and the submit button by `aria-label="Submit"`. If the Google Form layout changes, these selectors may need to be updated.
- A 1-second pause between submissions helps avoid rate limiting.
- All three values (address, price, link) must be present in the form for `zip` to populate correctly. If your form has a different field count, adjust accordingly.

---

## License

MIT
