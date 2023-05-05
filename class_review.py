# this is an example from browser to resolve quadratic equation
class Equation():

    # global parameters
    def __init__(_):
        _.a = int(input("Input 'a' for function f(x) = aX^2 + bX + c:")) # 1
        _.b = int(input("Input 'b' for function f(x) = aX^2 + bX + c:")) # -5
        _.c = int(input("Input 'c' for function f(x) = aX^2 + bX + c:")) # 6
        _.g = 0 # 求根公式定值，不需要输入覆盖
    
    
    def Discriminants(_):
    # initial object is referred by 'self' or '_'
    # you may think it defined as a linkage from global parameter and called object

        _.g = _.b**2 - 4*_.a*_.c
        print('求和公式(roots) =', _.b**2 - 4*_.a*_.c)
        
    # Only global parameters are retrievable. 
    # Don't trespass by tele-call functions/objects b/w defined functions. 
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
            
            
# call functions
def main():
    call_func = Equation()
    call_func.Discriminants() # remember to call 求根公式(roots) to activate function _.g
    call_func.Root1()
    call_func.Root2()

main()
