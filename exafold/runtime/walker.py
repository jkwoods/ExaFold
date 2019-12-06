
from .definitions import _default_omm_configuration
from ..mdsystem import OmmSystem
from . import integrate

import warnings

from simtk.openmm.app import Simulation
from simtk import openmm

__all__ = ["Walker"]

class Walker(object):
    '''Used to propagate a simulation instance
    associated to walker object.
    '''
    def __init__(self, simulation=None, configuration=None,
        integrator=None,):

        super(Walker, self).__init__()

        self._simulation    = simulation
        self._configuration = configuration
        self._integrator    = integrator
        self._platform      = None


    @property
    def configuration(self):
        return self._configuration


    @configuration.setter
    def configuration(self, configuration):

        if self.configuration is not None:
            self._configuration = configuration

        else:
            warning.warn(
                "Walker.configuration: attribute already set",
                Warning)


    @property
    def simulation(self):
        return self._simulation


    @simulation.setter
    def simulation(self, simulation):

        if self.simulation is not None:
            assert isinstance(simulation, Simulation)

            self._simulation = simulation

        else:
            warning.warn(
                "Walker.simulation: attribute already set",
                Warning)


    def go(self):
        self._simulation.step(
            self.configuration.n_steps
        )


    @property
    def platform(self):
        return self._platform


    @property
    def integrator(self):
        return self._integrator


    def create_platform(self, device=None):
        if device is None:
            device = _default_omm_configuration["device"]

        platform = openmm.Platform.getPlatformByName(device)


    def create_integrator(self, components):
        '''Integrator is created from the given components
        The actual timestep integrator name first or alone,
        then accesories such as barostat or thermostat.
        '''
        integrator = list()

        # first is the actual integrator
        # then additional components
        for _,component in components.items():

            if component:
                assert len(component) == 1

                nm,args  = list(component.items())[0]
                xaf_omm  = getattr(integrate, nm)()
                integrator.append(xaf_omm.create(**args))

        self._integrator = integrator


    def generate_simulation(self, system, device=None):

        assert isinstance(system, OmmSystem)

        if self.platform is None:
            self._platform = self.create_platform(device)

        if self.integrator is None:
            self.create_integrator(_default_omm_configuration)

        simulation = Simulation(
            system.topology,
            system,
            self.integrator,
            openmm.Platform("CUDA"),
            properties)

