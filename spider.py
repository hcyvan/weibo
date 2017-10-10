import re
import requests

from conf import Config

headers = Config.HEADERS


def get_one_search_page_by_char(char, page):
    url = "https://weibo.com/2032078483/fans#Pl_Official_RelationFans__66"
    querystring = {"cfs": "600", "relate": "fans", "t": "1", "f": "1", "type": "", "search": char,
                   "Pl_Official_RelationFans__66_page": page}
    response = requests.request("GET", url, headers=headers, params=querystring)
    pattern = re.compile('uid=(\d+)&nick=(.*?)\\\\')
    return pattern.findall(response.text)


def get_one_page_by_order(page, t=1):
    """
    :param page:
    :param t: 1 按时间排序， 5 按粉丝数目排序, 3??
    :return:
    """
    url = "https://weibo.com/2032078483/fans#Pl_Official_RelationFans__66"

    querystring = {"cfs": "", "relate": "fans", "t": "1", "f": "1", "type": "",
                   "Pl_Official_RelationFans__66_page": page}

    response = requests.request("GET", url, headers=headers, params=querystring)
    pattern = re.compile(
        '关注(?:.*?)>(\d+)<(?:.*?)粉丝(?:.*?)>(\d+)<(?:.*?)微博(?:.*?)>(\d+)<(?:.*?)uid=(\d+)&nick=(.*?)\\\\')

    return pattern.findall(response.text)


def search_users_by_char(char):
    id_names = []
    last_id = ''
    current_page = 1
    while True:
        id_names_in_this_page = get_one_search_page_by_char(char, current_page)
        if id_names and last_id == id_names[-1][0]:
            break
        id_names.extend(id_names_in_this_page)
        if not id_names:
            break
        last_id = id_names[-1][0]
        current_page = current_page + 1

    return id_names


def get_personal_page_id_by_uid(uid):
    url = "https://weibo.com/u/{}".format(uid)
    response = requests.request("GET", url, headers=headers)
    pattern = re.compile("page_id(.*?)(\d+)")
    match = pattern.search(response.text)
    if match:
        return match.group(2)
    return '100505' + str(uid)


def _get_personal_page_info(url):
    response = requests.request("GET", url, headers=headers)

    pattern_intro = re.compile('pf_intro(?:.*?)title=\\\\"(.*?)\\\\">')
    pattern_counts = re.compile(
        '<strong(?:.*?)>(.*?)<(?:.*?)关注(?:.*?)<strong(?:.*?)>(.*?)<(?:.*?)粉丝(?:.*?)<strong(?:.*?)>(.*?)<(?:.*?)微博')

    match = pattern_intro.search(response.text)
    intro = ''
    if match:
        intro = match.group(1)

    match = pattern_counts.search(response.text)
    fans_count = ''
    concern_count = ''
    weibo_count = ''
    if match:
        fans_count = match.group(1)
        concern_count = match.group(2)
        weibo_count = match.group(3)

    final = '{}<|>{}<|>{}<|>{}'.format(fans_count, concern_count, weibo_count, intro)

    if final != '<|><|><|>':
        return final, response.text

    return '', response.text


def get_personal_page_info_by_uid(uid):
    url = "https://weibo.com/u/{}".format(uid)

    final, html = _get_personal_page_info(url)
    if final:
        return final

    pattern_new_url = re.compile('url(?:.*?)"(https.*?)"')
    match = pattern_new_url.search(html)
    new_url = ''
    if match:
        new_url = match.group(1)

    final, html = _get_personal_page_info(new_url)
    if final:
        return final
    else:
        raise Exception('something wrong')


def get_personal_info_by_page_id(page_id):
    if not page_id:
        return None
    url = "https://weibo.com/p/{}/info".format(page_id)
    querystring = {"mod": "pedit_more"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    pattern = re.compile('"html":"(.*?)基本信息(.*?)(<ul(.*?)ul>)')
    match = pattern.search(response.text)
    if match:
        html = match.group(3)
        html = ''.join(html.split("\\t"))
        html = ''.join(html.split("\\r\\n"))
        html = ''.join(html.split("\\"))
        pattern = re.compile('<span(?:.*?)>(.*?)<(?:.*?)span><(?:.*?)>(.*?)<(?:.*?)><(?:.*?)li>')
        return pattern.findall(html)
    return ''


def get_personal_fans_by_page_id(page_id, page=1):
    if not page_id:
        return []
    url = "https://weibo.com/p/{}/follow#Pl_Official_HisRelation__60".format(page_id)
    querystring = {"page": page}
    response = requests.request("GET", url, headers=headers, params=querystring)
    pattern = re.compile('uid=(\d+)&nick=(.*?)\\\\')
    fans = pattern.findall(response.text)
    if fans:
        return fans[1:-1]
    return []


if __name__ == '__main__':
    # print(search_users_by_char('w'))
    # print(get_one_page_by_order(1))
    get_personal_page_info_by_uid(1039096957)
