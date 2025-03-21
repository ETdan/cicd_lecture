from cicd import hello

def test():
    assert hello("world") == "hello world"
    assert hello("") == "hello "
    
    print("all tests pass")
