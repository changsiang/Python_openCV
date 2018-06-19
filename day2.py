#!/usr/bin/python
import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray as ndarray
from cv2 import VideoCapture as cv2VCap


class VideoCapture(object):
    __version__ = "0.0.1a"
    __author__ = "Lim Chang Siang"

    def __init__(self, arg1):
        self.cap = self.get_camera(arg1)
        while 1:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            print(type(gray))
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def get_camera(index):
        return cv2.VideoCapture(index)


def main():
    VideoCapture(0)


if __name__ == "__main__":
    main()
