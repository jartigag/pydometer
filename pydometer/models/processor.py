from pydometer.models.filter import Filter

class Processor:

    def __init__(self, data):
        self.data = data
        self.__dot_product()
        self.__filter()

    def __dot_product(self):
        self.dot_product_data = None
        #TODO: rewrite and add input control from:
        # @dot_product_data = @data.map do |x|
        #   x[0][0] * x[1][0] + x[0][1] * x[1][1] + x[0][2] * x[1][2]
        # end

    def __filter(self):
        self.filtered_data = Filter.low_5_hz(self.dot_product_data)
        self.filtered_data = Filter.low_1_hz(self.filtered_data)
