import re
import hashlib
from collections import Counter, defaultdict
def get_external_links(page):
    comp = re.compile(r"\<a href\=\"https:\/\/(?P<exturl>\S+)\"\>")
    return comp.findall(page)

def get_pageurl(page):
    comp = re.compile(r"<meta property=\"og\:url\" content=\"https:\/\/(?P<pageurl>[0-9a-z\/\.\:]+)\"(\s+)?\/>")
    res = comp.search(page)
    if not res:
        return ""
    return res.group('pageurl')

def get_urlhash(url):
    return hashlib.md5(url.encode("utf-8")).hexdigest()

def solution(word, pages):
    page_info = defaultdict(dict)
    referenced_dict = defaultdict(dict)
    for page_idx, page in enumerate(pages):
        word_dict = Counter(re.split(r"[^a-z]", page.lower())) 
        page_url = get_pageurl(page)
        urlhash = get_urlhash(page_url)
        
        page_info[urlhash] = {
            'page_idx': page_idx,
            'origin_url': page_url,
            'ext_links': [],
            'default_point': word_dict[word.lower()],
            'link_point': 0
        }
        
        for ext_url in get_external_links(page):
            ext_urlhash = get_urlhash(ext_url)
            page_info[urlhash]['ext_links'].append(
                get_urlhash(ext_url)
            )
            if not ext_urlhash in referenced_dict:
                referenced_dict[ext_urlhash] = []
            referenced_dict[ext_urlhash].append(urlhash)
        
    _max = [-1, -1]
    for urlhash in page_info:
        for referer in referenced_dict[urlhash]:
            page_info[urlhash]['link_point'] += (page_info[referer]['default_point']/len(page_info[referer]['ext_links']))
        if page_info[urlhash]['link_point'] + page_info[urlhash]['default_point'] > _max[0]:
            _max[0] = page_info[urlhash]['link_point'] + page_info[urlhash]['default_point']
            _max[1] = page_info[urlhash]['page_idx']
    
    answer = _max[1]
    return answer

if __name__ == '__main__':
    print(
        solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    )