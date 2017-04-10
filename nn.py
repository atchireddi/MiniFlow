#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
    Neural Network to add numbers
"""

from myflow import *

# Graph Structure 

x, y, z = Input(), Input(), Input()

f = Add([x, y, z])

# z = Add(f, y)


# 
feed_dict = {x: 10, y: 25, z: 5}

sorted_neurons = topological_sort(feed_dict)
output = forward_pass(f, sorted_neurons)

# NOTE: because topological_sort set the values for the `Input` neurons we could also access
# the value for x with x.value (same goes for y).
print("{} + {} = {} (according to myflow)".format(feed_dict[x], feed_dict[y], output))