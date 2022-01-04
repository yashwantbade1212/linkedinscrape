from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Creating a webdriver instance
driver = webdriver.Chrome(executable_path=r'C:/Users\91976\OneDrive\Desktop\Phoenixgen\chromedriver.exe')
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("Yashwantbade1212@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("Yashwant@#$%^&*1212")

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']

driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/prashantmane/"

driver.get(profile_url)  # this will open the link



start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll}) ")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break



src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')
# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'mt2 relative'})
intro=intro.get_text().strip()
print(intro)
