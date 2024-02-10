import random
from criticalinjuries import *
injury_lists = {'b2': b2, 'b3': b3, 'b4': b4, 'b5': b5, 'b6': b6, 'b7': b7, 'b8': b8, 'b9': b9, 'b10': b10, 'b11': b11, 'b12': b12, 'h2': h2, 'h3': h3, 'h4': h4, 'h5': h5, 'h6': h6, 'h7': h7, 'h8': h8, 'h9': h9, 'h10': h10, 'h11': h11, 'h12': h12}
roll = (random.randint(1, 6))+(random.randint(1, 6))

type = input ("Head or body")
if type == "head":
    letter = 'h'
elif type == "body":
    letter = 'b'
injury = letter + str(roll)
injury_list = injury_lists.get(injury)

print("Injury:", injury_list[0])
print("Effect:", injury_list[1])
print("Quick fix:", injury_list[2])
print("Treatment:", injury_list[3])

