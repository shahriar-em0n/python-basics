username = "shahriar"

def func():
    username = "Build"
    print("Func username = ",username)
    
print("main username = ",username)
func()


x = 100

def func2(a):
    z = x + a
    print(z)
    return z

func2(5)


def func3():
    global x 
    x = 10
    
func3()
print(x)


def func4():
    x = 80
    def func5():
        print(x)
    func5()
    
func4()