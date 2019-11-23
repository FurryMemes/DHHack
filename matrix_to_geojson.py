import json

def arr_to_geojson(arr):
    d = {}
    for i in range(len(arr)):
        d[i] = {'latitude': arr[i][0], 'longitude': arr[i][1]}
    dump = json.dumps(d)
    return dump

if __name__ == '__main__':
    arr = [[1, 2], [3, 4]]
    arr_to_geojson(arr)