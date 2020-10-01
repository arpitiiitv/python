import random
import numpy as np
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
print(s)
random_number= random.randint(0,5)
print(random_number)
rand= random.random()*100   #print any number between 0 to 100
print(rand)
lst= ["startPlus","DD1", "Aaj Tak"]
choice= random.choice(lst)
print(choice)
