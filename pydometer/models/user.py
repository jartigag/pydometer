class User:

    GENDER = ['male', 'female']
    MULTIPLIERS = {'female': 0.413, 'male': 0.415}
    AVERAGES = {'female': 70.0, 'male': 78.0}

    def __init__(self, gender=None, height=None, stride=None):
        self.gender = str(gender).lower() if gender else None
        self.height = float(height) if height else None
        self.stride = float(stride) if stride else self.__calculate_stride()

        if self.gender and self.gender not in User.GENDER:
            raise ValueError("Invalid gender")
        if self.height and self.height<=0:
            raise ValueError("Invalid height")
        if self.stride and self.stride<=0:
            raise ValueError("Invalid stride")

    def __calculate_stride(self):
        if self.gender and self.height:
            return User.MULTIPLIERS[self.gender] * self.height
        elif self.height:
            return self.height * ( sum(User.MULTIPLIERS.values()) / len(User.MULTIPLIERS) )
        elif self.gender:
            return User.AVERAGES[self.gender]
        else:
            return (70.0+78.0)/2
            #return sum(User.AVERAGES.values()) / len(User.AVERAGES)
