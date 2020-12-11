import numpy as np
from polyfit import polyfit 

def regress(i,out,deg):
    '''
    Description: sets up a polynomial regress w/ lists and labels for visualization
    Parameters: x is input variable (a list of indepedent values)
                y is output variable (a list of dependent values)
                degree order of polynomial to fit x to y
    '''
    
    results = polyfit(i,out,deg)

    txt = 'r_sq: %.4f' % results['determination']
    p = np.poly1d(results['polynomial'])
    x = np.arange(min(i),max(i),0.01)
    y = p(x)
    
    return txt,p,x,y

