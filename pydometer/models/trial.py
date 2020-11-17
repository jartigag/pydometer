class Trial:
    def __init__(self, name, rate=None, steps=None):
        self.name = str(name).replace(' ','') if name else None
        try:
            self.rate = int(str(rate)) if rate or rate==0 else None
        except ValueError:
            raise ValueError("Invalid rate")
        try:
            self.steps = int(str(steps)) if steps or steps==0 else None
        except ValueError:
            raise ValueError("Invalid steps")

        if not self.name:
            raise ValueError("Invalid name")
        if self.rate!=None and self.rate<=0:
            raise ValueError("Invalid rate")
        if self.steps!=None and self.steps<0:
            raise ValueError("Invalid steps")
