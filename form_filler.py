"""
Google Form Automation Script using Selenium
Fills the form and captures screenshot of confirmation page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import os

# Load configuration
def load_config():
    """Load personal details from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def setup_driver():
    """Setup Chrome WebDriver with options"""
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Uncomment for headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def fill_google_form(driver, data):
    """Fill the Google Form with provided data - Using direct field selection"""
    
    # Navigate to the form
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"
    driver.get(form_url)
    
    # Wait for form to load
    wait = WebDriverWait(driver, 15)
    time.sleep(3)
    
    print("\n=== FILLING FORM ===\n")
    
    try:
        # Get all visible text inputs (excluding hidden ones)
        all_text_inputs = driver.find_elements(By.XPATH, "//input[@type='text' and not(@name)]")
        
        # Filter only visible inputs
        visible_inputs = [inp for inp in all_text_inputs if inp.is_displayed()]
        
        print(f"Found {len(visible_inputs)} visible text input fields")
        
        # Based on the form structure:
        # visible_inputs[0] = Full Name
        # visible_inputs[1] = Contact Number
        # visible_inputs[2] = Email ID
        # Textarea = Full Address
        # visible_inputs[3] = Pin Code
        # Date field = Date of Birth
        # visible_inputs[4] = Gender (text input)
        # visible_inputs[5] = CAPTCHA Code
        
        # 1. Full Name - First visible text input
        print("1. Filling Full Name...")
        if len(visible_inputs) > 0:
            visible_inputs[0].clear()
            visible_inputs[0].send_keys(data['full_name'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 2. Contact Number - Second visible text input
        print("2. Filling Contact Number...")
        if len(visible_inputs) > 1:
            visible_inputs[1].clear()
            visible_inputs[1].send_keys(data['contact_number'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 3. Email ID - Third visible text input
        print("3. Filling Email ID...")
        if len(visible_inputs) > 2:
            visible_inputs[2].clear()
            visible_inputs[2].send_keys(data['email'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 4. Full Address - Textarea
        print("4. Filling Full Address...")
        address_field = driver.find_element(By.XPATH, "//textarea")
        address_field.clear()
        address_field.send_keys(data['address'])
        time.sleep(0.5)
        print("   ✓ Done")
        
        # 5. Pin Code - Fourth visible text input
        print("5. Filling Pin Code...")
        if len(visible_inputs) > 3:
            visible_inputs[3].clear()
            visible_inputs[3].send_keys(data['pin_code'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 6. Date of Birth - Date input
        print("6. Filling Date of Birth...")
        date_field = driver.find_element(By.XPATH, "//input[@type='date']")
        date_field.clear()
        date_field.send_keys(data['dob'])
        time.sleep(0.5)
        print("   ✓ Done")
        
        # 7. Gender - Fifth visible text input
        print("7. Filling Gender...")
        if len(visible_inputs) > 4:
            visible_inputs[4].clear()
            visible_inputs[4].send_keys(data['gender'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 8. CAPTCHA Code - Sixth visible text input
        print("8. Filling CAPTCHA code...")
        if len(visible_inputs) > 5:
            visible_inputs[5].clear()
            visible_inputs[5].send_keys(data['captcha_code'])
            time.sleep(0.5)
            print("   ✓ Done")
        
        # 9. Submit the form
        print("9. Submitting form...")
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']/parent::*"))
        )
        submit_button.click()
        time.sleep(0.5)
        print("   ✓ Done")
        
        # Wait for confirmation page
        print("10. Waiting for confirmation...")
        time.sleep(4)
        
        print("\n✓ Form filled successfully!\n")
        return True
        
    except Exception as e:
        print(f"\n✗ Error filling form: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return False

def capture_screenshot(driver, filename='screenshots/confirmation.png'):
    """Capture screenshot of the confirmation page"""
    
    # Create screenshots directory if it doesn't exist
    os.makedirs('screenshots', exist_ok=True)
    
    try:
        # Wait for confirmation message
        wait = WebDriverWait(driver, 10)
        try:
            confirmation = wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'submitted') or contains(text(), 'response') or contains(text(), 'recorded')]"))
            )
            print("✓ Confirmation page detected")
        except:
            print("⚠ Could not find confirmation message, but taking screenshot anyway")
        
        # Take screenshot
        driver.save_screenshot(filename)
        print(f"✓ Screenshot saved: {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error capturing screenshot: {str(e)}")
        # Take screenshot anyway
        driver.save_screenshot(filename)
        return False

def main():
    """Main execution function"""
    
    print("=" * 60)
    print("       GOOGLE FORM AUTOMATION SCRIPT")
    print("=" * 60)
    
    # Load configuration
    print("\n[Step 1/4] Loading configuration...")
    config = load_config()
    print(f"✓ Loaded config for: {config['full_name']}")
    
    # Setup driver
    print("\n[Step 2/4] Setting up Chrome driver...")
    driver = setup_driver()
    print("✓ Chrome driver ready")
    
    try:
        # Fill the form
        print("\n[Step 3/4] Filling the form...")
        success = fill_google_form(driver, config)
        
        if success:
            # Capture screenshot
            print("[Step 4/4] Capturing screenshot...")
            capture_screenshot(driver)
            
            print("\n" + "=" * 60)
            print("       ✓ PROCESS COMPLETED SUCCESSFULLY!")
            print("=" * 60)
            print("\nNext step: Run 'python email_sender.py' to send submission")
        else:
            print("\n" + "=" * 60)
            print("       ✗ FAILED TO FILL THE FORM")
            print("=" * 60)
            
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Keep browser open for a moment to see result
        print("\nKeeping browser open for 10 seconds so you can see the result...")
        time.sleep(10)
        driver.quit()
        print("Browser closed.\n")

if __name__ == "__main__":
    main()