_default_omm_configuration = dict(
    integrator=dict(
        LangevinIntegrator=dict(
            temperature=300,
            frictionCoeff=1,
            stepSize=0.5,
        )
    ),
    barostat=dict(),
    thermostat=dict(),
)

_amber_test_configuration = dict(
    integrator=dict(
        VerletIntegrator=dict(
            stepSize=1, #same as amber default
        )
    ),
    barostat=dict(),
    thermostat=dict(
        AndersenThermostat=dict(
            defaultTemperature=0,
            defaultCollisionFrequency=100,
        )
    ),
)

_default_rt_configuration = dict(
    device="Reference",
    host="local",
)
