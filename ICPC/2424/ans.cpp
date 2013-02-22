#include <iostream>
#include <ios>
#include <set>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main(void) {
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    for(int iter = 0; iter < n; iter++) {
        string t;
        cin >> t;

        int count = 0;
        set<string> visited;
        while(true) {
            visited.insert(t);
            const int L = t.length();
            if(L == 1) {
                break;
            }
            int m = 0;
            for(int i = 1; i < L; ++i) {
                int a = atoi(t.substr(0, i).c_str());
                int b = atoi(t.substr(i).c_str());
                m = max(m, a * b);
            }
            char buffer[1000];
            snprintf(buffer, 1000, "%d", m);
            t = string(buffer);
            if(visited.find(t) != visited.end()) {
                count = -1;
                break;
            }
            count += 1;
        }
        cout << count << endl;
    }
    return 0;
}
