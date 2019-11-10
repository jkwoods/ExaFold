
__all__ = [
    "OMM_RESTRAINT_types",
    "OMM_RESTRAIN_distance",
    "OMM_RESTRAIN_torsion",
]


# TODO expand to list of options
#      for restraint implementation

# TODO inherit setting from user level
#      so these can be set
OMM_RESTRAINT_types   = ["distance","torsion"]

# FUNCTIONAL Encoding dicts
#  -> the dict keys and vals are used
#     programmatically, no typos!
OMM_RESTRAIN_distance = dict(
    # Name of OpenMM App Restraint Type
    CustomBondForce=dict(
        # given on outer App call
        #  - can be empty
        formula=["-k*(r-r0)^2"],
        # one-time calls to Restraint
        # type object
        parameters=[
            dict(addPerBondParameter=["k"]),
            dict(addPerBondParameter=["r0"]),
        ],
        # Name and call signature for method
        # to add each restraint instance..
        # This case has:
        # 1 restraint ~ [2 atoms, 2 parameters]
        restraint=dict(addBond=[2,2])
    ),
)

OMM_RESTRAIN_torsion  = "CustomTorsionForce"

