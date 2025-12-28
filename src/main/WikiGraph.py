from WikiPage import WikiPage
class WikiGraph:
    def __init__(self, graph=[]):
        self.graph = graph
   
    def to_dict(self):
        return {
            'graph': [page.to_dict() for page in self.graph]
        }
    
    @classmethod
    def from_dict(cls, data):
        graph_dict = data['graph']
        graph_arr_data = list(graph_dict)


        # get each page object
        graph_obj_arr = []
        for page_data in graph_arr_data:
            graph_obj_arr.append(WikiPage.from_dict(page_data))
        
        return cls(graph=graph_obj_arr)
    
    def __repr__(self):
        return f"graph: {self.graph!r}"
    
    def __eq__(self, other):
        if not isinstance(other, WikiGraph):
            return False
        
        return (
            self.graph == other.graph
        )
