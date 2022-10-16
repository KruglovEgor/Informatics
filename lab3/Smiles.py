import re
import Tests

pattern = r'X<{O'
for i in range(5):
    print(Tests.tests_smiles[i])
    print(len(re.findall(pattern, Tests.tests_smiles[i])))
    print(' \n')


#One line solution)))
#print(*[Tests.tests_smiles[i] + '\n' + str(len(re.findall(r'X<{O', Tests.tests_smiles[i]))) + '\n' for i in range(5)])