# Area and Perimeter
def compare_rectangles(l1, b1, l2, b2):
    area1= l1*b1
    area2= l2*b2
    
    parameter1 =2*(l1+b1)
    parameter2 =2*(l2+b2)
    
    if area1>area2:
        print("true")
    else:
        print("false")
        
    if parameter1>parameter2:
        print("true")
    else:
        print("false")
compare_rectangles(2,3,6,5)