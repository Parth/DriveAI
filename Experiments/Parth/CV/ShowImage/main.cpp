#include <cv.h>
#include <highgui.h>
#include <stdio.h>

int main(int argc, char** argv) {
	IplImage* img = cvLoadImage(argv[1]);
	cvNamedWindow("example1", CV_WINDOW_AUTOSIZE);
	cvShowImage("example1", img);
	cvWaitKey(0);
	cvReleaseImage(&img);
	cvDestroyWindow("example1");
}
