import urllib.request
import json

class PostData(object):
    def __init__(self):
        self.BOT_TOKEN = ''

    def header(self):
        return {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization': 'Bearer {0}'.format(self.BOT_TOKEN)
        }

def handler():
    url_post = 'https://slack.com/api/chat.postMessage'
    postdata = PostData()
    post_head = postdata.header()
    payload = {
        "test": "hello test",
        "username": "test_user",
        "channel": "#bot_test"
        } 
    req = urllib.request.Request(url_post, data=json.dumps(payload).encode('utf-8'), method='POST', headers=post_head)
    res = urllib.request.urlopen(req)
    print(res)

if __name__ == '__main__':
    handler()
