from django.test import TestCase

# Create your tests here.

s = "123456"

s=s+s

name = "somename"

ans =''

for i in range(len(s)):
    #print(ord(s[i]) ,ord((name[i%len(name)])))
    ans= ans + str(ord(s[i]) ^ord((name[i%len(name)])))
    print(ans)

print(ans)