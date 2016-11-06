

s = "hello world" # s zeigt auf str hello word in memory
# mutable and non mutable objects
# veranderbar z.b. lists / nicht veranderbar z.b. string

s = (s.split(" "))

sp = []
for item in s:
	sp.append(item.capitalize())
print sp

for i in range(0,len(s)):
	s[i]=s[i].capitalize()
print s
