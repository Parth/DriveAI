#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <stdlib.h>
#include <stdio.h>

using namespace cv;

int main(int argc, char** argv) {
    //Declare variables we're going to be using
    Mat src, src_gray;
    Mat grad;
    char* window_name = "Sobel Demo";
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16S;

    int c;

    //Load our source image
    src = imread(argv[1]);

    if (!src.data) {
        return -1;
    }

    //Apply gausian blur to reduce noise
    GaussianBlur(src, src, Size(3, 3), 0, 0, BORDER_DEFAULT);

    //Convert to grayscale
    cvtColor(src, src_gray, CV_RGB2GRAY);

    //Calculate 'derivatives' in x, and y directions
    Mat grad_x, grad_y;
    Mat abs_grad_x, abs_grad_y;

    //src gray input image
    //grad_x & grad_y output image
    //ddeppth the depth of the output image
    //order of the derivative in the x direction

    //Gradient X
    Sobel(src_gray, grad_x, ddepth, 2, 0, 3, scale, delta, BORDER_DEFAULT);
    //Gradient Y
    Sobel(src_gray, grad_y, ddepth, 0, 2, 3, scale, delta, BORDER_DEFAULT);

    convertScaleAbs(grad_x, abs_grad_x);
    convertScaleAbs(grad_y, abs_grad_y);

    addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0, grad);

    imshow(window_name, grad);
    waitKey(0);
    return 0;
}
