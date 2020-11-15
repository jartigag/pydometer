from user import User
from trial import Trial

class Analyzer:

    THRESHOLD = 0.09

    def __init__(self, data, user, trial):
        self.data = data
        self.user = user
        self.trial = trial
        self.measure_steps()
        self.measure_delta()
        self.measure_distance()
        self.measure_time()

    def measure_steps(self):
        self.steps = 0
        count_steps = True

        for i,dat in enumerate(self.data):

            if dat>=Analyzer.THRESHOLD and self.data[i-1]<Analyzer.THRESHOLD:
                if not count_steps:
                    continue
                self.steps+=1
                count_steps = False

            if dat<0 and self.data[i-1]>=0:
                cont_steps = True

    def measure_delta(self):
        if self.trial.steps:
            self.delta = self.steps - self.trial.steps

    def measure_distance(self):
        self.distance = self.user.stride * self.steps

    def measure_time(self):
        if self.trial.rate:
            #TODO: what's `@data.count` in `@time = @data.count/@trial.rate if @trial.rate`?
            if self.trial.rate:
                self.time = len(self.data) / self.trial.rate
