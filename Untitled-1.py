import re
a= "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
result=re.findall(r'wood\w*',a)
print (result)