#include <bits/stdc++.h>
using namespace std;
int main(void){
    int n, m;
    cin >> n >> m;
    vector<vector<int>> lst(n, vector<int>(m));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> lst.at(i).at(j);
        }
    }
    int a = lst.at(0).at(0);
    bool flag = true;
    if (m != 1){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                int b = a + i * 7 + j;
                if (lst.at(i).at(j) != b){
                    flag = false;
                }
            }
        }
    }else{
        for (int i = 0; i < n - 1; i++){
            if (lst.at(i).at(0) + 7 != lst.at(i + 1).at(0)){
                flag = false;
            }
        }
    }
    if (m != 7 && m != 1){
        for (int i = 0; i < m - 2; i++){
            if ((lst.at(0).at(i) % 7) >= (lst.at(0).at(i + 1) % 7)){
                flag = false;
            }
        }
        if (lst.at(0).at(0) % 7 == 0){
            flag = false;
        }
    }else if (m != 1){
        if (lst.at(0).at(0) % 7 != 1){
            flag = false;
        }
    }
    if (flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}