
__all__ = [
    "OMM_INTEGRATOR"
]

from simtk import unit as u

# TODO expand to list of options
# TODO enable user input for step size

# FUNCTIONAL Encoding dicts
OMM_INTEGRATOR = dict(
    langevin=dict(
        # length 1 dict w/name of OpenMM Integrator class
        LangevinIntegrator=dict(
            args=["100", "1", "0.002"], #temp, frictionCoeff, stepSize
            units=[
                u.kelvin,
                1/u.picoseconds, #inverse picoseconds
                0.002*u.picoseconds,
            ]
        ),
    ),

    verlet=dict(
        LangevinIntegrator=dict(
            args=["100", "1", "0.002"], #temp, frictionCoeff, stepSize
            units=[
                u.kelvin,
                1/u.picoseconds, #inverse picoseconds
                0.002*u.picoseconds,
            ]
        ),
    
    ), # other applicable integrators ? TODO

)

