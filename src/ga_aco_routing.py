import networkx as nx
import random

class GA_ACO_Routing:

    def __init__(self, graph):
        self.graph = graph

    def genetic_algorithm_route(self, source, target):
        paths = list(nx.all_simple_paths(self.graph, source, target, cutoff=5))
        if not paths:
            return None
        return random.choice(paths)

    def ant_colony_route(self, source, target):
        path = nx.shortest_path(self.graph, source, target, weight='weight')
        return path

    def optimize_route(self, source, target):
        ga_path = self.genetic_algorithm_route(source, target)
        aco_path = self.ant_colony_route(source, target)

        if ga_path and len(ga_path) < len(aco_path):
            return ga_path
        return aco_path
