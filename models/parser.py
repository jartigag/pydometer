from filter import Filter

class Parser:

    def __init__(self, data):
        self.data = data
        self.__parse()

    def __parse(self):
        """Extract numerical data into the format:
           [ [ [x1t, y1t, z1t] ], ..., [ [xnt, ynt, znt] ] ]
           OR
           [ [ [x1u, y1u, z1u], [x1g, y1g, z1g] ], ...,
             [ [xnu, ynu, znu], [xng, yng, zng] ] ]"""
        self.parsed_data = self.data #TODO
