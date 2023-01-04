# requests 와 json 을 활용하여 slack bot 조작하기
import requests
import json
import pickle
import os
from scraper.scraping_web import CreateAttachment



Token = '토큰 할당'
channel = "슬랙채널"
text = "notification_message"

def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text ,"attachments": attachments})


if __name__=="__main__":
    json_file = json.load(open('./configuration.json', 'r'))
    target_link = json_file['object_1']['target_link']
    target_name = json_file['object_1']['target_name']
    
    attach_list = [CreateAttachment(target_link).attachment()]
    slack_text= target_name+"의 "+attach_list[0]['date']+" 새 공지입니다."
    
    
    if 'before_notice.pickle' not in os.listdir("./"):
        pickle.dump(attach_list, open('before_notice.pickle', 'wb'))
        notice_message(Token, channel, slack_text, attach_list)
        before_notice = attach_list
    else:
        before_notice = pickle.load(open('before_notice.pickle', 'rb'))
    
    if (attach_list[0]['title']==before_notice[0]['title'] and attach_list[0]['date'] == before_notice[0]['date']):
        print("nothing to notice, before: {}, {}".format(attach_list[0]['title'], attach_list[0]['date']))
    else:
        pickle.dump(attach_list, open('before_notice.pickle', 'wb'))
        notice_message(Token, channel, slack_text, attach_list)
    
    