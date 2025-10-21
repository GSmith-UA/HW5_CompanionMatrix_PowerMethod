import numpy as np
import powerMethod as pm
import synthDiv as sd

def constructCompanionMatrix(coeffVec):
    # Returns an np matrix that is the companion matrix for the given polynomial coeff
    # Coefficients must be ordered as [c_0,c_1,c_2,c_3,...c_{n-1}]: this is the users responsibility
    # Note that these polynomials must be monic so the c_n coeff need not be given
    n = len(coeffVec)
    A = np.eye(n - 1, dtype=float) # Start with an identity matrix
    # Now I concatenate the first col and last row
    A = np.concatenate((np.zeros((n-1,1),dtype=float),A),axis=1)
    A = np.concatenate((A,np.array(coeffVec,ndmin=2)),axis=0)
    # Negate the last row...
    A[n-1,:] = -1*A[n-1,:]
    return A



def main():
    # Here is problem 2.1 given is the polynomial below:
    # It is the users responsibility to make sure the coeffecients are formatted correctly before passing to the constructor
    p = [6,-5,2,-3,0,1]
    C_p = constructCompanionMatrix(p[:len(p)-1])
    print("Here is the constructed companion matrix:")
    print( C_p)
    # Here is problem 2.2
    n = len(p) - 1
    roots,trust = pm.powerMethod_deflation(C_p,3,np.ones((n,1),dtype=float))

    print("**********Roots Finding From Power Method************")
    print("|------Root----------|--Trust--|")
    print("| ",roots[0].item(),"| ", trust[0],"  |")
    print("| ",roots[1].item(),"| ", trust[1],"  |")
    print("| ",roots[2].item()," | ", trust[2],"  |")

    # Here is problem 2.3
    # np.ndaSrray.flatten(roots)
    # roots = list(roots)
    reducedP,remainder = sd.synthDiv_multiple(p,roots)

    # Run the quad solver on the reduced polynomial
    # My multiple sythDiv function should print an error if you it ever finds a remainder far from 0
    x1,x2 = sd.quadSolver(reducedP)
    roots.append(x1)
    roots.append(x2)
    print("***********ALL ROOTS FOUND***********")
    for r in roots:
        print("Root Found: r = ", r.item())
    return None

main()