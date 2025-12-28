from sentence_transformers import SentenceTransformer
from time import perf_counter

class WikiPage:
    # init method must have access to needed elements to build object both from web scraping, but also from json reading
    # id is url, title is title stripped of - Wikipedia suffix, links is array of all 
    def __init__(self, id, title, links, title_vector): 
        self.id = id
        self.title = title       
        self.links = list(links) # convert from set (how its loaded) to list
        self.title = title_vector

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

        # get title vector       

        #DEBUG time to vectorize

        start_time = perf_counter()
        model = SentenceTransformer('all-MiniLM-L6-v2')
        title_vector = model.encode(title_text) 
        
        end_time = perf_counter()   
        elapsed_time = end_time - start_time
        print(f"Time taken to vectorize title '{title_text}': {elapsed_time:.4f} seconds")

        # return
        return url, title_text, links, title_vector