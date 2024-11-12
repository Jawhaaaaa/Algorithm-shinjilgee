#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

int knapsack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= W; w++) {
            if (wt[i - 1] <= w)
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][W];
}

void runTest(int testNum, int W, vector<int>& wt, vector<int>& val, int n, int expected) {
    int result = knapsack(W, wt, val, n);
    if (result == expected) {
       cout << "Test " << testNum << " correct: result = " << result << endl;
    } else {
        cout << "Test " << testNum << " wrong: expected " << expected << " but got " << result << endl;
    }
}

int main() {
    // Test case 1
    vector<int> wt1 = {1, 2, 3};
    vector<int> val1 = {60, 100, 120};
    int W1 = 5;
    int n1 = wt1.size();
    runTest(1, W1, wt1, val1, n1, 220); 

    // Test case 2
    vector<int> wt2 = {1, 3, 4, 5};
    vector<int> val2 = {10, 40, 50, 70};
    int W2 = 7;
    int n2 = wt2.size();
    runTest(2, W2, wt2, val2, n2, 110); 

    // Test case 3
    vector<int> wt3 = {5, 4, 6, 3};
    vector<int> val3 = {10, 40, 30, 50};
    int W3 = 10;
    int n3 = wt3.size();
    runTest(3, W3, wt3, val3, n3, 90); 

    return 0;
}
