
class Configuration(object):
    def __init__(self, **kwargs):
        super(Configuration, self).__init__()

        self.configure(kwargs)

    def configure(self, kwargs):
        self.n_steps = kwargs.get("n_steps")
        self.temps   = kwargs.get("temps")
