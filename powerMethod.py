import numpy as np
from scipy import linalg

def powerMethod_deflation(A, eigNumber, xInit, maxIter=1000, tol=1e-6):
    # Runs power method with deflation to return multiple eigenvalues
    # Since the powerMethod might exit with an eigenvalue out of spec I return a boolean that can be checked to see which are within tolerance
    # These booleans are then stored in the trustList so they can be queried as needed
    eigList = []
    trustList = []
    
    A_it = A
    for i in range(eigNumber):
        lam, v, goodExit = powerMethod_standard(A_it,xInit)
        eigList.append(np.ndarray.flatten(lam))
        trustList.append(goodExit)
        outerProd = np.outer(v,v)
        A_it = A_it - lam*outerProd
        # A_it = A_it - lam*(np.array(v,ndmin=2)@np.transpose(np.array(v,ndmin=2)))

    return eigList,trustList

def powerMethod_standard(A, xInit, maxIter = 1000, tol=1e-6):
    # Runs singular instance of power method to return the leading eigenvalue
    # Also returns boolean to check for good vs bad exit
    eig = None
    goodExit = False
    x_current = np.array(xInit,dtype=float,ndmin=2)
    
    for k in range(0,maxIter):
        y = A@x_current
        x_new = (1/np.linalg.norm(y))*y
        # print(np.shape(A))
        # print(A)
        # print(x_new)
        # print(np.shape(x_new))
        eigNew = np.transpose(x_new)@A@x_new

        # This checks to see how much our eigenvalue is changing... if only a little we have probably converged
        # Consider what the tolerance should be here... maybe better to check the eigen vector??
        if (k>0) and (np.abs(eigNew - eig) < tol):
            eig = eigNew
            goodExit = True
            return eig, x_new, goodExit
        
        eig = eigNew
        x_current = x_new

    return eig, np.ndarray.flatten(x_new), goodExit
