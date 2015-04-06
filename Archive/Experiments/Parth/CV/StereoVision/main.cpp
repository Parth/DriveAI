#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/core/core.hpp>
#include <opencv2/calib3d/calib3d.hpp>
#include <stdlib.h>
#include <stdio.h>

using namespace cv;

int main(int argc, char** argv) {
    Mat img1, img2, g1, g2;
    Mat disp, disp8;

    img1 = imread("left2.png");
    img2 = imread("right2.png");

    cvtColor(img1, g1, CV_BGR2GRAY);
    cvtColor(img2, g2, CV_BGR2GRAY);

    StereoBM sbm;
    sbm.state->SADWindowSize = 9;
    sbm.state->numberOfDisparities = 16;
    sbm.state->preFilterSize = 5;
    sbm.state->preFilterCap = 61;
    sbm.state->minDisparity = -39;
    sbm.state->textureThreshold = 250;
    sbm.state->uniquenessRatio = 0;
    sbm.state->speckleWindowSize = 0;
    sbm.state->speckleRange = 8;
    sbm.state->disp12MaxDiff = 1;

    sbm(g1, g2, disp);

    normalize(disp, disp8, 0, 255, CV_MINMAX, CV_8U);

    imshow("left", img1);
    imshow("right", img2);
    imshow("disp", disp8);

	cvWaitKey(0);
}
