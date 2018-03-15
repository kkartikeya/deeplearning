import cv2

cam = None
def main():
    cam = cv2.VideoCapture( 1 )

    while( True ):
        ret, frame = cam.read()
        cv2.imshow( 'Live', frame )
        if(cv2.waitKey( 1 ) & 0xFF == ord( 'q' )):
       		break


if __name__ == "__main__":
	main()
