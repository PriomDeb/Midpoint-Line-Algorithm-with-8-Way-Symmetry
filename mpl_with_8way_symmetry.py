

def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6


def convert_to_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def convert_to_original_zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def mpl_with_8way_symmetry(x1, y1, x2, y2):
        zone = find_zone(x1, y1, x2, y2)

        x1_to_z0, y1_to_z0 = convert_to_zone0(x1, y1, zone)
        x2_to_z0, y2_to_z0 = convert_to_zone0(x2, y2, zone)

        dy = y2_to_z0 - y1_to_z0
        dx = x2_to_z0 - x1_to_z0
        d = 2 * dy - dx
        d_E = 2 * dy
        d_NE = 2 * (dy - dx)

        x = x1_to_z0
        y = y1_to_z0

        original_x, original_y = convert_to_original_zone(x, y, zone)

        pixels = []

        while x <= x2_to_z0:
            pixels.append((original_x, original_y))

            if d < 0:
                x = x + 1
                d = d + d_E
            else:
                x = x + 1
                y = y + 1
                d = d + d_NE

            original_x, original_y = convert_to_original_zone(x, y, zone)

        return pixels


if __name__ == '__main__':
    pixels = mpl_with_8way_symmetry(x1=2, y1=2, x2=8, y2=4)
    for i in pixels:
        print(i)
