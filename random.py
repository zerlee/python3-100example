#!/sur/bin/python
#random熟悉
import random
random.random()
random.uniform(0,100)
random.randrange(0,100,2)
random.randint(0,100)
seed="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
random.choice(seed)
random.sample(seed,3)
''.join(random.sample(seed,3))
list1=list(seed)
random.shuffle(list1)
