from selenium.common.exceptions import NoSuchElementException

url = "https://merolagani.com/CompanyDetail.aspx?symbol=GBIME#0"
driver = webdriver.Chrome()  # Create a Chrome driver
driver.get(url)  # Open the URL in the browser

all_data = []  # Store data from all pages

while True:
    # Click on the element that loads the content (if applicable)
    # Find the "Price History" tab each time in the loop
    price_history_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab'))
    )
    price_history_tab.click()


    # You might need to introduce a delay here to ensure the content has loaded before fetching the HTML
    time.sleep(3)  # Adjust the delay as needed

    # Get the HTML content after the elements are loaded
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")  # Parse the HTML with BeautifulSoup
    table = soup.find("table", class_="table-bordered")  # Find the table element

    each_row = table.find_all('tr')
    # extract td tag text from each row excluding first row
    data = []
    for row in each_row[1:]:
        td = row.find_all('td')
        row_data = [row.text for row in td]
        data.append(row_data)
    
    all_data.extend(data)  # Add the data from the current page to all_data

    try:
        # Find and click the "Next" button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@title="Next Page"]'))
        )
        next_button.click()
    except NoSuchElementException:
        break  # Break the loop if the "Next" button is not found

driver.quit()  # Close the browser

# Convert the collected data to a DataFrame
df = pd.DataFrame(all_data, columns=["SN","Date", "LTP", "%change", "High", "Low", "Open","Qty.", "Turnover"])

# Convert the DataFrame to a CSV file
df.to_csv("stock_price.csv", index=False)
