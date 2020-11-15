from pydometer.models.filter import Filter

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
        #TODO put it clearer:
        self.parsed_data = [[[float(coord) for coord in coords.split(',') if coords] for coords in datapoint.split('|')] for datapoint in self.data.split(';')]
