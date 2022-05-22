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
    int n,m;
    cin >> n >> m;
    vi vec(m*2);
    // int a;
    rep(i,m*2){
        cin >> vec.at(i);
    }
    sort(ALL(vec));
    bool flg = true;
    for(int i = m*2-1; i >= 2; i--){
        if(vec.at(i) == vec.at(i-2)){
            flg = false;
            break;
        }
    }
    if(flg){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}