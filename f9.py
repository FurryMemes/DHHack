import random

def get_map_data(x, y, x2, y2, w, h, w2, h2, mass_data):
    answer = [[0 for i in range(abs(x - x2))] for _ in range(abs(y - y2))]
    colors = [[[] for i in range(abs(x - x2))] for _ in range(abs(y - y2))]
    w_to_x = abs(w - w2) / abs(x - x2)
    h_to_y = abs(h - h2) / abs(y - y2)
    max_c = 0
    min_c = 0
    for i in range(len(mass_data)):
        if min(w, w2) <= mass_data[i][0] and max(w, w2) >= mass_data[i][0]:
            if min(h, h2) <= mass_data[i][1] and max(h, h2) >= mass_data[i][1]:
                x = int(w_to_x * mass_data[i][0])
                y = int(h_to_y * mass_data[i][1])
                answer[x][y] += 1
                max_c = max(max_c, answer[x][y])
                min_c = min(min_c, answer[x][y])

    kof = (max_c - min_c) / min(100, len(mass_data) // 40)
    while kof > 10 and max_c * kof > 200:
        kof -= 10

    if kof == 0:
        kof = 1

    for x in range(len(answer)):
        for y in range(len(answer[0])):
            if answer[x][y] == 0:
                colors[x][y] = [0, 0, 0]
            else:
                colors[x][y] = [0, 0, 255 - int(answer[x][y] * kof)]
    #print(colors)
    return colors
