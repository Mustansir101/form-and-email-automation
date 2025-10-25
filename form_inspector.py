"""
Simple Form Inspector - Just opens the form and shows all fields
Run this first to understand the form structure
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def inspect_form(driver):
    """Open form and print all field information"""
    
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"
    print(f"Opening form: {form_url}\n")
    driver.get(form_url)
    
    # Wait for page to load
    time.sleep(4)
    
    print("=" * 80)
    print("FORM FIELD INSPECTOR")
    print("=" * 80)
    
    # Find all input fields
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\n📝 TEXT/INPUT FIELDS ({len(inputs)} found):\n")
    print("-" * 80)
    
    for i, inp in enumerate(inputs):
        try:
            input_type = inp.get_attribute("type") or "unknown"
            aria_label = inp.get_attribute("aria-label") or "NO LABEL"
            aria_desc = inp.get_attribute("aria-describedby") or ""
            name = inp.get_attribute("name") or ""
            data_params = inp.get_attribute("data-params") or ""
            
            print(f"Field #{i+1}:")
            print(f"  Type: {input_type}")
            print(f"  Label: {aria_label}")
            if name:
                print(f"  Name: {name}")
            if aria_desc:
                print(f"  Description: {aria_desc}")
            print()
        except Exception as e:
            print(f"  Error reading field: {e}\n")
    
    # Find all textareas
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    print(f"\n📋 TEXTAREA FIELDS ({len(textareas)} found):\n")
    print("-" * 80)
    
    for i, ta in enumerate(textareas):
        try:
            aria_label = ta.get_attribute("aria-label") or "NO LABEL"
            name = ta.get_attribute("name") or ""
            
            print(f"Textarea #{i+1}:")
            print(f"  Label: {aria_label}")
            if name:
                print(f"  Name: {name}")
            print()
        except Exception as e:
            print(f"  Error reading textarea: {e}\n")
    
    # Find radio buttons and dropdowns
    radios = driver.find_elements(By.XPATH, "//div[@role='radio']")
    print(f"\n🔘 RADIO BUTTONS ({len(radios)} found):\n")
    print("-" * 80)
    
    for i, radio in enumerate(radios):
        try:
            text = radio.text or "NO TEXT"
            aria_label = radio.get_attribute("aria-label") or ""
            
            print(f"Radio #{i+1}:")
            print(f"  Text: {text}")
            if aria_label:
                print(f"  Label: {aria_label}")
            print()
        except Exception as e:
            print(f"  Error reading radio: {e}\n")
    
    # Find all spans that might be labels
    print(f"\n🏷️  FORM QUESTIONS (Labels):\n")
    print("-" * 80)
    
    questions = driver.find_elements(By.XPATH, "//div[@role='heading']")
    for i, q in enumerate(questions):
        try:
            text = q.text or "NO TEXT"
            if text and len(text) > 2:  # Skip empty or very short texts
                print(f"Question #{i+1}: {text}")
        except:
            pass
    
    print("\n" + "=" * 80)
    print("INSPECTION COMPLETE")
    print("=" * 80)
    print("\nBrowser will stay open for 30 seconds...")
    print("You can manually scroll and see the form structure.")
    time.sleep(30)

def main():
    print("\n🔍 Starting Form Inspector...\n")
    
    driver = setup_driver()
    
    try:
        inspect_form(driver)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()
        print("\n✅ Browser closed.")

if __name__ == "__main__":
    main()