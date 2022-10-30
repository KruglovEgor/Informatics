import time

from ITMO.Informatics.lab4 import With_hands, With_regulars, With_libs

t0_hands = time.time()
for i in range(10):
    With_hands.start('Lr4.yaml', 'Tests/Hands/'+str(i+1)+'.json')

t1_hands = time.time()
print("Time for program (10x) made with hands:", t1_hands - t0_hands, '\n')


t0_re = time.time()
for i in range(10):
    With_regulars.start('Lr4.yaml', 'Tests/Regulars/'+str(i+1)+'.json')

t1_re = time.time()
print("Time for program (10x) made with regulars:", t1_re - t0_re, '\n')


t0_lib = time.time()
for i in range(10):
    With_libs.start('Lr4.yaml', 'Tests/Libs/'+str(i+1)+'.json')

t1_lib = time.time()
print("Time for program (10x) made with libraries:", t1_lib - t0_lib, '\n')