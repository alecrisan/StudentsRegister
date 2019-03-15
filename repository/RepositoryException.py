'''
Created on Nov 12, 2017

@author: Ale
'''

class RepoException(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        """
        Overriding the str method
        output: a new string (the message we want to print)
        """
        return self.message