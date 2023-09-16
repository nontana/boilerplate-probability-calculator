import copy
import random
# Consider using the modules imported above.

class Hat:
    ## use [**kwargs] for this case because we need keyword argument usch as [red=6]
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                ## Keep the key as a list
                self.contents.append(key)
        print(self.contents)
    def draw(self, n):
        balldrop = []
        ## Exceed case
        if n > len(self.contents):
            return self.contents
        else:
            for i in range(n):
                ## pop() : remove element
                drop = self.contents.pop(random.randrange(len(self.contents)))
                balldrop.append(drop)
            return balldrop

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0 # times
    for i in range(num_experiments):
        ## use deepcopy (protect the parrent from mutate)
        copy_hat = copy.deepcopy(hat)
        exper_draw = copy_hat.draw(num_balls_drawn)
        count = 0 # Dummy parameter
        for key, value in expected_balls.items():
            if exper_draw.count(key) >= value:
                ## Check count the conditions for each color
                count += 1
        if count==len(expected_balls):
            M += 1
        else:
            M += 0
    prob = M/num_experiments
    return prob
