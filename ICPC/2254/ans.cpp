#include <iostream>
#include <ios>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

int times[16][17];
int N;

map<vector<int>, int> memo;

int dp(const vector<int>& state) {
    auto it = memo.find(state);
    if(it != memo.end()) {
        return it->second;
    }

    const int L = state.size();
    if(L == 1) {
        return times[*state.begin()][0];
    } else {
        int min_route = 10000000;
        for(int i : state) {
            vector<int> copy = state;
            copy.erase(remove(copy.begin(), copy.end(), i));
            int min_time = times[i][0];
            for(int j = 0; j < N; ++j) {
                if(find(copy.begin(), copy.end(), j) != copy.end()) {
                    min_time = min(min_time, times[i][j + 1]);
                }
            }
            min_route = min(min_route, dp(copy) + min_time);
        }
        memo[state] = min_route;
        return min_route;
    }
}

int main(void) {
    ios::sync_with_stdio(false);

    while(true) {
        cin >> N;
        if(N == 0) {
            break;
        }
        for(int i = 0; i < N; ++ i) {
            for(int j = 0; j < N + 1; ++j) {
                int x;
                cin >> x;
                times[i][j] = x;
            }
        }
        vector<int> state;
        for(int i = 0; i < N; ++ i) {
            state.emplace_back(i);
        }
        memo.clear();
        cout << dp(state) << endl;
    }

    return 0;
}
