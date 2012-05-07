import sys
import itertools

crawled = []

def inherits_from(c, index):
	res = []
	for a in c[index]:
		if a in crawled:
			continue
		crawled.append(a)
		if c[a] == []:
			res += [a]
			#print res , ' -- limiting'
		else:
			#print res, ' -- Calling '
			res += [a] + inherits_from(c, a)	
	return res

for tc in xrange(1, int(sys.stdin.readline())+1):
  n = int(sys.stdin.readline())
  classes = {}
  msg = ''
  for i in xrange(0, n):
   try:
	c = sys.stdin.readline().split()[1:]
	c = [int(l) for l in c]
   except IndexError:
	classes[i+1] = []
   classes[i+1] = c
  print classes
  for x in classes:
	if classes[x] == []:
		continue
  	graph = inherits_from(classes, x)
  	if len(graph) != len(set(graph)):
		msg = 'Case #%d: Yes' % tc
		break
  if msg == '':
	msg = 'Case #%d: No' % tc
  #print classes
  #print graph
  print msg