# !/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
    Graph Structure Implementation.
    will use python Class to represent a generic Layer.
    Feed Forward Completed
"""

# Layer Base Classe
class Layer:
    """
        Layer Class defines base set of properties that every Layer holds.
        Specialized subclasses of Layer end-up in the graph.

        subclasses can be build that can perform Calculations and hold values.
    """

    def __init__(self, inbound_layer, weights):
        """

        :param inbound_layer: Input Layer
        :param weights:  weights
        """
        self.inputs = inputs
        self.weights = weights
        self.outputs = []

    forward()
        inputs = self.inbound_layer.outputs
        self.value = Non
        for n in range(len(inputs))
            weight = self.weights[n]
            input = inputs[n]
            self.outputs.append(do_math(input, weight))    # No of Outputs computed based on inputs and weights


class Input(Layer):
    """
        Input Layer Definition. Derived from Layer.

    """

    def __init__(self, inputs):
        """

        """
    pass


Input()

"""
No need to change anything below here!
"""



def topological_sort(feed_dict):
    """
    Sort the layers in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` Layer and the value is the respective value feed to that Layer.

    Returns a list of sorted layers.
    """

    input_layers = [n for n in feed_dict.keys()]

    G = {}
    layers = [n for n in input_layers]
    while len(layers) > 0:
        n = layers.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_layers:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            layers.append(m)

    L = []
    S = set(input_layers)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_layers:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L


def forward_pass(output_layer, sorted_layers):
    """
    Performs a forward pass through a list of sorted Layers.

    Arguments:

        `output_layer`: A Layer in the graph, should be the output layer (have no outgoing edges).
        `sorted_layers`: a topologically sorted list of layers.

    Returns the output layer's value
    """

    for n in sorted_layers:
        n.forward()

    return output_layer.value

