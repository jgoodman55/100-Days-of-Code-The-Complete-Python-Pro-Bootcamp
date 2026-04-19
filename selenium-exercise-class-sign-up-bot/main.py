#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import numpy as np
from datetime import datetime, timedelta
import os


# Add your credentials at the top of your script
ACCOUNT_EMAIL = "baldyjordan@gmail.com"  # The email you registered with
ACCOUNT_PASSWORD = "GymTanCode1!"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

TODAY = datetime.today().strftime("%Y-%m-%d")  # Get today's date in YYYY-MM-DD format
CURRENT_YEAR = datetime.today().year

#TUESDAY
NEXT_TUESDAY_DATE = (datetime.today() + timedelta((1 - datetime.today().weekday()) % 7))
NEXT_TUESDAY = NEXT_TUESDAY_DATE.strftime("%Y-%m-%d")  # Get the next Tuesday's date in YYYY-MM-DD format
NEXT_TUESDAY_6PM = f"{str(NEXT_TUESDAY)}-1800"  # Format the button ID for Tuesday at 6 PM

# THURSDAY
NEXT_THURSDAY_DATE = (datetime.today() + timedelta((3 - datetime.today().weekday()) % 7))
NEXT_THURSDAY = NEXT_THURSDAY_DATE.strftime("%Y-%m-%d")  # Get the next Thursday's date in YYYY-MM-DD format
NEXT_THURSDAY_6PM = f"{str(NEXT_THURSDAY)}-1800"  # Format the button ID for Thursday at 6 PM


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)
login_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
login_button.click()

email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

book_buttons = driver.find_elements(By.CSS_SELECTOR, "[id^='book-button-']")

classes_booked = 0
classes_waitlisted = 0
already_booked_waitlisted = 0
total_6pm_classes = 0

detailed_class_list = []

booked_classes_dict = {}

for button in book_buttons:
    button_id = button.get_attribute("id")
    if button_id.endswith(NEXT_TUESDAY_6PM) or button_id.endswith(NEXT_THURSDAY_6PM):
        class_date = datetime.strptime("-".join(button_id.split("-")[3:6]), "%Y-%m-%d")
        class_date_str = class_date.strftime("%a, %b %d")

        class_date_time = datetime.strptime("-".join(button_id.split("-")[3:7]), "%Y-%m-%d-%H%M")
        class_date_time_str = class_date_time.strftime("%Y-%m-%d-%H-%M")
        
        button_text = button.text
        button.click()

        class_type = button_id.split("-")[2].title()

        booking_key = f"{class_type.lower()}-{class_date_time_str}"
        booked_classes_dict[booking_key] = {"date": class_date_str, "status": ""}

        if button_text == "Booked":
            book_status = "✅ Already booked: "
            booked_classes_dict[booking_key]["status"] = "Booked"
            already_booked_waitlisted += 1
        elif button_text == "Waitlisted":
            book_status = "⏳ Already on waitlist: "
            booked_classes_dict[booking_key]["status"] = "Waitlisted"
            already_booked_waitlisted += 1
        elif button_text == "Join Waitlist":
            book_status = "⏳ Joined waitlist for: "
            detailed_class_list.append(f"• [New Waitlist] {class_type} Class on {class_date_str} at 6:00 PM")
            booked_classes_dict[booking_key]["status"] = "Waitlisted"
            classes_waitlisted += 1
        elif button_text == "Book Class":
            book_status = "✅ Booked: "
            detailed_class_list.append(f"• [New Booking] {class_type} Class on {class_date_str} at 6:00 PM")
            booked_classes_dict[booking_key]["status"] = "Booked"
            classes_booked += 1
        total_6pm_classes += 1
        msg = f"{book_status}{class_type} Class on {class_date_str} at 6:00 PM"
        print(msg)

# summary = f"""\n--- BOOKING SUMMARY ---
# New bookings: {classes_booked}
# New waitlist entries: {classes_waitlisted}
# Already booked/waitlisted: {already_booked_waitlisted}
# Total Tuesday & Thursday 6pm classes: {total_6pm_classes}\n"""
# print(summary)

# detailed_class_list_str = "\n".join(detailed_class_list)
# print(f"--- DETAILED CLASS LIST ---\n{detailed_class_list_str}")
bookings_page_dict = {}
found_bookings = 0
print("\n--- VERIFICATION RESULT ---")
my_bookings_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My Bookings")))
my_bookings_button.click()
try:
    bookings = driver.find_elements(By.CSS_SELECTOR, "[id^='booking-card-booking'], [id^='waitlist-card-waitlist']")
    for booking in bookings:
        # booking_id = booking.get_attribute("id")
        booking_class_name = booking.find_element(By.CSS_SELECTOR, "h3").text.split()[0].lower()
        booking_class_date = booking.find_element(By.CSS_SELECTOR, "p").text.split("When: ")[1]
        formatted_date = datetime.strptime(f'{CURRENT_YEAR}, {booking_class_date}', '%Y, %a, %b %d, %I:%M %p').strftime('%a %b %d at %I:%M %p')
        booking_class_button = booking.find_element(By.CSS_SELECTOR, "button").text
        booking_class_status = 'Booked' if booking_class_button == 'Cancel Booking' else 'Waitlisted'
        dict_key = f"{booking_class_name}-{datetime.strptime(f'{CURRENT_YEAR}, {booking_class_date}', '%Y, %a, %b %d, %I:%M %p').strftime('%Y-%m-%d-%H-%M')}"
        # print(f"Found booking: {booking_class_name} on {booking_class_date} with status {booking_class_button}")
        # search booked_classes_dict and find match
        if booked_classes_dict.get(dict_key) and booked_classes_dict.get(dict_key).get("status") == booking_class_status:
            print(f"✅ Verified {booking_class_status} for {booking_class_name.title()} Class on {formatted_date}")
            found_bookings += 1
        else:
            print(f"❌ Booking not found in initial scan for {booking_class_name.title()} Class on {formatted_date} with status {booking_class_status}")

except NoSuchElementException:
    print(f'Expected: {total_6pm_classes} bookings')
    print('Found: 0 bookings')
    pass


