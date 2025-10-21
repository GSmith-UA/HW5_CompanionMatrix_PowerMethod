import cmath

def synthDiv(coeffVec,root):
    # Input the full coeff vector... [c_0, c_1, ... c_{n-1}, c_n]
    # Going to return a vector that is one element smaller since synthetic divison will kill one root...
    newPoly = []
    remainder = None

    # Pulled from appendix H
    n = len(coeffVec)
    newPoly = [0]*n
    newPoly[n-1] = coeffVec[n-1]
    for i in range(n-2,-1,-1):
        
        newPoly[i] = coeffVec[i] + root*newPoly[i+1]
        # print(newPoly)

    # print("Before pop? poly = ", newPoly)
    remainder = newPoly[0]
    newPoly = newPoly[1:]

    return newPoly, remainder  


def synthDiv_multiple(coeffVec,roots):
    # Takes in the coeffVector = [c_0,c_1,... c_n] and multiple roots we want to divide out...
    remainder = None

    numerator = coeffVec
    for i in range(0,len(roots)):
        r = roots[i]
        updatedPoly, remainder = synthDiv(numerator,r)
        if remainder > 1e-3: 
            print("Something wrong!! remainder neq 0")
            print(remainder)
            return updatedPoly, remainder
        numerator = updatedPoly
    # Had some trouble here bc Python is not strongly typed: trying to grab the values in the ndarrays not the ndarrays    
    returnVal = []
    for n in numerator:
        returnVal.append(numerator[0][0])
    
    return returnVal,remainder

def quadSolver(coeffVec):
    if (len(coeffVec)) != 3:
        raise ValueError("You did not input a quadratic!!")
    
    # print(coeffVec[0])
    # print(coeffVec[1])
    # Find better way to compute the roots
    x1 = (-1*coeffVec[1] + cmath.sqrt((coeffVec[1]**2 - 4*coeffVec[2]*coeffVec[0])))/(2*coeffVec[2])
    x2 = (-1*coeffVec[1] - cmath.sqrt((coeffVec[1]**2 - 4*coeffVec[2]*coeffVec[0])))/(2*coeffVec[2])
    return x1,x2    




