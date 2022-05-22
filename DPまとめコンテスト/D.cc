#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define _rep(i, a, b) for (ll i = a, i##_len = (ll)(b); i < i##_len; i++)
#define rep(i, n) _rep(i,0,n)
#define reps(i, n) _rep(i,1,n+1)
#define rrep(i, n) for (ll i = n-1; i >= 0; i--)
#define rreps(i, n) for (ll i = n; i >= 1; i--)
#define YesNo(flag) if(flag){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}
#define _10_5 100010
#define _2_10_5 200010
#define mod 998244353
#define mod2 1000000007
#define inf 1000000000
#define INF 1000000000000000000L
// sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[N] < beta[N];}); <- N番目の要素でソート



int main(void){
    int n, w;
    cin >> n >> w;
    vector<vector<long long>> lst(n, vector<long long>(2));
    rep(i,n){
        cin >> lst[i][0] >> lst[i][1];
    }
    vector<vector<long long>> dp(n+1, vector<long long>(w+1));
    rep(i,n){
        int wi = lst[i][0], vi = lst[i][1];
        rep(j,w+1){
            if (j < wi) {
                dp[i+1][j] = dp[i][j];
                continue;
            }
            dp[i+1][j] = max(dp[i][j], dp[i][j-wi] + vi);
        }
    }
    cout << dp[dp.size()-1][w] << endl;
}
