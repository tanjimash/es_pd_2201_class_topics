# Global Variable in a  Function 


# var_test = 500  # global scope

def test():
    global var_test
    var_test = 10    
    print('From "test1" function:', var_test)

test()

var_test += 500

def test2():
    print('From "test2" function:', var_test)
test2()
