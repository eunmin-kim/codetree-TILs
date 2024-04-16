#include <iostream>
#include <string>

using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.

    string str[10];

    for (int i = 0; i < 10; i++)
    {
        cin >> str[i];
    }

    int count = 0;
    for (int i = 0; i < 10; i++)
    {
        count += str[i].length();
    }

    cout << count;


    return 0;
}