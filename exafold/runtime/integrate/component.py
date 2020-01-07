

class TimestepComponent(dict):
    """Parent class to handle building of OpenMM objects
    """
    def __init__(self, ommName, kwargs):
        super(TimestepComponent, self).__init__()

        self._kwd_order = list()

        # FIXME this is just wretched
        from simtk import openmm
        self._omm_obj  = getattr(openmm, ommName)
        del openmm

        for kwd,val in kwargs:
            self.update({kwd:val})
            self._kwd_order.append(kwd)

    def create(self, **kwargs):
        return self._omm_obj(*[
            self[kwd] * kwargs[kwd]
            for kwd in self._kwd_order
        ])

