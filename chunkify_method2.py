def chunkify(x, y):
	return [x[i:i + y] for i in range(0, len(x), y)]

print(chunkify([1,2,3,4,5,6], 2))
