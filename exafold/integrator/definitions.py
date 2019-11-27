
__all__ = [
    "OMM_INTEGRATOR"
]

from simtk import unit as u
from openmmtools import integrators # some of these are in openmmtools.integrators package - which is seperate


# TODO expand to list of options
# TODO enable user input for step size

# FUNCTIONAL Encoding dicts
OMM_INTEGRATOR = dict(
    langevin=dict( #most used, might be too slow
        # length 1 dict w/name of OpenMM Integrator class
        LangevinIntegrator=dict(
            args=["100", "1", "0.002"], #temp, frictionCoeff, stepSize
            units=[
                u.kelvin,
                1/u.picoseconds, #inverse picoseconds
                u.picoseconds,
            ]
        ),
    ),

    verlet=dict(
        VerletIntegrator=dict(
            args=["0.002"], #only stepSize
            units=[
                u.picoseconds,
            ]
        ),
    
    ),
    
        
    aMD=dict( 
        AMDIntegrator=dict( #supposedly very fast, might comprise accuracy
            args=["0.002", "-180590.8", "2721"], #stepSize, alpha, energy cutoff, where do these # come from? no idea
            units=[
                u.picoseconds, #the other two parameters don't seem to have units
            ]
        ),
    
    ),
    
    noseHoover=dict( #subclassed from CustomIntegrator in openmmtools, variation on verlet
        NoseHooverChainVelocityVerletIntegrator=dict(
            args=["300", "50", "0.001", "10", "5", "5"], #system (not listed), temperature, collision_frequency, timestep, chain_length, num_mts, num_yoshidasuzuki
            units=[
                u.kelvin, #temp
                1/u.picoseconds, #collision
                u.picoseconds, #timestep
            ]
        ),
    
    ),
        
    andersen=dict( #subclassed from CustomIntegrator in openmmtools, supposedly improves efficiency of verlet
        AndersenVelocityVerletIntegrator=dict(
            args=["300", "91", "0.001"], #temperature, collision_rate, timestep
            units=[
                u.kelvin, #temp
                1/u.picoseconds, #collision
                u.picoseconds, #timestep
            ]
        ),
    
    ),

)

