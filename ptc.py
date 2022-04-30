import re
st1 = input()
st2 = input()
mt = list(re.finditer('(?=(%s))' %st2, st1))
if(not mt):
    print((-1,-1))
for i in mt:
    print((i.start(1), i.end(1)-1))