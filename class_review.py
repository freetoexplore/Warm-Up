# this is an example from browser
class Equation():

    def __init__(_):
    # global parameters
        a = int(input("Input 'a' for function f(x) = aX^2 + bX + c:"))
        b = int(input("Input 'b' for function f(x) = aX^2 + bX + c:"))
        c = int(input("Input 'c' for function f(x) = aX^2 + bX + c:"))
        g = 0 
    
    
    def Discriminants(_):
    # initial object is referred by 'self' or '_'

        _.g = _.b**2 - 4*_.a*_.c
        print('求和公式 =', _.b**2 - 4*_.a*_.c)
        
    
    def Root1(_):
        if _.b*_.b - 4*_.a*_.c >= 0:
            print((-_.b + _.g**0.5)/(2*_.a))
            
        else:
            print('No root for input formulation.')
            
    def Root2(_):
        if _.b*_.b - 4*_.a*_.c >= 0:
            print((-_.b - _.g**0.5)/(2*_.a))
            
        else:
            print('No root for input formulation.')
            
            
# Only global parameters are retrievable. Functions are not inter-callable. Because they served as sub-units under one class type.
# Keep in mind that defined objects are not reachable between defined functions.
def main():
    call_func = Equation()
    call_func.Discriminants() 
    call_func.Root1()
    call_func.Root2()

main()
