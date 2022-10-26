#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define _rep(i, a, b) for (ll i = a, i##_len = (ll)(b); i < i##_len; i++)
#define rep(i, n) _rep(i,0,n)
#define reps(i, n) _rep(i,1,n+1)
#define rrep(i, n) for (ll i = n-1; i >= 0; i--)
#define rreps(i, n) for (ll i = n; i >= 1; i--)
#define ALL(x) (x).begin(), (x).end()
#define YesNo(flag) if(flag){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}
#define _10_5 100010
#define _2_10_5 200010
#define mod 998244353
#define mod2 1000000007
#define inf 1000000000
#define INF 1000000000000000000L
// sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[N] < beta[N];}); <- N番目の要素でソート



int main(void){
    string n;
    cin >> n;
    ll l = 0, r = 0;
    ll i = 0;
    while (i < n.length() && n[i] == '0') {
        l++;
        i++;
    }
    i = 1;
    while (i <= n.length() && n[n.length()-i] == '0') {
        r++;
        i++;
    }
    if (l > r) {
        cout << "No" << endl;
        return 0;
    }
    string s = "";
    ll m = r - l;
    rep(j, m) {
        s += '0';
    }
    s += n;
    ll a = n.length() + m;
    rep(i, a / 2) {
        if (s[i] != s[a-i-1]) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}
