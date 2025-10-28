import app

def test_add_num():
    assert app.add_num(5,3)==8
    assert app.add_num(-2,2)==0
    assert app.add_num(0,0)==0