#!/usr/bin/env python

from time import sleep

from simtk.openmm.app import AmberPrmtopFile, AmberInpcrdFile
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
    def __init__(self, ff_type, **kwargs):
        if ff_type.lower() == "amber":
            prmtop = AmberPrmtopFile(kwargs["topology"])
            inpcrd = AmberInpcrdFile(kwargs["coordinates"])
            self.system = prmtop.createSystem(nonbondedMethod=NoCutoff)

    def save_xml(self, system_file):
        with open(system_file, "w") as f:
            f.write(XmlSerializer.serialize(self.system))

    def load_xml(self.xml_file):
        # TODO file access control
        attempt = 0
        retries = 10
        while True:
            try:
                with open(xml_file) as f:
                    self.system = XmlSerializer.deserialize(f.read())
                return
    
            except ValueError as e:
                if attempt < retries:
                    attempt += 1
                    sleep(5*random.random())
                else:
                    raise e

