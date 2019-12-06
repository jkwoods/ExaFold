_default_omm_configuration = dict(
    integrator=dict(
        LangevinIntegrator=dict(
            temperature=300,
            frictionCoeff=1,
            stepSize=2,
        )
    ),
    barostat=dict(),
    thermostat=dict(),
)

_default_rt_configuration = dict(
    device="Reference",
    host="local",
)
