#include<iostream>
#include<cv.h>
#include<highgui.h>

using namespace std;
	
void example2_4(IplImage* image) {
	cvNamedWindow("Example4-in");
	cvShowImage("Example4-in", image);

	IplImage* out = cvCreateImage(cvGetSize(image), IPL_DEPTH_8U, 3);

	cvSmooth(image, out, CV_GAUSSIAN, 3, 3);
	for (int i = 0; i < 10000; i++) {
		cvSmooth(out, out, CV_GAUSSIAN, 3, 3);
	}

	cvShowImage("Example4-out", out);
	cout << out << endl;
	cout << &out << endl;
	cvReleaseImage(&out);
	cvWaitKey(0);

	cvDestroyWindow("Example4-in");
	cvDestroyWindow("Example4-out");
}

int main(int argc, char** argv) {
	example2_4(cvLoadImage(argv[1]));
}
