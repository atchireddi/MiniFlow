#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Graph Structure Implementation.
will use python Class to represent a generic node.
"""

class Neuron:
    """
        Neuron Class defines base set of properties that every node holds.
        only specialized subclasses of Neuron will endup in the graph.
        
        Make sure you build sub classes of Neuron that can perform Calculations
        and hold values.
    """
    
    def __init__(self, inbound_neurons=[]):
        # Arguments:
        # Class Constructor, self represents its own instantiation.
        
        # . . . . Properties will go here! -----
        
        # Each node of graph might receive input from multiple other nodes.
        # generates a single output which will likely be passed to other nodes.
        # add two lists: one to store references to the inbound nodes, and the 
        # other to store references to the out bound nodes.
        
        # Neuron from which this neuron receives values
        self.inbound_neurons = inbound_neurons   
        
        # Neuron to which this Neuron passes values
        self.outbound_neurons = []

        # For each inbound Neuron here, add this Neurron as an Outbound
        # Neuron there.
        for n in self.inbound_neurons:
            n.outbound_neurons.append(self)
            
        
        # Each Node will calculate a value that represents its output.
        # initialize the value to None to indicate that it exists but hasn't 
        # been set yet.
        self.value = None
        
        
        # . . . . Methods will go here! ----
        
        # Each node will need to be able to pass values forward and perform
        # backpropagation. Define methods for forward and backwrad propagation.
        
        def forward(self):
            """
            Forward Propagation.
            
            Compute the output value based on 'inbound_neurons' and store the
            result in self.value
            """
            
            raise NotImplemented
            
        def backward(self):
            """
            Backward propagation
            
            
            """
            
            raise NotImplemented
            
            
            
            
class Input(Neuron):
    """
        Derived subclass from Neuron.
        
        Represents the input node of the graph. Is the only node in the graph
        where the value may be passed as an argument to forward()
        
        Unlike other subclasses of Neuron, the Input subclass does not actually
        calculate anything. 
        
        Input subclass just holds a value, sush as a data feature or a model
        parameter.
        
        can set value either explicitly or with  the forward method. This value
        is then fed through the rest of the neural network.
    """
    def __init__(self):
        
        # Input Neuron has no inbound neurons.
        # so no need to pass anything to the Neuron Instantiatior.
        
        Neuron.__init__(self)
        
    def forward(self, value=None):
        
        # Overwrite the value if one is passed in.
        
        if value is not None:
            self.value = value
        
        
class Add(Neuron):
    """
        Derived calss from Neuron. Adds and store values of input nodes.
        
        This node performs a calculation. This node should appear in one of 
        hidden layers
    """
        
    def __init__(self, x, y):
        
        # Add Neuron requires min of two inbound Neurons
        
        Neuron.__init__(self, [x,y])
        
        
    def forward(self):
        """
            Add values of inbound neurons and stores result in self.value
        """
        
        self.value = 0        # Init Value
        
        for n in self.inbound_neurons:
            self.value += n.value

            
            
            

"""
No need to change anything below here!
"""


def topological_sort(feed_dict):
    """
    Sort generic nodes in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` node and the value is
                    the respective value feed to that node.

    Returns a list of sorted nodes.
    """

    input_neurons = [n for n in feed_dict.keys()]

    G = {}
    neurons = [n for n in input_neurons]
    while len(neurons) > 0:
        n = neurons.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_neurons:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            neurons.append(m)

    L = []
    S = set(input_neurons)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_neurons:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L


def forward_pass(output_neuron, sorted_neurons):
    """
    Performs a forward pass through a list of sorted neurons.

    Arguments:

        `output_neuron`: A neuron in the graph, should be the output neuron 
                            (have no outgoing edges).
        `sorted_neurons`: a topologically sorted list of neurons.

    Returns the output neuron's value
    """

    for n in sorted_neurons:
        n.forward()

    return output_neuron.value
    
    