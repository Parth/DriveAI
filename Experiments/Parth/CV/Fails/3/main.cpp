#include "opencv/highgui.h"

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	IplImage* img = cvLoadImage(argv[1]);
	cvNameWindow("Example1", CV_WINDOW_AUTOSIZE);
	cvShowImage("Example1", img);
	cvWaitKey(0);
	cvReleaseImage(&img);
	cvDestroyWindow("Example1");
	return 0;
}
