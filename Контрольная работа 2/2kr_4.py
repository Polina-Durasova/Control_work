import re

test_string="#HHHHHH"
if re.findall(pattern=r"(#)", string=test_string) and len(test_string)==7:
    print('yes')
else:
    print('not')