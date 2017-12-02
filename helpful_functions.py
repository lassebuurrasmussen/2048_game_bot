import math


def diff_cords_in_sets(input_dict, char, threshold=50):
    """Takes a dictionary and a key and returns the amount of coordinates
    with a distance larger than the treshold between them"""
    kinds = 1
    new_kinds = []
    kind_indices = [0]

    try:
        first_y = input_dict[char][0][0]
        first_x = input_dict[char][1][0]
    except IndexError:
        kinds = 0
        return kinds, kind_indices

    for i in range(1, len(input_dict[char][0])):
        c_list = []

        current_y = input_dict[char][0][i]
        current_x = input_dict[char][1][i]

        a = current_y - first_y
        b = current_x - first_x
        c_list.append(math.sqrt(a ** 2 + b ** 2))

        if min(c_list) > threshold:
            if len(new_kinds) > 0:
                for kind in new_kinds:
                    kind_y = kind[0]
                    kind_x = kind[1]

                    a2 = current_y - kind_y
                    b2 = current_x - kind_x
                    c_list.append(math.sqrt(a2 ** 2 + b2 ** 2))

                if min(c_list) > threshold:
                    kinds += 1
                    new_kinds.append((current_y, current_x))
                    kind_indices.append(i)


            else:
                kinds += 1
                new_kinds.append((current_y, current_x))
                kind_indices.append(i)

    return kinds, kind_indices
