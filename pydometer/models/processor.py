from pydometer.models.filter import Filter

class Processor:

    def __init__(self, data):
        self.data = data
        self.__dot_product()
        self.__filter()

    def __dot_product(self):
        self.dot_product_data = [ d[0][0]*d[1][0] + d[0][1]*d[1][1] + d[0][2]*d[1][2] if any(d) else 0 for d in self.data]

    def __filter(self):
        self.filtered_data = Filter.low_5_hz(self.dot_product_data)
        self.filtered_data = Filter.high_1_hz(self.filtered_data)
