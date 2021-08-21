from grey.pyparser import parse_function, parse_class

def test_func_parser():
    function = """def test1(a, *args, kw1, **kwargs) -> 'xyz': pass"""
    funcname, params, ret_annotation = parse_function(function)

    assert(funcname == 'test1')
    assert(len(params)==4)
    assert(params[0]['name']=='a')
    assert(ret_annotation='xyz')

def test_func_parser_with_extensible_arguments():
    function = """def test2(a, *, b, c, **kwargs) -> 'xyz': pass"""
    funcname, params, ret_annotation = parse_function(function)
    assert(funcname == 'test2')
    assert(len(params)==4)
    assert(params[0]['name']=='a')
    assert(ret_annotation='xyz')

def test_func_parser_with_typing():
    function = """def test3(a, b: typing.Tuple[typing.Int, typing.Int],
                           c: int=123, d=3+11.23j, e='abc', **kw) -> 'xyz':
                     pass"""
    funcname, params, ret_annotation = parse_function(function)
    assert(funcname == 'test3')
    assert(len(params)==4)
    assert(params[0]['name']=='a')
    assert(ret_annotation='xyz')


def test_class_parser():
    cls = """class ABC123(str, int): pass"""
    classname, base_classes = parse_class(cls)
    assert(classname=='ABC123')
    assert(len(base_classes)==2)
    assert('str' in base_classes)
