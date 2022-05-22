#include <bits/stdc++.h>
#define rep(i, n) for(int i=0, i##_len=(n); i<i##_len; i++)
# define ALL(x) (x).begin(), (x).end()
# define SZ(x) ((int)(x).size())
# define pb push_back
using namespace std;
using ll = long long;
int main(void){
    int n, m, cnt;
    cin >> n;
    cnt = 0;
    for(int i = 0; i < n; i++){
        cin >> m;
        bool flg = false;
        for(int a = 1; a < 200; a++){
            for(int b = 1; b < 200; b++){
                if(4*a*b+3*a+3*b == m){
                    cnt++;
                    flg = true;
                    break;
                }else if(4*a*b+3*a+3*b > m){
                    break;
                }
            }
            if(flg){
                break;
            }
        }
    }
    cout << n - cnt;
}