
__all__ = ["read_restraints"]

# TODO update docstrings, we are not returning 2 lists
#      anymore but rather the native format for using
#      with restraint definitions in OpenMM
#      (a heterogeneous list with particles, something
#      else maybe, and force constants)
# TODO reconsider the all-caps silly things that now
#      seem like user-facing objects


from pathlib import Path
import parse

from .definitions import OMM_RESTRAINT_types


def read_restraints(filename, restraint_type):
    """Read a file containing restraint definitions
    and return a dict encoding API calls for OpenMM
    that will implement the restraints.

    Currently supported restraint types:
     - distance, torsion

    Returns
    -------
    `dict` with
      - key: name of OpenMM restraint implementation
      - value: list of 2 lists
        > list1: (possibly ordered) sets of particles
                 the restraint applies to
        > list2: minimum position, force-constant, ...?
    """
    assert restraint_type in OMM_RESTRAINT_types

    if restraint_type == "distance":
        return parse_distance_restraints(filename)

    elif restraint_type == "torsion":
        return parse_torsion_restraints(filename)

    else:
        # restraint types list has type that isn't checked for
        raise Exception("read_restraints function not implemented correctly")


def reader(_reader):
    """Wrapper for file parsers
    """
    def _reader_wrapper(filename):
        fnm = Path(filename)
        assert fnm.is_file()
        with open(fnm) as f:
            return _reader(f)

    return _reader_wrapper


@reader
def parse_distance_restraints(fileobj):
    """Use the distance template to get restraints
    from a file. The upper and lower are currently
    ignored.

    returns
    -------
    `list` of 2 `list`
      > list1: pairs of particles
      > list2: minimum position
    """
    #old jinbo stuff
    """
    interactions = list()
    TEMPLATE_distance = "assign (resid {R1} and name {A1}) (resid {R2} and name {A2}) {MIN} {L} {U}"
    #TEMPLATE_distance = "{R1}    {R1N}    {A1}    {R2}    {R2N}    {A2}    {DIST}"

    #_parse_fields_ = ["R1", "R1N", "A1", "R2", "R2N", "A2", "DIST"]
    _parse_fields_ = ["R1", "A1", "R2", "A2", "MIN", "L", "U"]

    for line in fileobj:
        parsed = parse.parse(TEMPLATE_distance, line)
        if all([pf in parsed for pf in _parse_fields_]):
            R1, A1, R2, A2, MIN, L, U = [parsed[pf] for pf in _parse_fields_]

            interactions.append([(int(R1),A1),(int(R2),A2), float(MIN)])
    """
    interactions = list()
    for line in fileobj:
        cols = line.split()
        R1 = int(cols[0])
        R1N = cols[1]
        A1 = cols[2]
        R2 = int(cols[3])
        R2N = cols[4]
        A2 = cols[5]
        DIST = float(cols[6])
        FLAT = float(cols[7])
        interactions.append([(R1,A1),(R2,A2),DIST,FLAT])

    return interactions

#TEMPLATE_torsion  = "assign (resid {R1} and name {A1}) (resid {R2} and name {A2}) {MIN} {L} {U}"
#    "TEMPLATE_torsion",

@reader
def parse_torsion_restraints(fileobj):
    interactions = list()
    for line in fileobj:
        cols = line.split()
        R1 = int(cols[0])
        A1 = cols[1]
        R2 = int(cols[2])
        A2 = cols[3]
        R3 = int(cols[4])
        A3 = cols[5]
        R4 = int(cols[6])
        A4 = cols[7]
        ANG = float(cols[8])
        interactions.append([(R1,A1),(R2,A2),(R3,A3),(R4,A4),ANG])

    return interactions





