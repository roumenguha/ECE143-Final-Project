import numpy as np

def polyfit(x, y, degree):
    '''
    Description: returns the results of the numpy polyfit function
                    polynomial regression
    Parameters: x is input variable (a list of indepedent values)
                y is output variable (a list of dependent values)
                degree order of polynomial to fit x to y
    '''
    results = {}

    coeffs = np.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                      # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results

def regress(i, out, deg):
    '''
    Description: sets up a polynomial regress w/ lists and labels for visualization
    Parameters: x is input variable (a list of indepedent values)
                y is output variable (a list of dependent values)
                degree order of polynomial to fit x to y
    '''
    
    results = polyfit(i, out, deg)

    txt = 'r_sq: %.4f' % results['determination']
    p = np.poly1d(results['polynomial'])
    x = np.arange(min(i), max(i), 0.01)
    y = p(x)
    
    return txt,p,x,y

