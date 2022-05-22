#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; i++)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define pb push_back
using namespace std;
typedef long long ll;
typedef long double ld;
typedef int itn;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
int main(void){
    int n,w;
    cin >> n >> w;
    vvl v(n, vl(2));
    rep(i,n){
        cin >> v[i][0] >> v[i][1];
    }
    sort(ALL(v));
    int m = 0, idx = n-1;
    ll ans = 0;
    while(m < w){
        ll wm = w-m;
        ans += v[idx][0] * min({v[idx][1], wm});
        m += v[idx][1];
        if(m < w){
            idx--;
            if(idx < 0){
                break;
            }
        }
    }
    cout << ans << endl;
}