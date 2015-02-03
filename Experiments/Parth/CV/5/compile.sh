g++ -ggdb `pkg-config --cflags opencv` -o `basename main.cpp .cpp` main.cpp `pkg-config --libs opencv`
