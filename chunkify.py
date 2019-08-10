def chunkify(x, y):
	p = []
	for i in range(0, len(x), y):
		p.append(x[i:i + y])
	return p

print(chunkify([1,2,3,4,5,6], 2))
