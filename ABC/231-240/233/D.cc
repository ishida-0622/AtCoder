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
    ll n,k,ans;
    ans = 0;
    cin >> n >> k;
    vector<ll> vec(n);
    rep(i,n){
        cin >> vec[i];
    }
    int m = 0,l = 0;
    rep(i,n){
        m += vec[i];
        l = m;
        if(l == k){
            ans++;
        }
        rep(j,i){
            l -= vec[j];
            if(l == k){
                ans++;
            }
        }
    }
    cout << ans;
}