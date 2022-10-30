import re
import Tests

for group, txt in Tests.test_kick:
    pattern = re.compile(r'[A-ZА-ЯЁ]\w+ ([A-ZА-ЯЁ])\.\1\. ' + group + r'\b\s?')
    print("Input:")
    print("Group -", group)
    print(txt)
    print("Output:")
    print(re.sub(pattern, "", txt), "\n")

#one line solution)))
# print(*["\nInput:\nGroup - " + Tests.test_kick[i][0] + "\n" + Tests.test_kick[i][1] + "\nOutput:\n" + re.sub(re.compile(r'[A-ZА-ЯЁ]\w+ ([A-ZА-ЯЁ])\.\1\. ' + Tests.test_kick[i][0] + r'\b\s?'), "", Tests.test_kick[i][1]) + "\n" for i in range(5)])
