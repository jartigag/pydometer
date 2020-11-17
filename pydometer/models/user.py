class User:

    GENDER = ['male', 'female']
    MULTIPLIERS = {'female': 0.413, 'male': 0.415}
    AVERAGES = {'female': 70.0, 'male': 78.0}

    def __init__(self, gender=None, height=None, stride=None):
        try:
            self.gender = str(gender).lower() if gender else None
        except ValueError:
            raise ValueError("Invalid gender")
        try:
            self.height = float(str(height)) if height or height==0 else None
        except ValueError:
            raise ValueError("Invalid height")
        try:
            self.stride = float(str(stride)) if stride or stride==0 else None
        except ValueError:
            raise ValueError("Invalid stride")

        if self.gender and self.gender not in User.GENDER:
            raise ValueError("Invalid gender")
        if self.height!=None and self.height<=0:
            raise ValueError("Invalid height")
        if self.stride!=None and self.stride<=0:
            raise ValueError("Invalid stride")

        if not self.stride:
            self.stride = self.__calculate_stride()

    def __calculate_stride(self):
        if self.gender and self.height:
            return User.MULTIPLIERS[self.gender] * self.height
        elif self.height:
            return self.height * ( sum(User.MULTIPLIERS.values()) / len(User.MULTIPLIERS) )
        elif self.gender:
            return User.AVERAGES[self.gender]
        else:
            return sum(User.AVERAGES.values()) / len(User.AVERAGES)
