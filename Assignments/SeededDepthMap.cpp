#define Coordinate double

const double FOCAL_LENGTH = 0.035;
const double c = 1000;
const double k = 80;

const Coordinate[] rightCameraPosition;
const Coordinate[] leftCameraPosition;
const Coordinate[] rightCameraOrientation
const Coordinate[] leftCameraOrientation;

Coordinate[] lidarToWorld(Coordinate radius, Coordinate theta, Coordinate rho);
Coordinate[] worldToImage(Coordinate x, Coordinate y, Coordinate z);
Coordinate[] imageToWorld(Coordinate u, Coordinate v, Coordinate w);
Coordinate[] imageToImage(Coordinate u, Coordinate v, Coordinate w);


