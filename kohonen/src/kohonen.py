from dataclasses import dataclass
from typing import List, Tuple
from abc import ABC, abstractmethod
import numpy as np
import random

@dataclass
class Node:
    row: int
    col: int
    weights: List[float]
    distance: float = "inf"

    # def get_pixel(self):
    #     if self.distance == 'inf': return 255
    #     else:
    #         return self.distance

    def get_pixel(self):
        return int(sum(self.weights) / len(self.weights) * 255)
        
    def __post_init__(self):
        self.pixel = self.get_pixel()


class InputVector:
    def __init__(self, size: int):
        self.size = size
        self.vector = [random.uniform(0, 1) for _ in range(self.size)]

    def show(self):
        print([_ for _ in self.vector])


class Network:
    def __init__(self, map_size: Tuple, input_vector_size: int):
        self.height, self.width = map_size
        # self.input_vector = InputVector(size=input_vector_size)
        self.input_vector_size = input_vector_size
        self.nodes = self.initialize_nodes()

    def initialize_nodes(self) -> List[Node]:
        nodes = []
        for row in range(self.height):
            node_row = []
            for col in range(self.width):
                node_row.append(
                    Node(
                        row=row,
                        col=col,
                        weights=[random.uniform(0, 1) for _ in range(self.input_vector_size)],
                    )
                )
            nodes.append(node_row)
        return nodes

    def get_image_data(self):
        nodes = []
        for row in range(self.height):
            node_row = []
            for col in range(self.width):
                node_row.append(self.nodes[row][col].pixel)
            nodes.append(node_row)
        return nodes

    def show(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.nodes[row][col].weights)
            print()


class Trainer(ABC):
    @abstractmethod
    def train(self):
        pass


class KohonenTrainer(Trainer):
    def __init__(self, network: Network, input_vector: InputVector, max_iterations: int) -> None:
        self.network = network
        self.input_vector = input_vector
        self.bmu = self.get_bmu()
        self.max_iterations = max_iterations
        self.s_0 = max(self.network.width, self.network.height) / 2
        self.lam = self.max_iterations / np.log(self.s_0)

    def get_euclidian_distance(self, vector1: List[int], vector2: List[int]):
        return np.linalg.norm(np.array(vector1) - np.array(vector2))

    def get_bmu(self) -> Node:
        best_distance = float("inf")
        best_node = None

        for row in range(self.network.height):
            for col in range(self.network.width):
                node = self.network.nodes[row][col]
                # node.distance = self.get_euclidian_distance(self.input_vector, node)
                node.distance = self.get_euclidian_distance(self.input_vector.vector, node.weights)
                if node.distance < best_distance:
                    best_distance = node.distance
                    best_node = self.network.nodes[row][col]
        return best_node

    def get_neighbourhood_radius(self, iteration: int):
        s_t = self.s_0 * np.exp(-iteration / self.lam)
        return s_t

    def get_learning_rate(self, iteration):
        a_0 = 0.1
        a_t = a_0 * np.exp(-iteration / self.lam)
        return a_t

    def get_influence(self, node: Node, iteration: int):
        s_t = self.get_neighbourhood_radius(iteration)
        distance = self.get_euclidian_distance([self.bmu.row, self.bmu.col], [node.row, node.col])
        influence = np.exp(-(distance**2) / (2 * s_t**2))
        return influence

    def update_weights(self, node: Node, iteration: int):
        a_t = self.get_learning_rate(iteration)
        influence = self.get_influence(node, iteration)
        current_weights = np.array(node.weights)
        new_weights = current_weights + a_t * influence * (np.array(self.input_vector.vector) - current_weights)
        node.weights = new_weights.tolist()
        node.distance = self.get_euclidian_distance(self.bmu.weights, node.weights)
        node.pixel = node.get_pixel()

    def train(self):
        for iteration in range(self.max_iterations):
            for row in range(self.network.height):
                for col in range(self.network.width):
                    self.update_weights(node=self.network.nodes[row][col], iteration=iteration)
