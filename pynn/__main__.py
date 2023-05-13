import sys
from .nearest_neighbor_index import NearestNeighborIndex

def main():
    #file upload and index
    if (len(sys.argv) < 2):
        print("Error Unknown File")
    elif (len(sys.argv) == 2):
        file = get_txt(sys.argv[1])
    elif (len(sys.argv) == 3):
        file_ext = sys.argv[1].split('.')
        if(file_ext[1] != 'txt'):
            print("Error .txt File Required")
        else:
            file = get_txt(sys.argv[1])
            file2 = get_txt(sys.argv[2])
        

    #call NNI
    uut = NearestNeighborIndex(file)
    for point in file2:
        print(uut.find_nearest(point))
    
        
def get_txt(file):
    #text files only
    try:
        with open(file, "r") as f:
            lines = f.readlines()
    
        points = []
        for line in lines:
            point = tuple(float(num) for num in line.replace('\n', '').split(' '))
            points.append(point)
        return points
    except:
        print('Error Reading File')

    

if __name__ == "__main__":
    main()