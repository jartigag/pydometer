from pydometer.models.parser import Parser
from pydometer.models.processor import Processor
from pydometer.models.analyzer import Analyzer

class Pipeline:

    def __init__(self, data, user, trial):
        self.data = data
        self.user = user
        self.trial = trial
        self.parser, self.processor, self.analyzer = [None]*3
        self.feed()

    def feed(self):
        self.parser = Parser(self.data)
        self.processor = Processor(self.parser.parsed_data)
        self.analyzer = Analyzer(self.processor.filtered_data, self.user, self.trial)
