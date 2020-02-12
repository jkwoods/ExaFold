__all__ = ["LangevinIntegrator", "VerletIntegrator", "AndersenThermostat"]


from .component import TimestepComponent
from simtk import unit as u

# OpenMM integrators with simple call signature
# give argument names and corresponding simtk units
# as fields of each integrator dict
class LangevinIntegrator(TimestepComponent):

    # This list of 2-tuples defines the init signature
    # for the underlying OMM object. We cannot give
    # kwargs for some reason, they must be positional
    # args so this list lets us easily bind arguments
    # later via kwargs that will automatically be put
    # in the correct order (see TimesteComponent.create
    # method definition).
    kwargs = [
        ("temperature"  , u.kelvin),
        ("frictionCoeff", 1/u.picosecond),
        ("stepSize"     , u.femtosecond),
    ]

    # Copy this and replace "LangevinIntegrator" with
    # the name of whatever similar barostat/thermostat/
    # integrator class from OMM to create addition
    # exafold wrappers.
    def __init__(self):
        super(LangevinIntegrator, self).__init__(
            "LangevinIntegrator", LangevinIntegrator.kwargs)

class VerletIntegrator(TimestepComponent):

    kwargs = [
        ("stepSize"	, u.femtosecond),
    ]

    def __init__(self):
        super(VerletIntegrator, self).__init__(
            "VerletIntegrator", VerletIntegrator.kwargs) 

class VariableVerletIntegrator(TimestepComponent):

    kwargs = [
        ("errorTol"     , 1), #no units
    ]

    def __init__(self):
        super(VariableVerletIntegrator, self).__init__(
            "VariableVerletIntegrator", VariableVerletInegrator.kwargs) 


class AndersenThermostat(TimestepComponent):

    kwargs = [
        ("defaultTemperature"     	, u.kelvin),
        ("defaultCollisionFrequency"	, 1/u.picosecond),
    ]

    def __init__(self):
        super(AndersenThermostat, self).__init__(
            "AndersenThermostat", AndersenThermostat.kwargs)

# TODO update these to use the TimestepComponent parent
#      class following the LangevinIntegrator example.
'''
AndersenThermostat     = dict(
    defaultTemperature = u.kelvin,
    defaultCollisionFrequency = 1/u.picosecond,
)
'''
MonteCarloBarostat     = dict(
    defaultPressure    = u.bar,
    defaultTemperature = u.kelvin,
    frequency          = 1, # this one in MD timesteps
)

# TODO the interweb is not clear on wether this is
#      a good practice or not... I like it
del u
del TimestepComponent
