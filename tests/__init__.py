from db import seed

def teardown_module(module):
    """ setup any state specific to the execution of the given module."""
    seed()
