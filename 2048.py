import numpy as np
from PIL import ImageGrab
import cv2
import math
from helpful_functions import diff_cords_in_sets as dcis

# Make coordinates list of tuples
first_square_coords = (72, 71)
square_center_cords = []
for i in list(range(0, 4)):
    for j in list(range(0, 4)):
        square_center_cords.append((first_square_coords[0] + i * 120, first_square_coords[1] + j * 120))

# Create a list with the template number types
temp_types = [2]
for i in range(0, 8):
    temp_types.append(temp_types[-1] * 2)

temp_images = [cv2.imread('templates/%i.jpg' % i, 0) for i in temp_types]

# Width and height saved as (w,h) in temcoords list for all templates
temp_coords = [temp_img.shape[::-1] for temp_img in temp_images]


def detect_numbers(input_image, temp_img_list):
    """
    Take an input image and a list of templates and outputs an image with squares around identified templates

    """
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    res_dict = {}
    for temp_image, temp_type in zip(temp_img_list, temp_types):
        res_dict[temp_type] = cv2.matchTemplate(input_image, temp_image, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    value_matrix = np.zeros((4, 4))

    locs_dict = {}
    for temp_type, res in res_dict.items():
        locs_dict[temp_type] = np.where(res >= threshold)
        coord_count, coord_indices = dcis(locs_dict, temp_type)
        for j in range(0, coord_count):
            for i in range(len(square_center_cords)):
                a = locs_dict[temp_type][::-1][0][coord_indices[j]] - square_center_cords[i][0]
                b = locs_dict[temp_type][::-1][1][coord_indices[j]] - square_center_cords[i][1]
                c = math.sqrt(a ** 2 + b ** 2)
                if c < 55:
                    mat_col_i = math.floor(i / 4)
                    mat_row_i = i - (mat_col_i * 4)
                    value_matrix[mat_row_i, mat_col_i] = temp_type

    print(value_matrix)

    for i, temp_type in zip(range(len(temp_img_list)), temp_types):
        for pt in zip(*locs_dict[temp_type][::-1]):
            cv2.rectangle(input_image, pt,
                          (pt[0] + temp_coords[i][0], pt[1] + temp_coords[i][1]),
                          (0, 255, 255), 2)

    return input_image


def screen_record():
    while True:
        printscreen = np.array(ImageGrab.grab(bbox=(0, 60, 500, 560)))
        printscreen = detect_numbers(printscreen, temp_images)
        cv2.imshow('window', printscreen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
