#include <iostream>
#include <fstream>
using namespace std;

char* readFileBytes(const char *name)
{
    ifstream fl(name);
    fl.seekg( 0, ios::end );
    size_t len = fl.tellg();
    char *ret = new char[len];
    fl.seekg(0, ios::beg); 
    fl.read(ret, len);
    fl.close();
    return ret;
}

int main() {
	cout << readFileBytes("shailene_woodley.png");

	return 0;
}
