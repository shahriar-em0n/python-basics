def my_sum(*args):
    print(args)
    
    for i in args:
        print(i * 2)
        
    return sum(args)

print(my_sum(2, 4))   

print(my_sum(1,2,3))
