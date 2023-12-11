import time
from time import sleep

import cv2
import neoapi
from neoapi import Image as NeoImage


class CamHandler:
    def __init__(self, serial: str) -> None:
        self.neoCam: neoapi.Cam = neoapi.Cam()
        self.currentImage: NeoImage = None
        self.neoCam.EnableImageCallback(self.imageCallback)
        self.neoCam.Connect(serial)
        self.neoCam.f.PixelFormat = neoapi.PixelFormat_BGR8

    def imageCallback(self, image: NeoImage) -> None:
        self.currentImage = image


    def getImage(self) -> NeoImage:
        startTime = time.time()
        self.neoCam.f.AcquisitionStart.Execute()
        self.neoCam.f.TriggerSoftware.Execute()
        neoImage: NeoImage = self.neoCam.GetImage()
        while True:
            sleep(0.500)
            if self.currentImage is not None:
                print("Got Image")
                break
            if time.time() - startTime > 5:
                ("Timeout")
                break
        neoImage = self.currentImage
        self.currentImage = None
        sleep(2)
        return neoImage


def main():
    camHandler = CamHandler("700005866925")
    while True:
        input("Press any key to continue...")
        try:
            image = camHandler.getImage()
            if image is None:
                print('Empty Image')
                continue
            npArray = image.GetNPArray()
            cv2.imwrite("D:\Repos\\banane.png", npArray)
        except Exception as error:
            print(error)
        print('Done')

if __name__ == "__main__":
    main()
