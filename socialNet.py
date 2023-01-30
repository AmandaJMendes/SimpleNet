import pickle
from graphClass import Graph
import matplotlib.pyplot as plt
import networkx as nx
import copy
from matplotlib.lines import Line2D

class SimpleNet:
    def __init__(self):
        """
        This is a SimpleNet class
        It is an interface between the windows and the graph
        """
        self.G = None
        
    def fromPkl(self, filepath):
        """
        Load graph from pickle
        """
        if not self.G:
            with open(filepath, 'rb') as inp:
                self.G = pickle.load(inp)
        else:
            print("Graph already exists")
            
    def dumpToPkl(self, filepath):
        with open(filepath, "wb") as outp:
            pickle.dump(self.G, outp, pickle.HIGHEST_PROTOCOL)
            
    def fromEmptyGraph(self):
        """
        Create empty graph
        """
        if not self.G:
            self.G = Graph()
        else:
            print("Graph already exists")
            
    def getUsers(self):
        """
        Return network users / graph vertices
        """
        return self.G.getVertices()
    
    def getUser(self, username):
        """
        Return vertex instance given the username (key)
        """
        return self.G.getVertex(username)
    
    def getFollowers(self, username):
        """
        Return vertex instance given the username (key)
        """
        return self.G.getIncident(username)
    
    
    def isUser(self, user):
        """
        Return whether an user is in the network or not
        """
        return self.G.inGraph(user)
    
    def validData(self, data, unexpected):
        """
        Return whether data is valid or not
        """
        for d, un in zip(data, unexpected):
            if d == un:
                return False
        return True
    
    def createAccount(self, user, passwrd, person, data, unexpeceted_data, private, labels):
        """
        Create account / add vertex to graph
        """
        if self.isUser(user):
            return -1
        elif not self.validData(data+[user, passwrd], unexpeceted_data+["", ""]):
            return 0        
        else:
            private, public = self.setUserData(data, private, labels)
            info = {"person": person, "passwrd": passwrd,
                    "private": private, "public": public,
                    "friends": [], "acquaintances": [],
                    "familly": [], "orgs": [], "posts": []}
            self.G.addVertex(user, info)
            
    def updateAccount(self, user, data, unexpeceted_data, private, labels):
        """
        Update user's information / vertex's value
        """
        if not self.validData(data, unexpeceted_data):
            return False        
        else:
            private, public = self.setUserData(data, private, labels)
            user.value["private"] = private
            user.value["public"] = public
            return True
            
    def setUserData(self, data, private_cb, labels):
        """
        Set new data
        """
        private = {}
        public = {}
        for info, cb, field in zip(data, private_cb, labels):
            if cb:
                private[field] = info
            else:
                public[field] = info
        return private, public
    
        
    def smartSearch(self, user, key, value, person = True):
        """
        Perform BFS to find user[key] = value
        """
        if key == "user":
            matches = self.G.BFS(user, True, lambda v: v.value["person"] == person and v.key == value)
        else:
            matches = self.G.BFS(user, True, lambda v: v.value["person"] == person and key in v.value["public"].keys() and v.value["public"][key] == value)
        return matches
    
    def dumbSearch(self, key, value, person = True):
        """
        Perform BFS to find user[key] = value
        """
        matches = []
        for v in self.G.vertices.values():
            if key == "user" and v.value["person"] == person and v.key == value:
                matches.append(v)
            if v.value["person"] == person and key in v.value["public"].keys() and v.value["public"][key] == value:
                matches.append(v)
        return matches
            
        
    def getConnection(self, user1, user2):
        """
        Get relatioship between two users
        """
        return self.G.getEdgeWeight(user1.key, user2.key)
    
    def addFriendship(self, user1, user2):
        """
        Add edge between two users with weight = friend
        """
        self.G.addEdge(user1.key, user2.key, weight = "Amigo")
        self.G.addEdge(user2.key, user1.key, weight = "Amigo")
        
    def addAcquaintance(self, user1, user2):
        """
        Add edge between two users with weight = acquaintance
        """
        self.G.addEdge(user1.key, user2.key, weight = "Conhecido")
        
    def addFamily(self, user1, user2):
        """
        Add edge between two users with weight = family
        """
        self.G.addEdge(user1.key, user2.key, weight = "Família")
        self.G.addEdge(user2.key, user1.key, weight = "Família")
        
    def addClient(self, user1, user2):
        """
        Add edge between two users with weight = client
        """
        self.G.addEdge(user1.key, user2.key, weight = "Cliente")

    def removeFriendship(self, user1, user2):
        """
        Remove edge between two users 
        """
        self.G.removeEdge(user1.key, user2.key)
        self.G.removeEdge(user2.key, user1.key)
        
    def removeAcquaintance(self, user1, user2):
        """
        Remove edge between two users 
        """
        self.G.removeEdge(user1.key, user2.key)
        
    def removeFamily(self, user1, user2):
        """
        Remove edge between two users 
        """
        self.G.removeEdge(user1.key, user2.key)
        self.G.removeEdge(user2.key, user1.key)
        
    def removeClient(self, user1, user2):
        """
        Remove edge between two users 
        """
        self.G.removeEdge(user1.key, user2.key)
    
            
    def saveGraphImg(self, user, path, levels = None):
        """
        Create graph in the networkx library
        Save it to image
        """
        DG = nx.DiGraph()
        
        if levels != None:
            vertices = self.G.BFS(start = user.key, visible = False, max_level = levels)       
        else:
            vertices = self.G.vertices.values()

        node_colors = []
        for v in vertices:
            if v is user:
                DG.add_node(v.key, color = "paleturquoise")
                node_colors.append("paleturquoise")
            else:
                DG.add_node(v.key, color = "palegoldenrod")
                node_colors.append("palegoldenrod")
                
            for v2 in v.adjacent.values():
                if v2[0] in vertices:
                    w = self.getConnection(v, v2[0])
                    if w == "Amigo":
                        color = "red"
                    elif w == "Conhecido":
                        color = "blue"
                    elif w == "Família":
                        color = "green"
                    else:
                        color = "black"
                    DG.add_edge(v.key, v2[0].key, color = color)

        edge_colors = [DG[u][v]['color'] for u,v in DG.edges()]
        pos = nx.circular_layout(DG)
        nx.draw(DG, pos, with_labels=True, edge_color=edge_colors, node_color = node_colors)
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Família',markerfacecolor='g', markersize=8),
            Line2D([0], [0], marker='o', color='w', label='Amigo',markerfacecolor='r', markersize=8),
            Line2D([0], [0], marker='o', color='w', label='Conhecido',markerfacecolor='blue', markersize=8),
            Line2D([0], [0], marker='o', color='w', label='Cliente',markerfacecolor='black', markersize=8),  
        ]
        plt.legend(handles=legend_elements, loc='upper right')
        plt.savefig(path)
        plt.clf()
        
        
        
        
        
        
        
        
        
    
    
        
