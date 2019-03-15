'''
Created on Nov 22, 2017

@author: Ale
'''
class UIException(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message