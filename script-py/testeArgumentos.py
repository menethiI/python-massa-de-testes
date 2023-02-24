# %%
import sys
import random

# %%
arg1 = sys.argv[0]
arg2 = sys.argv[1]
arg3 = sys.argv[2]

# %%
print('arg1', arg1)
print('arg2', arg2)
print('arg3', arg3)

def generate_number():
    return random.randint(0, 9)

function_name = 'generate_number'

result = eval(f'{function_name}()')

print(result)