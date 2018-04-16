from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

class StudentsScraper():
    def __init__(self):
                self.url = "https://www.collegedata.com/cs/admissions/admissions_tracker_result.jhtml?schoolId=436&classYear="
                titles = ["Profile", "Gender", "Type", "State", "UW", "W", "M", "CR","WT", "Rank", "ACT", "Status", "EA-ED", "Legacy","Athlete"]
                with open('../csv/Students.csv', 'w') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)                    
                    spamwriter.writerow(titles)
                    
                    
    def __download_html(self, url):
                browser = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Python\Python36-32\selenium\webdriver\geckodriver-v0.20.1-win64\geckodriver.exe')
                browser.get(url)
                WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.ID, "view_type")))
                browser.find_element_by_xpath("//*[@id='view_type']/option[text()='List View']").click()
                WebDriverWait(browser, 10).until(
                                                    EC.visibility_of_element_located((By.ID, "tableBodyWrap")))

                html_page = browser.page_source

                browser.quit()
                return html_page
            
    def __get_students(self, html_page):
                soup = BeautifulSoup(html_page, "html.parser")
                table = soup.find(id="profiles")

                thead = list(table.select("thead tr th div"))

                titles = [sp.get_text() if "Gender" not in sp.get_text() else "Gender" for sp in thead]
                
                tbody = list(table.select("tbody tr"))

                with open('../csv/Students.csv', 'a') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    #spamwriter.writerow(titles)
                    for tr in tbody:        
                        values = [td.get_text().replace('\n','').replace('\t','').replace('Save','').strip() if not td.find('img') else "Female" if "_female" in td.select("img")[0]['src'] else "Male" for td in tr.select("td")]
                        spamwriter.writerow(values)

    

    def scrape(self):
                    print ("Web Scraping of students' accepted in college data from " + \
                            "'" + self.url + "'...")
                    
                    # Download HTML
                    for x in range(2012, 2025):
                        html_page = self.__download_html(self.url+ str(x) )
                        self.__get_students(html_page)
                    
                    
                    
