import math


class NearestNeighborIndex:
    """
    Finds the Nearest Neighbor Index for a point using set of points in a 2D plane. 
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points
        self.sort_points()

    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        min_dist = None
        min_point = None

        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point
    
    def sort_points(self):
        """
        duplicates and sorts an array of 2d tuples, one array for each dimension
        """
        self.points_x_sort = sorted(self.points)
        self.points_y_sort = sorted(self.points, key=lambda x: x[1])

    def calculate_estimate(self, points, axis, query_point):
        """
        Returns the two closest points based on the x or y axis
        """
        low = 0
        high = len(points) - 1
    
        # Binary search to find the closest points
        while low <= high:
            mid = (low + high) // 2
            if points[mid][axis] == query_point[axis]:
                return mid, mid
            elif points[mid][axis] < query_point[axis]:
                low = mid + 1
            else:
                high = mid - 1
    
        # Handle edge cases
        if high < 0:
            return low, low+1
        elif low >= len(points):
            return high-1, high
        elif abs(points[low][axis] - query_point[axis]) < abs(points[high][axis] - query_point[axis]):
            return low, low+1
        else:
            return high-1, high
        
    def calculate_distance(self, point, query_point):
        """
        Calculates the distance between two points.
        """
        deltax = point[0] - query_point[0]
        deltay = point[1] - query_point[1]
        return math.sqrt(deltax * deltax + deltay * deltay)

    def find_nearest(self, query_point):
        """
        Returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """
        x_sort = self.points_x_sort
        y_sort = self.points_y_sort

        # find the closest points on the x-axis and the y-axis
        x_close = self.calculate_estimate(x_sort, 0, query_point)
        y_close = self.calculate_estimate(y_sort, 1, query_point)

        # combine the closest points on the x and y axis
        closest_points = []
        if self.points != None and len(self.points) > 0:
            for index in range(1):
                closest_points.append(x_sort[x_close[index]])
                closest_points.append(y_sort[y_close[index]])
        

        min_dist = None
        min_point = None

        for point in closest_points:
            dist = self.calculate_distance(point, query_point)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point
