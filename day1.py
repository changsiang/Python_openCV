#!/usr/bin/python
import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray as ndarray


class Day1(object):
    __version__ = "0.0.1a"
    __author__ = "Lim Chang Siang"
    img = ndarray([])

    def __init__(self, arg1: str):
        print(arg1)
        self.img = self.get_image(arg1)
        print(type(self.img))

    @staticmethod
    def get_image(file: str):
        return cv2.imread(file, cv2.IMREAD_COLOR)

    @staticmethod
    def show_image(self, title: str):
        cv2.imshow(title, self.img)
        cv2.waitKey(0)

    @staticmethod
    def show_image_plt(self):
        plt.imshow(self.img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        #plt.plot([200, 300, 400], [100, 200, 300], 'c', lineWidth=5)
        plt.show()

    @staticmethod
    def close_window():
        cv2.destroyAllWindows()


firstVar = Day1("conycry.png")
secondVar = Day1("conyGray.png")
firstVar.show_image_plt(firstVar)
firstVar.show_image(firstVar, "Cony")
firstVar.close_window()
