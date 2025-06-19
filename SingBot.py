from seleniumbase import SB
import time

# URL variable for inline.app booking
INLINE_URL = "https://inline.app/booking/-N_1xDQeMXaa3du_tCti:inline-live-3"

def main():
    with SB(test=True, uc=True) as sb:
        sb.open(INLINE_URL)
        last_url = ""
        
        while True:
            current_url = sb.get_current_url()
            
            if current_url != last_url:
                url_parts = current_url.split('/')
                
                if "/booking/" in current_url and url_parts[-1] != "form":
                    try:
                        # Set adult picker to 3
                        if sb.is_element_visible("#adult-picker"):
                            sb.select_option_by_value("#adult-picker", "3")
                        
                        # Select date by keyword 6月19
                        if sb.is_element_visible('#date-picker'):
                            sb.click('#date-picker')
                        
                        # Select first time slot (leftmost) for 6月19日
                        if sb.is_element_visible('button[aria-label*="2025-06-19"]'):
                            sb.click('button[aria-label*="2025-06-19"]:first-of-type')
                    except Exception as e:
                        print(f"Error in booking mode: {e}")
                    
                elif url_parts[-1] == "form":
                    try:
                        # Fill form mode
                        if sb.is_element_visible("#familyName"):
                            sb.type("#familyName", "pang")
                        if sb.is_element_visible("#givenName"):
                            sb.type("#givenName", "chiu sing")
                        if sb.is_element_visible('span:contains("先生")'):
                            sb.click('span:contains("先生")')
                        if sb.is_element_visible('select[name="country-code"]'):
                            sb.select_option_by_text('select[name="country-code"]', "Hong Kong +852")
                        if sb.is_element_visible("#phone"):
                            sb.type("#phone", "67034350")
                        if sb.is_element_visible("#email"):
                            sb.type("#email", "sing062911@gmail.com")
                        # Card number iframe
                        if sb.is_element_visible('#card-number iframe'):
                            sb.switch_to_frame('#card-number iframe')
                            sb.type("input", "4111111111111111")
                            sb.switch_to_default_content()
                        # Card expiry iframe
                        if sb.is_element_visible('#card-expiry iframe'):
                            sb.switch_to_frame('#card-expiry iframe')
                            sb.type("#cc-exp", "12/25")
                            sb.switch_to_default_content()
                        # Card security code iframe
                        if sb.is_element_visible('#card-security-code iframe'):
                            sb.switch_to_frame('#card-security-code iframe')
                            sb.type("#cc-ccv", "123")
                            sb.switch_to_default_content()
                        if sb.is_element_visible("#cardholder-name"):
                            sb.type("#cardholder-name", "sing")
                        if sb.is_element_visible('label[for="deposit-policy"]'):
                            sb.click('label[for="deposit-policy"]')
                    except Exception as e:
                        print(f"Error in form mode: {e}")
                
                last_url = current_url
                
            time.sleep(1)

if __name__ == "__main__":
    main()