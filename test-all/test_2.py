import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Adjust implicit wait time if needed
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password", [
    ("afiahR", "12345"),  # Example valid credentials
    ("user2", "pass2"),   # Invalid credentials
    ("butter", "butter"),  # Example valid credentials
    ("butter", "pass2"),   # Valid username, wrong password
    ("testing", "testing"),  # Example valid credentials
    ("user2", "wrongpass"),   # Invalid credentials
    ("test2", "test2"),  # Example valid credentials
    ("wronguser", "wrongpass"),  # Invalid credentials
    ("toffee", "cat1"),  # Example valid credentials
    ("invalid", "invalid"),  # Invalid credentials
])
def test_login(driver, username, password):
    driver.get("http://127.0.0.1:8000/login/")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-custom")
    
    # Enter credentials
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    # Wait for a success or error condition
    success_url = "http://127.0.0.1:8000/"
    is_success = WebDriverWait(driver, 10).until(
        lambda d: d.current_url == success_url or 
                  d.find_elements(By.CSS_SELECTOR, ".error-message")
    )

    if driver.current_url == success_url:
        assert is_success, f"Expected success but failed for credentials: {username} {password}"
    else:
        assert any("Invalid" in e.text or "error" in e.text.lower() 
                   for e in driver.find_elements(By.CSS_SELECTOR, ".error-message")), \
            f"Expected error but passed for credentials: {username} {password}"

# Test Sign-Up Functionality
@pytest.mark.parametrize("username, password", [
    ("hR", "123456"),  # Example valid details
    ("hurRy", "126"),  # Example valid details
    ("", "126"),  # Example invalid details
])
def test_signup(driver, username, password):
    driver.get("http://127.0.0.1:8000/signup/")  # Replace with your sign-up page URL
    
    # Locate form fields and submit button
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-custom")
    
    # Fill out the form
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    
    # Wait for success redirection
    success_url = "http://127.0.0.1:8000/login/"  # Replace with expected redirect URL after sign-up
    WebDriverWait(driver, 10).until(EC.url_to_be(success_url))
    
    # Assertions
    print(f"Sign-Up passed for: {username}, {password}")
    assert driver.current_url == success_url, f"Sign-Up failed for: {username}, {password}"

@pytest.mark.parametrize("search_term", ["k", "cafe", "unavailable", ""])  # Add more search terms as needed
def test_search_with_multiple_queries(search_term):
    # Setup WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(898, 574)
    
    try:
        # Navigate to the search page
        driver.get("http://127.0.0.1:8000/search/")  # Directly open the search page
    
        # Step 1: Locate the search box
        search_box = driver.find_element(By.NAME, "query")
        search_box.click()
    
        # Step 2: Perform a search query
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)
    
        # Step 3: Wait for the search results page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".restaurant-card"))  # Update selector if needed
            )
        except Exception as e:
            print(f"Warning: Timeout occurred for query '{search_term}'.")
        
        # Step 4: Collect search results
        result_elements = driver.find_elements(By.CSS_SELECTOR, ".restaurant-card")  # Update selector if needed
        results = [result.text for result in result_elements]
    
        # Debugging Log
        print(f"Search results for '{search_term}': {results}")
    
        # Step 5: Assertions to validate search results
        if search_term == "":
            assert len(results) == 0, "Expected no results for an empty search query."
            print(f"Test passed for empty search query: No results found.")
        else:
            if search_term == "unavailable":  # Adjust for known cases
                assert len(results) == 0, f"Expected no results for unavailable query: '{search_term}'."
            else:
                assert len(results) > 0, f"No results found for search query: '{search_term}'"
    
    finally:
        # Teardown WebDriver
        driver.quit()

