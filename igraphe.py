
import unittest
from abc import ABC

class GraphInterface(ABC):

    def add_node(self, node):
        return NotImplemented

    def node_count(self):
        return NotImplemented

    def add_edge(self, nd1, nd2):
        return NotImplemented

    def edge_count(self):
        return NotImplemented

    def edge_exists(self, nd1, nd2):
        return NotImplemented


class Graph(GraphInterface):
    #TODO : implement me
    # constructeur
    def __init__(self):
        # attribut
        self.noeud = []
        self.arete = []

    # declarer une methode
    def add_node(self, noeud):
        print(noeud + ' est ajoute')
        self.noeud.append(noeud)

    def add_edge(self, noeud1, noeud2):
        print('Ajout arete entre ' + noeud1 + ' et ' + noeud2)
        self.arete.append(noeud1 + ':' + noeud2)

    def edge_exist(self, n1, n2):
        result = "Cette arete n'existe pas"

        for a in self.arete:
            if a == (n1 + ':' + n2):
                result = "Cette arete existe"

        return result