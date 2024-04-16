#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main() {

    string input;
    vector<string> v;
    for(int i = 0; i < 4; i++)
    {
        cin >> input;
        v.push_back(input);
    }

    for(int i = 3; i >= 0; --i)
    {
        cout << v[i] << endl;
    }

    return 0;
}