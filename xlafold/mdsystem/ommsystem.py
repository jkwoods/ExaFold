#!/usr/bin/env python

from time import sleep

from simtk.openmm.app import AmberPrmtopFile, AmberInpcrdFile, NoCutoff
from simtk import openmm


__all__ = ["OmmSystem"]


class OmmSystem(object):
    """OmmSystem is a wrapper around the OpenMM System object
    that does a bunch of simple stuff for us with simpler API

    Attributes
    ----------
    system :: OpenMM `system` instance

    Methods
    -------
    """

    @property
    def restraints(self):
        """dict with the API calls, atom groups and force
        parameters needed to generate all the given restraints
        """
        return self._restraints


    def __init__(self, ff_type=None, system_file=None, **kwargs):

        # This dict will store the API calls
        # along with atom groups and force
        # parameters needed to generate all
        # the given restraints
        self._restraints = dict()

        if ff_type is not None:
            if ff_type.lower() == "amber":
                prmtop = AmberPrmtopFile(kwargs["topology"])
                inpcrd = AmberInpcrdFile(kwargs["coordinates"])
                self.system = prmtop.createSystem(nonbondedMethod=NoCutoff)

        elif system_file is not None:
            self.load_xml(system_file)

        else:
            # Inspect and set ff_type
            # TODO ff_type as instance attribute
            pass


    def initialize_restraint_force(self, restraint_definition, atom_groups=list(), parameters=list()):
        assert len(restraint_definition) == 1
        assert isinstance(restraint_definition, dict)

        # PROGRAMMATIC use of the dict fields happens here
        restraint_type    = list(restraint_definition)[0]
        rd                = restraint_definition[restraint_type]
        restraint_formula = rd.get("formula", list())
        restraint_pars    = rd.get("parameters", list())
        restraint_method  = rd.get("restraint", dict())

        restraint_force   = getattr(openmm, restraint_type)(*restraint_formula)
    
        for mpar in restraint_pars:
            assert len(mpar) == 1
            method,parameter = next(iter(mpar.items()))
            getattr(restraint_force, method)(*parameter)

        self._restraints.update(
            {restraint_type : [restraint_force, restraint_method]}
        )

        if atom_groups and parameters:
            self.add_restraint_groups(restraint_type, atom_groups, parameters)


    def add_restraints(self, restraint_type, atom_groups, parameters):

        assert isinstance(atom_groups, (list, tuple))
        assert isinstance(parameters, (list, tuple))

        restraint_force, restraint_method = self._restraints[restraint_type]

        for restraint in zip(atom_groups, parameters):
            rargs = restraint[0]
            rargs.append(restraint[1])
            getattr(restraint_force, restraint_method)(*rargs)


    def save_xml(self, system_file):
        with open(system_file, "w") as f:
            f.write(openmm.XmlSerializer.serialize(self.system))


    def load_xml(self, system_file):
        attempt = 0
        retries = 20
        while True:
            try:
                with open(system_file) as f:
                    self.system = openmm.XmlSerializer.deserialize(f.read())
                return
    
            except ValueError as e:
                if attempt < retries:
                    attempt += 1
                    sleep(5*random.random())
                else:
                    raise e

