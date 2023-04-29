from bs4 import BeautifulSoup
import requests, openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
main_url = 'https://doctor.webmd.com/results?q=Family%20Medicine&sids=29259&pagenumber=1&d=16&rd=16&sortby=bestmatch&extractionname=Family%20Medicine&extractiontype=specialty&medicare=false&medicaid=false&newpatient=false&isvirtualvisit=false&minrating=0&entity=practice&hospPromo=false&pt=45.544,-122.639&city=Portland&state=OR'

browser = webdriver.Chrome(executable_path=r'C:/Users/bheema/anaconda3/Lib/site-packages/chromedriver_py/chromedriver_win32.exe')
source= browser.get(main_url)

'''excel = openpyxl.Workbook()
print(excel.sheetnames)

sheet = excel.active
sheet.title = 'Houzz latest details'
print(excel.sheetnames)
sheet.append(['Business Name','Phone Number','Hozz Url','Website Url','Facebook Link'])'''

try:
    soup = BeautifulSoup(source.text,'html.parser')
    
    details = soup.find('ul', class_ = "resultslist-content").find('div',class_= "webmd-card__body")


    
    for link in details:
        url = link.find('h4',class_="title").find("a")
        print(url)
        break
        # page = requests.get(url)
        # soup1 = BeautifulSoup(page.content, 'html.parser')
            
        # business_details = soup1.find('main', {"class":"sc-183mtny-0 jXcpx"}).find("section",{"id":"business"}).find_all("p", {"class": "sc-mwxddt-0 cZJFpr"}):
        # print(business_details.get_text())
    #   p_tags = business_details.find('div',class_='sc-183mtny-0 sc-1wm9uar-0 bmFdUT eFNJDl hui-grid').find('p',class_='mwxddt')

    #         left_div_list = [div for div in business_details.find_all('div', class_="sc-183mtny-0 sc-1uw6j8i-0 BusinessDetails__StyledCell-sc-1iscszt-0 dYJOPh ecpWHO gRCcss hui-cell")]
    #         left_p_list = [div.find_all('p') for div in left_div_list]
    #         left_content = [item.text.strip() for p in left_p_list for item in p]
    #         facebook_link = business_details.find("a",{"aria-label":"Find me on Facebook"})
            
    #         if facebook_link:
    #             facebook_link = business_details.find("a",{"aria-label":"Find me on Facebook"}).get('href')
                
        # else:
    #              left_content.append('No FB Link')  
            
    #         business_name = left_content[0]
    #         phone_number = left_content[1]
    #         Hozz_url = url
    #         website_url = left_content[2]
            
            
    #         print (business_name,phone_number,Hozz_url,website_url,facebook_link)
    #         #sheet.append([business_name,phone_number,Hozz_url,website_url,facebook_link])

            
    
    #         #excel.save('IMDB Movie Rating.xlsx')               
        # except Exception as inner_exp:
            # print(inner_exp)
    
except Exception as e:
    print(e)


