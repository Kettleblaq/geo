import math


class NearestNeighborIndex:
    """
    TODO give me a decent comment

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points

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
    
    def index_points(self):
        """
        duplicates and sorts an array of 2d tuples, one array for each dimension
        """
        self.points_x_sort = sorted(self.points)
        self.points_y_sort = sorted(self.points, key=lambda x: x[1])

    def find_nearest_axis(self, points, index, query_point):
        """
        returns an array of two 2d tuples with the closest value to x
        """

        low = 0
        high = len(points) - 1
        while low <= high:
            mid = (low + high) // 2
            if points[mid][index] == query_point[index]:
                return mid, mid
            elif points[mid][index] < query_point[index]:
                low = mid + 1
            else:
                high = mid - 1
        if high < 0:
            return low, low+1
        elif low >= len(points):
            return high-1, high
        elif abs(points[low][index] - query_point[index]) < abs(points[high][index] - query_point[index]):
            return low, low+1
        else:
            return high-1, high

    def find_nearest_fast(self, query_point):
        """
        TODO: Re-implement me with your faster solution.

        find_nearest_fast returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """
        x_sort = self.points_x_sort
        y_sort = self.points_y_sort

        x_close = self.find_nearest_axis(x_sort, 0, query_point)
        y_close = self.find_nearest_axis(y_sort, 1, query_point)

        closest_points = x_sort[x_close[0]:x_close[1]] + y_sort[y_close[0]:y_close[1]]

        min_dist = None
        min_point = None

        for point in closest_points:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    def find_nearest(self, query_point):
        """
        TODO comment me.
        """

        # TODO implement me so this class runs much faster.
        return self.find_nearest_fast(query_point)
