import networkx as nx
from ga_aco_routing import GA_ACO_Routing
from catboost_predictor import CongestionPredictor
from q_learning_agent import QLearningAgent

class HybridController:

    def __init__(self):
        self.graph = nx.erdos_renyi_graph(10, 0.3)

        for u,v in self.graph.edges():
            self.graph[u][v]['weight'] = 1

        self.router = GA_ACO_Routing(self.graph)
        self.predictor = CongestionPredictor()
        self.rl_agent = QLearningAgent(10,5)

    def run(self, dataset):

        self.predictor.train(dataset)

        source = 0
        destination = 9

        path = self.router.optimize_route(source,destination)

        print("Optimized Route:", path)
