from scraper import generate_wiki_graph
from WikiPage import WikiPage
from WikiGraph import WikiGraph
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

    with open('wiki_page_test.json', "w") as f:
        json.dump(wiki_page.to_dict(), f, indent=2)

    # test json deserializing
    with open('wiki_page_test.json', "r") as f:
        loaded_data = json.load(f)
    
    loaded_obj = WikiPage.from_dict(loaded_data)

    # test graph serialization
    with open('wiki_graph_test.json', 'w') as f:
        json.dump(wg.to_dict(), f, indent=2)

    # test graph deserialization
    with open('wiki_graph_test.json', 'r') as f:
        graph_data = json.load(f)
    
    graph_loaded_obj = WikiGraph.from_dict(graph_data)

    





if __name__ == "__main__":
    main()