#include <cv.h>
#include <highgui.h>

int main(int argc, char** argv) {
	cvNamedWindow("Contours", 1);
	IplImage* img_8uc1 = cvLoadImage(argv[1], CV_LOAD_IMAGE_GRAYSCALE);
	IplImage* img_edge = cvCreateImage(cvGetSize(img_8uc1), 8, 1);
	IplImage* img_8uc3 = cvCreateImage(cvGetSize(img_8uc1), 8, 3);

	cvThreshold(img_8uc1, img_edge, 128, 255, CV_THRESH_BINARY);

	CvMemStorage* storage = cvCreateMemStorage();
	CvSeq* first_contour = NULL;

	int Nc = cvFindContours(
		img_edge,
		storage,
		&first_contour,
		sizeof(CvContour),
		CV_RETR_LIST
	);

	int n = 0;
	printf("Total Contours Detected: %d\n", Nc);
	for (CvSeq* c = first_contour; c!=NULL; c = c->h_next) {
		cvCvtColor(img_8uc1, img_8uc3, CV_GRAY2BGR);
		cvDrawContours(
			img_8uc3,
			c,
			CV_RGB(0xff,0x00,0x00),
			CV_RGB(0x00,0x00,0xff),
			100,
			2,
			8
		);
		printf("Contour #%d\n", n);
		cvShowImage("Contours", img_8uc3);
		printf(" %d elements:\n", c-> total);
		for (int i = 0; i < c-> total; i++) {
			CvPoint* p = CV_GET_SEQ_ELEM(CvPoint, c, i);
			printf("    (%d, %d)\n", p->x, p->y);
		}
		cvWaitKey(0);
		n++;
	}

	printf("Finished All contours.\n");
	cvCvtColor(img_8uc1, img_8uc3, CV_GRAY2BGR);
	cvShowImage(argv[0], img_8uc3);
	cvWaitKey(0);

	cvDestroyWindow(argv[0]);

	cvReleaseImage(&img_8uc1);
	cvReleaseImage(&img_8uc3);
	cvReleaseImage(&img_edge);

	return 0;
}
