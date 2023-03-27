t = int(input())
for _ in range(t):
	n = int(input())	
	s = input()
	a,b, sw = 0,0,0
	for c in s:
		if c=='U':b += 1
		if c=='R':a += 1
		if c=='D':b -= 1
		if c=='L':a -= 1
		if a==1 and b==1:sw = 1
	print("YES" if sw else "NO")