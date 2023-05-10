"""A solver for the 1D diffusion eqtn."""
import numpy as np

np.set_printoptions(formatter ={'float': '{: 5.1f}'.format}) # reduce dps


def solve1d(concentration, spacing,time_step, diffusivity):
    flux = -diffusivity * np.diff(concentration) / spacing
    #concentration[1:-1] = concentration[1:-1] - time_step * np.diff(flux) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing # -= takes care of the conc on the right hans side
    return(concentration)


def solve1d_2(C1, C2, spacing,time_step, diffusivity):
    C1 = 500
    C2 = 0
    Lx = 10
    concentration = np.empty(Lx)
    concentration[: int(Lx/2)] = C1
    concentration[int(Lx/2) :] = C2
    flux = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] = concentration[1:-1] - time_step * np.diff(flux) / spacing
    #concentration[1:-1] -= time_step * np.diff(flux) / spacing # -= takes care of the conc on the right hans side
    return(concentration)
    
def _example(): # '_' says ignore
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    #print(C)

    for _ in range(1,5): #' _' place holder for loop counter
        C = solve1d(C, dx, dt, D)
        print(C)

def _example2(C1 = 500, C2 = 0): # '_' says ignore
    D = 100
    Lx = 10
    dx = 0.5
    #C1 = 500
    #C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    #print(C)

    for _ in range(1,5): #' _' place holder for loop counter
        C = solve1d(C, dx, dt, D)
        print(C)

        
        
if __name__ == "__main__":
    _example()
    
#for _ in range(1,5):
    #C = solve1d_2(500, 0, 0.5, 0.5 * 0.5 / 100 / 2.1, 100) # use the generic function - provide 2 concentrations to calculate diff??
    #print(C)
    
#print(_example2)