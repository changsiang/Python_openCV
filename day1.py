#!/usr/bin/python
import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray as ndarray
import copy


class Day1(object):
    __version__ = "0.0.1a"
    __author__ = "Lim Chang Siang"

    def __init__(self, arg1: str):
        self.img = self.get_image(arg1)

    @staticmethod
    def get_image(file: str):
        return cv2.imread(file, cv2.IMREAD_REDUCED_COLOR_2)

    def show_image(self, title: str):
        cv2.imshow(title, self.img)
        cv2.waitKey(0)

    def show_image(self, title: str, channel: int):
        img = copy.deepcopy(self.img)
        img[:, :, channel] = 0
        cv2.imshow(title, img)
        cv2.waitKey(0)

    def show_image_plt(self):
        plt.imshow(self.img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        #plt.plot([200, 300, 400], [100, 200, 300], 'c', lineWidth=5)
        plt.show()

    @staticmethod
    def close_window():
        cv2.destroyAllWindows()

    def clone_region(self, source_x: int, source_y: int, dest_x: int, dest_y: int):
        img = self.img[source_x:source_y, source_x:source_y]
        self.img[dest_x:dest_y, dest_x:dest_y] = img
        img[dest_x:dest_y, dest_x:dest_y, 0] = 0


def main():
    day1 = Day1("islet.jpg")
    # second_var = Day1("conyGray.png")
    # day1.show_image_plt(day1)
    # day1.clone_region(256, 500, 0, 244)
    day1.show_image('Off DAPI', 0)
    day1.show_image('Off 488', 1)
    day1.show_image('Off 594', 2)
    day1.show_image('Original')
    day1.close_window()


if __name__ == "__main__":
    main()
