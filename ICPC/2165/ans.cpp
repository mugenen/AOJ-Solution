#include <iostream>
#include <ios>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <array>
using namespace std;
int main(void) {
    ios::sync_with_stdio(false);

    const int M = 256;
    while(true) {
        int N = 0;
        cin >> N;
        if(N == 0) {
            break;
        }
        vector<int> I;
        for(int i = 0; i < N; ++i) {
            int temp;
            cin >> temp;
            I.push_back(temp);
        }

        double min_H = -1;
        double min_S, min_A, min_C;
        for(int S = 0; S < 16; ++S) {
            for(int A = 0; A < 16; ++A) {
                for(int C = 0; C < 16; ++C) {
                    vector<int> R;
                    R.push_back(S);
                    for(int i = 0; i < N; ++i) {
                        R.push_back((A * R[i] + C) % M);
                    }
                    array<int, M> count;
                    fill(count.begin(), count.end(), 0);
                    for(int i = 0; i < N; ++i) {
                        count[(I[i] + R[i + 1]) % M] += 1;
                    }
                    double H = 0;
                    for(int c: count) {
                        if(c != 0) {
                            H -= c / static_cast<double>(N) * log(c / static_cast<double>(N));
                        }
                    }
                    if(min_H == -1) {
                        min_H = H;
                        min_S = S;
                        min_A = A;
                        min_C = C;
                    }
                    if(min_H > H + 1e-9) {
                        min_H = H;
                        min_S = S;
                        min_A = A;
                        min_C = C;
                    }
                }
            }
        }
        cout << min_S << " " << min_A << " " << min_C << endl;
    }

    return 0;
}
