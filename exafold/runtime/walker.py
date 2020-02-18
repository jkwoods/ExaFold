
from .definitions import _default_omm_configuration, _amber_test_configuration, _default_rt_configuration
from .configuration import Configuration
from ..mdsystem import OmmSystem
from . import integrate

import warnings

from simtk.openmm.app import Simulation, StateDataReporter, DCDReporter, PDBReporter
from simtk import openmm
from simtk import unit as u

__all__ = ["Walker"]

class Walker(object):
    '''Used to propagate a simulation instance
    associated to walker object.
    '''
    def __init__(self, simulation=None, configuration=None,
        integrator=None,):

        super(Walker, self).__init__()

        self._simulation    = simulation
        self._integrator    = integrator
        self._platform      = None
        self._properties    = None

        if configuration is None:
            self._configuration = Configuration()


    def add_reporters(self):

        self.simulation.reporters.append(PDBReporter("output.pdb", 5000))

        if self.configuration.fn_state:
            self.simulation.reporters.append(
                StateDataReporter(
                    self.configuration.fn_state,
                    self.configuration.fr_save,
                    step=True,
                    potentialEnergy=True,
                    kineticEnergy=True,
                    totalEnergy=True,
                    temperature=True,
                    separator="  ||  ",
                    volume=True,
                    density=True,
                    speed=True,
            ))

        if self.configuration.fn_state:
            self.simulation.reporters.append(
                DCDReporter(
                    self.configuration.fn_traj,
                    self.configuration.fr_save,
            ))


    def configure_walk(self, cfg=None):
        if cfg:
            self.configuration.configure(cfg)

        self.add_reporters()

        # Poor-mans version of properties on Walker
        # instances to corresponding Configuration fields
        #  - i.e. read-only attributessd;
        #  - TODO it's still like a method
        def _property(key):
            return lambda: getattr(self.configuration, key)

        for field in self.configuration._fields:
            self.__dict__[field] = _property(field)


    @property
    def configuration(self):
        return self._configuration


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


    def go(self, distance_force, torsion_force):
        """Fire off the walker
        """        
        cycles = 20 #don't take user information for this is has to be tuned super perfectly
        t = [36,72,108,144,180,216,252,288,324,360,480,600,562,524,486,448,410,372,334,296,258,220,182,144,106,53,0]#([(400//10)*i for i in range(1,11)]+[500,600]+[(550//13)*i+100 for i in range(12, -1, -1)]+[50,0])
        c = [400,400,400,400,400,400,400,400,400,400,400,400,2000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,400,100,50]#(12*[400])+[2000]+(11*[4000])+[1000,100,50]
        temp_series = iter(cycles*t)
        coll_series = iter(cycles*c)
        assert len(t) == len(c)
        print(t)
        print(c)
        vlimit = 5 #1 nm = 10 angstroms; amber is 10 angstroms

	#TODO enable the turning off of rst
        self._simulation.context.setParameter("k", 0.0)
        self._simulation.context.setParameter("a", 0.0)

        step = 0
        done = False
        increment = 0.0
        while not done:
            try:

                self._simulation.context.setParameter('AndersenTemperature', next(temp_series)) #TEMP FIX - TODO change
                self._simulation.context.setParameter('AndersenCollisionFrequency', next(coll_series)) #TEMP FIX

                if (increment < 1):
                    increment += 0.1

                    self._simulation.context.setParameter("k", distance_force*increment)  
                    self._simulation.context.setParameter("a", torsion_force*increment)


                    self._simulation.step(1000)
                    step += 1000

                else:
                    self._simulation.step(2000)


                current_velocities = self._simulation.context.getState(getVelocities=True).getVelocities()
                #vlimit logic - there are some issues here
                '''
                changed = False
                for i,v in enumerate(current_velocities):
                    nx = v[0]/(u.nanometer/u.picoseconds)
                    ny = v[1]/(u.nanometer/u.picoseconds)
                    nz = v[2]/(u.nanometer/u.picoseconds)
                    changed_v = False
                    if (nx > vlimit):
                        nx = vlimit
                        changed_v = True
                    if (ny > vlimit):
                        ny = vlimit
                        changed_v = True
                    if (nz > vlimit):
                        nz = vlimit
                        changed_v = True
                    #negatives
                    if (nx < -1*vlimit):
                        nx = -1*vlimit
                        changed_v = True
                    if (ny < -1*vlimit):
                        ny = -1*vlimit
                        changed_v = True
                    if (nz < -1*vlimit):
                        nz = -1*vlimit
                        changed_v = True
                    if changed_v:
                       current_velocities[i] = openmm.Vec3(x=nx, y=ny, z=nz)*(u.nanometer/u.picoseconds)
                       changed = True


                if changed:
                    self._simulation.context.setVelocities(current_velocities)
                    print("Velocities reset at " + str(step) + ":\n")i
                '''
            except StopIteration:
                done = True


    @property
    def properties(self):
        return self._properties


    @property
    def platform(self):
        return self._platform


    @property
    def integrator_components(self):
        if len(self._integrator) > 1:
            return self._integrator[1:]
        else:
            return []


    @property
    def integrator(self):
        if self._integrator:
            return self._integrator[0]
        else:
            return []


    def create_platform(self, device=None):
        if device is None:
            device = _default_omm_configuration["device"]

        self._platform = openmm.Platform.getPlatformByName(device)


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

    def generate_simulation(self, system):

        assert isinstance(system, OmmSystem)

        if not self.platform:
            self._platform = self.create_platform(
                _default_rt_configuration["device"])

        if not self.integrator:
            self.create_integrator(
                _amber_test_configuration)  #TODO change back when figured out

        if (len(self.integrator_components) > 0):
            for component in self.integrator_components:
               getattr(system.system, "addForce")(component)

        self._simulation = Simulation(
            system.topology.to_openmm(),
            system.system,
            self.integrator,
            self.platform,)
            #self.properties)

        initial_positions = system.initial_positions
        self.set_positions(initial_positions)


    def set_positions(self, positions):
        self._simulation.context.setPositions(positions)

