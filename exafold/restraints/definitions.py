
__all__ = [
    "OMM_RESTRAINT_types",
    "OMM_RESTRAIN_distance",
    "OMM_RESTRAIN_torsion",
]

from simtk import unit as u


# TODO expand to list of options
#      for restraint implementation

# TODO inherit setting from user level
#      so these can be set
OMM_RESTRAINT_types   = ["distance","torsion"]

# FUNCTIONAL Encoding dicts
#  -> the dict keys and vals are used
#     programmatically, no typos!
#  --> first one has distance-type restraints
#  --> thus apply/require 2-particle input
OMM_RESTRAIN_distance = dict(
    # our reference name for a Restraint
    # Force Group implementation
    simpleharmonic_customforce=dict(
        # Name of OpenMM App Restraint Type
        #  --> must be length 1 dict with
        #      name of OpenMM force class
        CustomBondForce=dict(
            # given on outer App call
            #  - can be empty
            formula=["k*(r-r0)^2"],
            # one-time calls to Restraint
            # type object
            parameters=[
                dict(addGlobalParameter=["k", 0.0]),
                dict(addPerBondParameter=["r0"]),
            ],
            # Name and call signature for method
            # to add each restraint instance..
            # This case has:
            # 1 restraint ~ [2 atoms, 2 parameters]
            restraint=dict(addBond=[2,1]),
            # One for each parameter
            # in order of parameters list
            units=[
                1,
            ],
        ),
    ),
    complexharmonic_customforce=dict(),
    # TODO probably wrap the default implementations
    #      and test if they run faster or not
    harmonic_force=dict(),
    flatbottom_customforce=dict(
        # Name of OpenMM App Restraint Type
        #  --> must be length 1 dict with
        #      name of OpenMM force class
        CustomBondForce=dict(
            # given on outer App call
            #  - can be empty
            formula=["step(r-r0)*(k/2)*(r-r0)^2"],
            # one-time calls to Restraint
            # type object
            parameters=[
                dict(addGlobalParameter=["k", 0.0]),
                dict(addPerBondParameter=["r0"]),
            ],
            # Name and call signature for method
            # to add each restraint instance..
            # This case has:
            # 1 restraint ~ [2 atoms, 2 parameters]
            restraint=dict(addBond=[2,1]),
            # One for each parameter
            # in order of parameters list
            units=[
                1,
            ],
        ),
    ),
)

OMM_RESTRAIN_torsion  = "CustomTorsionForce"

