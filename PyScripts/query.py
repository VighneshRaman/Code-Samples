import requests
from bs4 import BeautifulSoup

def query(url,req='get',params={},headers={},cookies={},proxies={}):
    # url: give the url as a string.
    # req: a string ('get' or 'post') that specifies request type.
    # params, headers, cookies & proxies:
    if req == 'post':
        # Post requests
        r = requests.post(url,data=params,headers=headers,cookies=cookies,proxies=proxies)
        soup = BeautifulSoup(str(r.text))
        return soup
    else:
        # Get requests
        r = requests.get(url,data=params,headers=headers,cookies=cookies,proxies=proxies)
        soup = BeautifulSoup(str(r.text))
        return soup
