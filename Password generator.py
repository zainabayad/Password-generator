#Password automatic generator
import random 

from click import command

lowercase = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
sym = '@#$%^&*()_+=-'

znb = lowercase + num + sym
len = 8
passsword = "".join(random.sample(znb, len))
print("Random password is", passsword)