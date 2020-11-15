#TODO: pytest or unittest?
from pydometer.models.parser import Parser

def test_new():
    data = '0.123,-0.123,5;0.456,-0.789,0.111;-0.212,0.001,1;'
    parser = Parser(data)
    #TODO:
    # assert parser.parsed_data==None

# --- Creation Tests ---

def test_create_combined_data():
    data = '0.123,-0.123,5;0.456,-0.789,0.111;-0.212,0.001,1;'
    parser = Parser(data)
    #TODO:
    # assert parser.parsed_data==[ [[0.123, -0.123, 5.0],   [0, 0, 0]],
    #  [[0.456, -0.789, 0.111], [0, 0, 0]],
    #  [[-0.2120710948533322, 0.0011468544965549535, 0.9994625125426089],
    #   [7.109485333219216e-05, -0.00014685449655495343, 0.0005374874573911294]]]

def test_create_separated_data():
    data = '0.028,-0.072,5|0.129,-0.945,-5;0,-0.07,0.06|0.123,-0.947,5;0.2,-1,2|0.1,-0.9,3;'
    parser = Parser(data)
    #TODO:
    # assert parser.parsed_data==[[[0.028, -0.072, 5], [0.129, -0.945, -5]],
    #   [[0, -0.07, 0.06],   [0.123, -0.947, 5]],
    #   [[0.2, -1.0, 2.0], [0.1, -0.9, 3.0]]]

def test_create_string_values_parses_to_0s():
    data = "1,2,foo;"
    parser = Parser(data)
    #TODO:
    # assert parser.parsed_data==[[[1.0, 2.0, 0.0], [0, 0, 0]]]

    data = "1,2,foo|4,bar,6;"
    parser = Parser(data)
    #TODO:
    # assert parser.parsed_data==[[[1.0, 2.0, 0.0], [4.0, 0.0, 6.0]]]

# --- Creation Failure Tests ---

def test_create_none():
    pass #TODO

def test_create_empty():
    pass #TODO

def test_create_bad_input_too_many_values():
    pass #TODO

def test_create_bad_input_too_few_values():
    pass #TODO

def test_create_bad_input_delimiters():
    pass #TODO
