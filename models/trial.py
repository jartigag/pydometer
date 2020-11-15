class Trial:
    def __init__(self, name, rate=None, steps=None):
        self.name = str(name).strip().replace(' ','_')
        self.rate = int(rate) if rate else 0
        self.steps = int(steps) if steps else 0

        if not self.name:
            raise ValueError("Invalid name")
        if self.rate and self.rate<=0:
            raise ValueError("Invalid rate")
        if self.steps and self.steps<=0:
            raise ValueError("Invalid steps")
