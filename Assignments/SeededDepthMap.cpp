#define Coordinate double

const double FOCAL_LENGTH = 0.035;
const double c = 1000;
const double k = 80;

// coordinate triples that specify, in world (x,y,z) coordinates, the offset and orientation of the cameras relative to the lidar scanner
const Coordinate[] rightCameraPosition;
const Coordinate[] leftCameraPosition;
const Coordinate[] rightCameraOrientation
const Coordinate[] leftCameraOrientation;

/**
 * Conducts a stereo correspondence seeded by lidar data
 * 
 * @param left  left image to be used in correspondence
 * @param right right image to be used in correspondence
 * @param lidar lidar data to be used as the seed
 */
CoordinateList seededCorrespondence(Image left, Image right, CoordinateList lidar)
{
    
}
