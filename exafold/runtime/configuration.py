
class Configuration(object):
    """Save important details for the MD runtime
    """

    _fields = [
        "n_steps", "temperature", "fn_traj",
        "fn_state", "fr_save"]

    def __init__(self, **kwargs):
        super(Configuration, self).__init__()

        self.configure(kwargs)

    def configure(self, kwargs):

        # TODO can expand so instance get additional fields
        for field in self._fields:
            setattr(self, field, kwargs.get(field))
