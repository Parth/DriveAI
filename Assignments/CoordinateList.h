#define Coordinate double

class CoordinateList {
    public:
        List<Coordinates> coordinates;
        char type;
        /**
        *
        */
        void toType(int type);

        /**
        * 
        */
        void toType(int type, Coordinate[] origin);
        CoordinateList clone();
};
