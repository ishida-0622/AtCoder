#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; i++)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define pb push_back
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef long long ll;
typedef long double ld;
typedef int itn;
int main(void){
    int x;
    cin >> x;
    // x++;
    while(true){
        bool flg = true;
        for(int i = 2; i <= floor(sqrt(x)); i++){
            if(x % i == 0){
                flg =  false;
                break;
            }
        }
        if(flg){
            cout << x;
            break;
        }
        x++;
    }
}