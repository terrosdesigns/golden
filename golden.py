import requests
from bs4 import BeautifulSoup
# from proxies import proxies
import sys

def extractPageContent(url):
    try:
        page = requests.get(url)
    except:
        print("Error while trying to get page")
        sys.exit()
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def getFirstSearchResult(user_query):
    # query = input("What is your query ?\n")
    base_url = 'https://golden.com'
    base_search_url = 'https://golden.com/search/'
    search_url = base_search_url + user_query
    soup = extractPageContent(search_url)
    links_list = []
    for link in soup.find_all('a'):
        links_list.append(link.get('href'))
    first_result = links_list[3]
    first_result_link = base_url + first_result
    return first_result_link

def getQueryUrl():
    base_url = 'https://golden.com/wiki/'
    query = getSearchResult()
    url = base_url + query
    return url

def download(user_query):
    search_url = getFirstSearchResult(user_query)
    try:
        page = requests.get(search_url)
    except:
        print("Error while trying to get page")
        sys.exit()
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup
    # description = soup.find_all('p')[0].get_text()
    # print(description)
    # return description

def summary_old(user_query, sentences=0):
    query = str(user_query)
    soup=download(query)
    summary = []
    i = 0
    while i <= sentences:
        summary.append(soup.find_all('p')[i].get_text())
        i+=1
    description = "".join(summary)
    return description

def timeline_old(user_query, events=0):
    query = str(user_query)
    soup=download(query)
    timeline_block = soup.findAll("div", {"class": "EntityTimeline"})
    events_list = []
    i=0
    while i <= events:
        try:
            event_div = soup.findAll("div", {"class": "TimelineEvent"})[i]
        except:
            print("No more events. Breaking.")
            break
        event = {}
        try:
            event["date"] = event_div.findAll("div", {"class": "TimelineEvent__date"})[i].get_text()
            event["subtitle"] = event_div.findAll("h3")[0].get_text()
            event["content"] = event_div.findAll("p")[0].get_text()
        except:
            print("No more events. Breaking.")
            break
        events_list.append(event)
        i+=1
    # events_string = "\n".join(events_list)
    return events_list

def summary(soup, sentences=0):
    summary = []
    i = 0
    while i <= sentences:
        summary.append(soup.find_all('p')[i].get_text())
        i+=1
    description = "".join(summary)
    return description

def timeline(soup, events=0):
    timeline_block = soup.findAll("div", {"class": "EntityTimeline"})
    events_list = []
    i=0
    while i <= events:
        try:
            event_div = soup.findAll("div", {"class": "TimelineEvent"})[i]
        except:
            print("No more events. Breaking.")
            break
        event = {}
        try:
            event["date"] = event_div.findAll("div", {"class": "TimelineEvent__date"})[i].get_text()
            event["subtitle"] = event_div.findAll("h3")[0].get_text()
            event["content"] = event_div.findAll("p")[0].get_text()
        except:
            print("No more events. Breaking.")
            break
        events_list.append(event)
        i+=1
    # events_string = "\n".join(events_list)
    return events_list
