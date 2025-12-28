from WikiGraph import WikiGraph
from WikiPage import WikiPage
from FrontierQueue import FrontierQueue
import requests
from bs4 import BeautifulSoup

# util library for scraper methods

# request page
# return text of html
def request_page(url):
    # header
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    "Accept-Encoding": "gzip"
    }

    # request page
    response = None
    try:
        response = requests.get(url, headers=header)

        if response.status_code == 200:
            # succesful -> return
            ...
        else:
            print(f"Request Failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Request Error: ", e)
    
    return response.text


# parses page and returns soup object 
def parse_page(txt):
    soup = BeautifulSoup(txt, "html.parser")
    return soup

# generate wiki graph: BFS out from a start node, adding pages
# start: url, limit: int
def generate_wiki_graph(start, limit):
    # init
    wg = WikiGraph()
    page_visted = set()
    num_visited = 0
    frontier = FrontierQueue()

    frontier.push(start)

    # loop
    while frontier.size() > 0 and num_visited < limit: 
        # pop url
        current_url = frontier.pop()
        print(current_url)

        # add to page visited
        page_visted.add(current_url)

        # request page
        current_txt = request_page(current_url)

        # parse page
        current_pg_parsed = parse_page(current_txt)

        # load wiki object
        wo = WikiPage(*WikiPage.load_wiki_page(current_pg_parsed, current_url))
        wg.graph.append(wo)

        # add links to frontier
        for link in wo.links:
            # ensure uniquness
            if link not in page_visted:           
                frontier.push(link)

        # repeat
        num_visited += 1

    return wg

