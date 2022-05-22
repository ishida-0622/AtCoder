#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
int main(void){
    int n, a;
    vector<int> v = {};
    vector<int> ans = {};
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> a;
        v.push_back(a);
    }
    for (int i = 0; i < n; i++){
        if (v[i] > v[i + 1]){
            ans.push_back(1);
            int cnt = 1;
            for (int j = i + 1; j < n; j++){
                if (v[j] < v[j + 1]){
                    ans.push_back(1);
                    break;
                }else{
                    if (j == n - 1){
                        ans.push_back(1);
                    }else{
                        ans.push_back(0);
                    }
                }
                cnt++;
            }
            i += cnt;
        }else{
            ans.push_back(0);
        }
    }
    int sum = accumulate(ans.begin(), ans.end(), 0);
    if (sum % 2 == 1){
        for (int i = n; i > 0; i--){
            if (ans[i] == 1){
                ans[i] = 0;
                break;
            }
        }
    }
    for (int i = 0; i < n - 1; i ++){
    cout << ans[i] << " ";
    }
    cout << ans.back() << endl;
}
