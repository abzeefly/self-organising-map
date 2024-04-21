import sys
sys.path.append("...")
from src.kohonen import Node, InputVector, Network, KohonenTrainer
import numpy as np
import pytest


@pytest.mark.parametrize(
    "weights, expected_pixel",
    [
        ([0.1, 0.2, 0.3, 0.4], 63),
        ([0.5, 0.5], 127),
        ([0.0, 1.0], 127),
        ([1.0, 0.0], 127),
        ([0.25, 0.25, 0.25, 0.25], 63),
    ],
)
def test_get_pixel(weights, expected_pixel):
    node = Node(row=1, col=1, weights=weights)
    pixel = node.get_pixel()
    assert pixel == expected_pixel


import pytest


@pytest.mark.parametrize(
    "iteration, expected_learning_rate",
    [
        (0, 0.1),
        (7, 0.03789291416275996),
        (10, 0.025),
        (1, 0.08705505632961241),
    ],
)
def test_get_learning_rate(iteration, expected_learning_rate):
    input_vector = InputVector(size=3)
    network = Network(map_size=(4, 4), input_vector_size=input_vector.size)
    trainer = KohonenTrainer(network=network, input_vector=input_vector, max_iterations=5)
    learning_rate = trainer.get_learning_rate(iteration)
    assert pytest.approx(learning_rate, rel=1e-5) == expected_learning_rate


"""

More tests can be added

"""
