#!/usr/bin/env python

from simtk import openmm

__all__ = ["OmmSimulation"]

class OmmSimulation(object):
     """OmmSimulation is a wrapper around the OpenMM Simulation object

    Initialized/returned by the OmmSystem class, acting as a factory. 

    Attributes
    ----------
    simulation   :: OpenMM `Simulation` instance

    Methods
    -------
    run ::
        run simulation, doesn't need any new parameters
	but will take them if user wants to change steps,
	reporters, etc.


    """

    @property
    def simulation(self):
        if not self._simulation:
            return None
        else:
            return self._simulation


    def __init__(self, omm_system, integrator, platform, sim_steps):
        self._simulation = openmm.app.Simulation(ommm_system.topology, omm_system.system, integrator, platform)
	self._simulation.context.setPositions(omm_system.initial_positions)
	self.sim_steps = sim_steps

    def run(statedata_freq=1000, structure_freq=10000, simulation_steps=self.sim_steps, simulation_file="simulation.pdb", tag=""):
        self._simulation.minimizeEnergy()

        self._simulation.reporters.append(app.StateDataReporter(sys.stdout, statedata_freq, separator=" | ", step=True,
            time=True, potentialEnergy=True, kineticEnergy=True, totalEnergy=True, temperature=True, speed=True))

        self._simulation.reporters.append((app.PDBReporter( simulation_file.format(tag), structure_freq)

        self._simulation.step(simulation_steps)


