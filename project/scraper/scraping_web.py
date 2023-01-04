# library
import requests
import json
from bs4 import BeautifulSoup


class CreateAttachment():
    def __init__(self, target_link):
    
        self.target_link = target_link
        self.scrape_result = self.scrape_site()
    
    def scrape_site(self):
        html_text = requests.get(self.target_link).text
        soup = BeautifulSoup(html_text, 'html.parser')
        latest_notification = soup.select_one('#sub > div > div.board_container > table > tbody > tr:nth-child(1)')
        return latest_notification

    def attachment(self):
        new_noti_number = (self.scrape_result.find(class_="body_col_number dn1").text).strip()
        new_noti_title = (self.scrape_result.find('a').text).strip()
        new_noti_link = (self.scrape_result.find('a'))['href']
        new_noti_date = (self.scrape_result.find(class_="body_col_regdate dn5").text).strip()
        
        attach_dict = {
            'color' : '#ff0000',
            'author_name' : 'Slack Bot Notice',
            'title' : new_noti_title,
            'title_link' : self.target_link+new_noti_link,
            'date' : new_noti_date,
        }
        return attach_dict


# main
if __name__=="__main__":
    target_link = json.load(open('../configuration.json', 'r'))['object_1']['target_link']
    myObject = CreateAttachment(target_link)
    print(myObject.attachment())