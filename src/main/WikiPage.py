class WikiPage:
    # init method must have access to needed elements to build object both from web scraping, but also from json reading
    # id is url, title is title stripped of - Wikipedia suffix, links is array of all 
    def __init__(self, id, title, links): 
        self.id = id
        self.title = title       
        self.links = list(links) # convert from set (how its loaded) to list
        
        ...

    # override __eq__ method 

    # loader static method that enables the construction of object from soup-object page
    def load_wiki_page(parsed_page, url):
        # url is easy
            
        # get title (strip of suffix)
        title_text = parsed_page.title.string
        title_text = title_text.removesuffix("- Wikipedia")

        # get list of links
        links = set()
        for link in parsed_page.find_all('a'):
            href_txt = link.get('href')

            if href_txt is None:
                continue
            if "#" in href_txt:
                continue
            if ":" in href_txt:
                continue
            if "/wiki/" not in href_txt:
                continue

            links.add("https://en.wikipedia.org" + href_txt)
        
        # return
        return url, title_text, links