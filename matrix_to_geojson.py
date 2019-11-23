import geojson

def arr_to_geojson(arr):
    my_point = geojson.Point(arr)
    dump = geojson.dumps(my_point, sort_keys=True)
    return dump

if __name__ == '__main__':
    arr = [[1, 2], [3, 4]]
    arr_to_geojson(arr)