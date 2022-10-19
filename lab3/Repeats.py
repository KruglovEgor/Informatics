import re
import Tests

pattern = re.compile(r'(\b\w+\b)\W+(\b\1\b\W+){1,}')
for i in range(5):
    print("Input:")
    print(Tests.test_repeats[i])
    print("Output:")
    print(re.sub(pattern, lambda x: x.groups()[-1], Tests.test_repeats[i]), "\n")

#one line solution)))
#print(*["\nInput:\n" + Tests.test_repeats[i] + "\nOutput:\n" + re.sub(re.compile(r'(\b\w+\b)\W+(\b\1\b\W+){1,}'), lambda x: x.groups()[-1], Tests.test_repeats[i]) + " \n" for i in range(5)])
