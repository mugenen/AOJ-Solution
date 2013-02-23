#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
    ios::sync_with_stdio(false);

    vector<int> square;
    for(int i = 0; i * i <= 32768; ++i) {
        square.push_back(i * i);
    }
    const size_t L = square.size();
    while(true) {
        int n = 0;
        cin >> n;
        if(n == 0) {
            break;
        }

        int count = 0;
        for(int i = 0; i < L; ++i) {
            for(int j = i; j < L; ++j) {
                for(int k = j; k < L; ++k) {
                    int v = n - square[i] - square[j] - square[k];
                    if(v < square[k]) {
                        break;
                    }
                    if(binary_search(square.begin(), square.end(), v)) {
                        count += 1;
                    }
                }
            }
        }
        cout << count << endl;
    }

    return 0;
}
