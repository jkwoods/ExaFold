
__all__ = [
    "OMM_INTEGRATOR"
]

from simtk import unit as u

# TODO expand to list of options

# FUNCTIONAL Encoding dicts
OMM_INTEGRATOR = dict(
    langevin=dict(
        CustomBondForce=dict(
            args=["100", "", ""], #temp, frictionCoeff, stepSize
            units=[
                u.kelvin,
                1/u.picoseconds, #inverse picoseconds
                0.002*u.picoseconds,
            ]
        ),
    ),

    brownian=dict(), #etc. figure out which integrators are applicable

)

