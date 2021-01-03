class PIDController:
    def __init__(self, pK=0, iK=0, windup_limit=None):
        self.pK = pK
        self.iK = iK
        self.windup_limit = windup_limit

        self.integral_sum = 0

    def handle_proportional(self, error):
        return self.pK * error

    def handle_integral(self, error):
        if self.windup_limit is None \
                or abs(self.integral_sum) < self.windup_limit \
                or error > 0 != self.integral_sum > 0:
            self.integral_sum += error
        return self.iK * self.integral_sum

    def get_adjustment(self, error):
        p = self.handle_proportional(error)
        i = self.handle_integral(error)
        return p + i

    def reset(self):
        self.integral_sum = 0
