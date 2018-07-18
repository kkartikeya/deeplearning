import cv2
import numpy as np

cam1 = None
cam2 = None
def main():
    cam1 = cv2.VideoCapture( 1 )
    cam2 = cv2.VideoCapture( 2 )

    while( True ):
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()

        numpy_horizontal = np.hstack((frame1, frame2))
        numpy_horizontal_concat = np.concatenate((frame1, frame2), axis=1)
        cv2.imshow( 'Live', numpy_horizontal_concat )
        if(cv2.waitKey( 1 ) & 0xFF == ord( 'q' )):
            break


if __name__ == "__main__":
    main()
