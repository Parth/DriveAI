#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <highgui.h>

#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int main() {
	CascadeClassifier face_cascade;

	face_cascade.load("haarcascade_frontalface_alt.xml");

	VideoCapture captureDevice;
	captureDevice.open(0);

	Mat captureFrame;
	Mat grayscaleFrame;

	namedWindow("outputCamera", 1);

	while (true) {
		captureDevice>>captureFrame;

		cvtColor(captureFrame, grayscaleFrame, CV_BGR2GRAY);
		equalizeHist(grayscaleFrame, grayscaleFrame);

		std::vector<Rect> faces;
		face_cascade.detectMultiScale(grayscaleFrame, faces, 1.1, 3, CV_HAAR_FIND_BIGGEST_OBJECT|CV_HAAR_SCALE_IMAGE, Size(30,30));

		for(int i = 0; i < faces.size(); i++)  {
			Point pt1(faces[i].x + faces[i].width, faces[i].y + faces[i].height);
			Point pt2(faces[i].x, faces[i].y);
						 
			rectangle(captureFrame, pt1, pt2, cvScalar(0, 255, 0, 0), 1, 8, 0);
										     }

		imshow("outputCamera", captureFrame);
		waitKey(33);
	}

	return 0;
}
