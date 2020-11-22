from models.filter import Filter
class Parser:

    def __init__(self, data):
        self.data = data
        self.__parse()

    def __parse(self):
        #TODO: remove this workaround
        import os, ast
        with open('data.tmp', 'w') as f:
            f.write(self.data)
        self.parsed_data = ast.literal_eval(os.popen(f"ruby models/parser.rb data.tmp").read())
        os.system("rm data.tmp")
'''
    def __parse(self):
        """Extract numerical data into the format:
           [ [ [x1t, y1t, z1t] ], ..., [ [xnt, ynt, znt] ] ]
           OR
           [ [ [x1u, y1u, z1u], [x1g, y1g, z1g] ], ...,
             [ [xnu, ynu, znu], [xng, yng, zng] ] ]"""
        #TODO put it clearer and complete (raise exception if bad input, handle all cases):
        self.parsed_data = [[[float(coord) for coord in coords.split(',') if coords] for coords in datapoint.split('|')] for datapoint in self.data.split(';')]

        for datapoint in self.parsed_data:
            for coords in datapoint:
                    if len(coords)!=3:
                        raise ValueError('Bad Input. Ensure data is properly formatted.')

        if len(self.parsed_data[0])==1:
            # Low-pass filter combined acceleration into the following format:
            # [ [ [x1u, x2u, ..., xnu], [x1g, x2g, ..., xng] ],
            #   [ [y1u, y2u, ..., ynu], [y1g, y2g, ..., yng] ],
            #   [ [z1u, z2u, ..., znu], [z1g, z2g, ..., zng] ] ]

            self.parsed_data = [datapoint[0] if datapoint[0] else [0]*3 for datapoint in self.parsed_data]
            # [ [x1t, y1t, z1t] ] -> [ x1t, y1t, z1t ] for each line

            total_accl_coords = list(map(list, zip(*self.parsed_data)))
            # [ [ x1t, y1t, z1t ], [ x2t, y2t, z2t ], ..., [xnt, ynt, znt] ] -> [ [x1t, x2t, ..., xnt], [y1t, y2t, ..., ynt], [z1t, z2t, ..., znt] ]

            grav_accl_coords, user_accl_coords = [], []
            for total_accl_coord in total_accl_coords:
                grav_accl_datapoint = Filter.low_0_hz(total_accl_coord)
                grav_accl_coords.append(grav_accl_datapoint)
                user_accl_coords.append([t-g for t,g in zip(total_accl_coord,grav_accl_datapoint)])

            # Format filtered acceleration into the following format:
            # [ [ [x1u, y1u, z1u], [x1g, y1g, z1g] ], ...,
            #   [ [xnu, ynu, znu], [xng, yng, zng] ] ]
            self.parsed_data = list(map(list, zip(grav_accl_coords, user_accl_coords)))
'''
