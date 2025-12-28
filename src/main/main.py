from scraper import generate_wiki_graph

def main():
    START = "https://en.wikipedia.org/wiki/Ankara"
    LIMIT = 2
    wg = generate_wiki_graph(START, LIMIT)
    print(wg.graph)
    print(len(wg.graph))

    for page in wg.graph:
        print(page.title)
        print(page.id)




if __name__ == "__main__":
    main()