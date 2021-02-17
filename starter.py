from bs4 import BeautifulSoup as bs
import requests as r

url = "http://"+input("insert IP>>> ")+":10000" #base url
# url = "http://192.168.0.101:10000" #base url
documents = url+"/Documents" #available document folders    


def starter():
    """returns text of '/x ' folder
    https://www.kite.com/python/answers/how-to-get-href-links-from-urllib-urlopen-in-python
    """
    req = r.request("get",documents).text 

    soup = bs(req,"lxml") #create soup of get
    links = soup.find_all("a") #finds all 'a' tags
    valid_links = []

    for l in links:
        valid_links.append(l.get("href")) #gets all hrefs from soup.find_all
        
    for files in valid_links[1:]:
        get_files(files)

def get_files(path):
    """gets all files in path"""
    req = r.request("get",url+path).text 

    soup = bs(req,"lxml") #create soup of get
    links = soup.find_all("a") #finds all 'a' tags
    valid_links = []

    for l in links:
        valid_links.append(l.get("href")) #gets all hrefs from soup.find_all

    for paths in valid_links:
        if str(paths).endswith(".jpg"): #gets all jpg files
            downloader(paths)#sends all files to downloader

def downloader(path):
    fullpath = url+path
    names = str(path).split("/")
    if str(names[3]).startswith(".") == False:
        res = r.get(fullpath)
        file = open(f"file-{names[3]}","wb")
        file.write(res.content)
        file.close()

starter()