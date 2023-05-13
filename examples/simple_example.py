
from pynn import NearestNeighborIndex

"""
Note that in order for this code to work, 
you'll need to create a file called "query_points.txt" in the same directory as the Python script, 
and populate it with a list of 2D points, one point per line, like this:

1 2
1 0
10 5
-1000 20
3.14159 42
42 3.14159
"""

# read in points from a file
file = 'examples/query_points.txt'
with open(file, "r") as f:
    lines = f.readlines()

points = []
for line in lines:
    point = tuple(float(num) for num in line.replace('\n', '').split(' '))
    points.append(point)

# create a nearest neighbor index
nni = NearestNeighborIndex(points)

# find nearest neighbors for query points
query_points = [(1, 2), (5, 7), (10, 15)]
for query_point in query_points:
    nearest_point = nni.find_nearest(query_point)
    print("Query point:", query_point)
    print("Nearest point:", nearest_point)

