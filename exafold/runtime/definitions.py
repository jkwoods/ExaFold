_default_omm_configuration = dict(
    integrator=dict(
        LangevinIntegrator=dict(
            temperature=300,
            frictionCoeff=1,
            stepsize=2,
        )
    ),
    barostat=dict(),
    thermostat=dict(),
    device="CUDA",
)
