from scraper import generate_wiki_graph
from WikiPage import WikiPage
import json

def main():
    START = "https://en.wikipedia.org/wiki/Ankara"
    LIMIT = 1
    wg = generate_wiki_graph(START, LIMIT)
    print(wg.graph)
    print(len(wg.graph))

    for page in wg.graph:
        print(page.title)
        print(page.id)

    # test json serializing
    wiki_page = wg.graph[0]
    print(wiki_page.__repr__())

    with open('wiki_page_test.json', "w") as f:
        json.dump(wiki_page.to_dict(), f, indent=2)

    # test json deserializing
    with open('wiki_page_test.json', "r") as f:
        loaded_data = json.load(f)
    
    loaded_obj = WikiPage.from_dict(loaded_data)
    print(wiki_page.__repr__())
    print(loaded_obj.__repr__())

    print(wiki_page == loaded_obj)




if __name__ == "__main__":
    main()