class Graph: 
    def __init__(self,routes) : 
        self.routes = {} 
        for start,end in routes: 
            if start in self.routes : 
                self.routes[start].append(end)
            else: 
                self.routes[start] = [ end ]
        print(self.routes) 
    

    def find_all_route (self, start,end , path = []) :
        path = path + [start]

        if start == end : 
            return [path]

        if start not in self.routes: 
            return []
        
        all_route = []

        for i in self.routes[start]: 
            if i not in path:
                all = self.find_all_route(i, end , path)
                for j in all:
                    all_route.append(j)
        return all_route

    def get_shortest_path (self, start,end , path = []) :
        path = path + [start]

        if start == end : 
            return path

        if start not in self.routes: 
            return None
        
        shortest_path = None

        for i in self.routes[start]: 
            if i not in path:
                sp = self.get_shortest_path(i, end , path)
                if sp: 
                    if shortest_path is None or len( sp) < len (shortest_path):
                        shortest_path = sp
        return shortest_path



if __name__ == "__main__": 
    route =  [
        ("Mumbai", "Surat"),
        ("Mumbai", "Pune"),
        ("Surat", "Delhi"),
        ("Surat", "Jaipur"),
        ("Pune","Delhi"),
        ("Pune","Banglore"),
        ("Jaipur", "Pune")
    ]
    graph = Graph(route)

    start="Mumbai"
    end= "Banglore"
    print ( "all path are =",graph.find_all_route(start,end) ) 
    print ( "one of the shortest path =",graph.get_shortest_path(start,end) ) 


