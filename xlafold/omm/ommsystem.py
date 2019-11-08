#!/usr/bin/env python

from time import sleep

from simtk.openmm.app import AmberPrmtopFile, AmberInpcrdFile, NoCutoff
from simtk.openmm import XmlSerializer


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
    def __init__(self, ff_type=None, system_file=None, **kwargs):
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

    def save_xml(self, system_file):
        with open(system_file, "w") as f:
            f.write(XmlSerializer.serialize(self.system))

    def load_xml(self, system_file):
        # TODO file access control
        attempt = 0
        retries = 10
        while True:
            try:
                with open(system_file) as f:
                    self.system = XmlSerializer.deserialize(f.read())
                return
    
            except ValueError as e:
                if attempt < retries:
                    attempt += 1
                    sleep(5*random.random())
                else:
                    raise e

