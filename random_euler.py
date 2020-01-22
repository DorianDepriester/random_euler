import numpy as np
from scipy import stats

def mat2euler(M):
		Phi = np.arccos(M[2,2])
		if Phi == 0.0:
			phi1 = np.arctan2(-M[1,0], M[0,0])
			phi2 = 0.0	
		elif Phi == np.pi:
			phi1 = np.arctan2(M[1,0], M[0,0])
			phi2 = 0.0
		else:
			phi1 = np.arctan2(M[2,0], -M[2,1])
			phi2 = np.arctan2(M[0,2], M[1,2])
		if phi1 < 0.0:
			phi1 += 2*np.pi
		if phi2 < 0.0:
			phi2 += 2*np.pi
		return phi1,Phi,phi2    

def random_euler(n=1,**kwargs):
    M = stats.special_ortho_group.rvs(dim=3,size=n,**kwargs)
    if n==1:
        return mat2euler(M)
    else:
        return [mat2euler(M[i,:,:]) for i in range(0,n)]
