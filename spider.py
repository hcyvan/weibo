import re
import requests

from conf import Config

headers = Config.HEADERS


def get_one_page_by_char(char, page):
    url = "https://weibo.com/2032078483/fans#Pl_Official_RelationFans__66"
    querystring = {"cfs": "600", "relate": "fans", "t": "1", "f": "1", "type": "", "search": char,
                   "Pl_Official_RelationFans__66_page": page}
    response = requests.request("GET", url, headers=headers, params=querystring)
    pattern = re.compile('uid=(\d+)&nick=(.*?)\\\\')
    return pattern.findall(response.text)


def search_users_by_char(char):
    id_names = []
    last_id = ''
    current_page = 1
    while True:
        id_names_in_this_page = get_one_page_by_char(char, current_page)
        id_names.extend(id_names_in_this_page)
        if not id_names or last_id == id_names[-1][0]:
            break
        last_id = id_names[-1][0]
        current_page = current_page + 1

    return id_names


if __name__ == '__main__':
    print(search_users_by_char('珲'))

