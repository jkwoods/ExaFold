
from .component import TimestepComponent
from simtk import unit as u

# OpenMM integrators with simple call signature
# give argument names and corresponding simtk units
# as fields of each integrator dict
class LangevinIntegrator(TimestepComponent):

    kwargs = [
        ("temperature"  , u.kelvin),
        ("frictionCoeff", 1/u.picosecond),
        ("stepSize"     , u.femtosecond),
    ]

    def __init__(self):
        super(LangevinIntegrator, self).__init__(
            "LangevinIntegrator", LangevinIntegrator.kwargs)

# TODO update these to use the TimestepComponent parent
#      class following the LangevinIntegrator example
AndersenThermostat     = dict(
    defaultTemperature = u.kelvin,
    defaultCollisionFrequency = 1/u.picosecond,
)

MonteCarloBarostat     = dict(
    defaultPressure    = u.bar,
    defaultTemperature = u.kelvin,
    frequency          = 1, # this one in MD timesteps
)

del u
