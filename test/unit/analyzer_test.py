#TODO: pytest or unittest?
from pydometer.models.parser import Parser
from pydometer.models.processor import Processor
from pydometer.models.analyzer import Analyzer
from pydometer.models.user import User
from pydometer.models.trial import Trial

def test_new():
    analyzer = Analyzer([0, 0], User(), Trial('walk1'))

# --- Creation Tests ---

def test_create():
    data = [0, 0, 3.0950446845522207e-05, 8.888784491236883e-05,
            0.00017675661757108235, 0.0003010710258273255,
            0.0004670334044406543, 0.0006857659826903315]
    analyzer = Analyzer(data, User(), Trial('walk1'))
    #TODO
    # assert analyzer.delta==None
    # assert analyzer.time==None
    # assert analyzer.steps==0
    # assert analyzer.distance==0

def test_create_non_zero_data():
    user = User('female', 167, 70)
    trial = Trial('walk 1', 100, 18)
    parser = Parser(open('test/data/female-167-70_walk2-100-10.txt').read())
    processor = Processor(parser.parsed_data)
    analyzer = Analyzer(processor.filtered_data, user, trial)
    #TODO
    # assert analyzer.steps==10
    # assert analyzer.delta==-8
    # assert analyzer.distance==700
    # assert analyzer.time==1037/100
