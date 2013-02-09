#include <iostream>

//http://www.deqnotes.net/acmicpc/p0006/

void coin(int n, int result[4]) {
    result[0] = (n % 50) / 10;
    result[1] = (n % 100) / 50;
    result[2] = (n % 500) / 100;
    result[3] = n / 500;
}

int main(void) {
    std::string str;
    while(true) {
        int n = 0;
        std::cin >> n;
        if(n == 0){
            break;
        }

        int c10, c50, c100, c500;
        std::cin >> c10 >> c50 >> c100 >> c500;

        int result[4];
        coin(c10 * 10 + c50 * 50 + c100 * 100 + c500 * 500 - n, result);
        if(c10 - result[0] > 0)
            str += "10 " + std::to_string(c10 - result[0]) + "\n";
        if(c50 - result[1] > 0)
            str += "50 " + std::to_string(c50 - result[1]) + "\n";
        if(c100 - result[2] > 0)
            str += "100 " + std::to_string(c100 - result[2]) + "\n";
        if(c500 - result[3] > 0)
            str += "500 " + std::to_string(c500 - result[3]) + "\n";
        str += "\n";
    }
    std::cout << str.substr(0, str.length() - 1);
    return 0;
}
