
__all__ = ["read_restraints"]


from pathlib import Path
import parse


# TODO expand to list of options
#      for restraint implementation
OMM_RESTRAINT_types   = ["distance","torsion"]
OMM_RESTRAIN_distance = "HarmonicBondForce"
OMM_RESTRAIN_torsion  = "HarmonicTorsionForce"
TEMPLATE_distance     = "assign (resid {R1} and name {A1}) (resid {R2} and name {A2}) {MIN} {L} {U}"
#TEMPLATE_torsion  = "assign (resid {R1} and name {A1}) (resid {R2} and name {A2}) {MIN} {L} {U}"


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
        return {
            OMM_RESTRAIN_distance : parse_distance_restraints(filename)
        }

    elif restraint_type == "torsion":
        return {
            OMM_RESTRAIN_torsion  : parse_torsion_restraints(filename)
        }

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
    atom_pairs     = list()
    restraint_mins = list()

    _parse_fields_ = ["R1", "A1", "R2", "A2", "MIN", "L", "U"]

    for line in fileobj:
        parsed = parse.parse(TEMPLATE_distance, line)
        if all([pf in parsed for pf in _parse_fields_]):
            R1, A1, R2, A2, MIN, L, U = [parsed[pf] for pf in _parse_fields_]

            atom_pairs.append([(int(R1),A1),(int(R2),A2)])
            restraint_mins.append(float(MIN))

    return atom_pairs, restraint_mins
