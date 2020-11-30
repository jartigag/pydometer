from models.filter import Filter
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

        def cast_to_float(string):
            try:
                return float(string)
            except ValueError:
                return 0.0

        # convert string data to numerical data in the standard format: [[[x1u, y1u, z1u], [x1g, y1g, z1g]], ..., [[xnu, ynu, znu], [xng, yng, zng]]]
        self.parsed_data = [[[cast_to_float(coord) for coord in coords.split(',') if coords] for coords in datapoint.split('|')] for datapoint in self.data.split(';')]

        # remove empty lists:
        for i,datapoint in enumerate(self.parsed_data):
            if not datapoint[0]:
                del self.parsed_data[i]

        for datapoint in self.parsed_data:
            for coords in datapoint:
                    if coords and len(coords)!=3:
                        raise ValueError('Bad Input. Ensure data is properly formatted.')

        if len(self.parsed_data[0])==1:
        # so this data is in the combined format

            ##1. use a low-pass filter to split combined acceleration into user acceleration and gravitational acceleration, like this:
            # [ [ [x1u, x2u, ..., xnu], [x1g, x2g, ..., xng] ],
            #   [ [y1u, y2u, ..., ynu], [y1g, y2g, ..., yng] ],
            #   [ [z1u, z2u, ..., znu], [z1g, z2g, ..., zng] ] ]

            # to do that, we need to:
            # - extract gravitational acceleration from combined acceleration, applying the low-pass filter
            # - substract gravitational acceleration from total acceleration, in order to get the user acceleration

            # [ [x1t, y1t, z1t] ] -> [ x1t, y1t, z1t ] for each line
            self.parsed_data = [datapoint[0] for datapoint in self.parsed_data]

            # transpose combined acceleration coordenates arrays:
            # [ [ x1t, y1t, z1t ], [ x2t, y2t, z2t ], ..., [xnt, ynt, znt] ] -> [ [x1t, x2t, ..., xnt], [y1t, y2t, ..., ynt], [z1t, z2t, ..., znt] ]
            combined_accl_coords_arrays = list(map(list, zip(*self.parsed_data)))

            user_accl_coords, grav_accl_coords = [], []
            for combined_accl_coord_array in combined_accl_coords_arrays:
                grav_accl_datapoint = Filter.low_0_hz(combined_accl_coord_array)
                grav_accl_coords.append(grav_accl_datapoint)
                user_accl_coords.append([t-g for t,g in zip(combined_accl_coord_array,grav_accl_datapoint)])

            ##2. reorganize the filtered acceleration into the following standard format:
            # [ [ [x1u, y1u, z1u], [x1g, y1g, z1g] ], ...,
            #   [ [xnu, ynu, znu], [xng, yng, zng] ] ]

            # transpose user and gravitational acceleration coordenates arrays back:
            # [ [ x1u, x2u, ..., xnu ], [ y1u, y2u, ..., ynu ], [ z1u, z2u, ..., znu ] ] -> [ [x1u, y1u, z1u], [x2u, y2u, z2u], ..., [xnu, ynu, znu] ]
            # [ [ x1g, x2g, ..., xng ], [ y1g, y2g, ..., yng ], [ z1g, z2g, ..., zng ] ] -> [ [x1g, y1g, z1g], [x2g, y2g, z2g], ..., [xng, yng, znu] ]
            user_accl_coords = list(map(list, zip(*user_accl_coords)))
            grav_accl_coords = list(map(list, zip(*grav_accl_coords)))

            self.parsed_data = list(map(list, zip(user_accl_coords, grav_accl_coords)))
