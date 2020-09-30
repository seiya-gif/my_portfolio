import requests
from bs4 import BeautifulSoup


line_url = "https://notify-api.line.me/api/notify"

# LINE Notifyのアクセストークンを記述
access_token = ('')
headers = {'Authorization': 'Bearer ' + access_token}

taisei_url = 'https://scfc2000.amebaownd.com/pages/1525052/static'
r1 = requests.get(taisei_url)
soup = BeautifulSoup(r1.text, 'html.parser')
article = soup.find(class_='block-txt txt txt--s u-txt-clr').text


def send(message):
   params = {'message': message}
   r2 = requests.post(line_url, headers=headers, params=params,)

def main():
    send(article + '\n' + taisei_url)


if __name__ == '__main__':
    main()


