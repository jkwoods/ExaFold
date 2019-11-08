
from time import sleep
from simtk.openmm import XmlSerializer

def system_from_xml(xml_file):
    # TODO file access control
    attempt = 0
    retries = 10
    while True:
        try:
            with open(xml_file) as f:
                system = XmlSerializer.deserialize(f.read())
            return system

        except ValueError as e:
            if attempt < retries:
                attempt += 1
                sleep(5*random.random())
            else:
                raise e
