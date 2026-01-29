import numpy as np

class GammaDistribution:
    def __init__(self, max_delay=6):
        self.max_delay = max_delay

    def dis_sample(self):
        return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.34060516, 0.3900214, 0.18700785, 0.06177684, 0.01664414, 0.00394461])

    def dis_probability(self):
        return np.array([0, 0.34060516, 0.3900214, 0.18700785, 0.06177684, 0.01664414, 0.00394461])

class UniformDistribution:
    def __init__(self, max_delay=13):
        self.max_delay = max_delay

    def dis_sample(self):
        return np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
                                p=[0.07693, 0.07693, 0.07693, 0.07693, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692])

    def dis_probability(self):
        return np.array([0, 0.07693, 0.07693, 0.07693, 0.07693, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692, 0.07692])

class DoubleGaussianDistribution:
    def __init__(self, max_delay=10):
        self.max_delay = max_delay

    def dis_sample(self):
        return np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p=[0.03982, 0.12356, 0.15381, 0.13144, 0.10588, 0.13168, 0.15682, 0.11015, 0.04098, 0.00586])

    def dis_probability(self):
        return np.array([0, 0.03982, 0.12356, 0.15381, 0.13144, 0.10588, 0.13168, 0.15682, 0.11015, 0.04098, 0.00586])