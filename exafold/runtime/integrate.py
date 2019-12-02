
# TODO too ugly...
__all__ = [
    "OMM_INTEGRATORS",
    "OMM_BAROSTATS",
    "OMM_THERMOSTATS",
]

from simtk import unit as u

# OpenMM integrators with simple call signature
# give argument names and corresponding simtk units
# as fields of each integrator dict
OMM_INTEGRATORS        = dict(
    LangevinIntegrator = dict(
        temperature    = u.kelvin,
        frictionCoeff  = 1/u.picosecond,
        stepSize       = u.femtosecond,
    ),
)

OMM_THERMOSTATS            = dict(
    AndersenThermostat     = dict(
        defaultTemperature = u.kelvin,
        defaultCollisionFrequency = 1/u.picosecond,
    ),
)

OMM_BAROSTATS              = dict(
    MonteCarloBarostat     = dict(
        defaultPressure    = u.bar,
        defaultTemperature = u.kelvin,
        frequency          = 1, # this one in MD timesteps
    ),
)
