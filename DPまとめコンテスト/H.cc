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
    ll h, w;
    cin >> h >> w;
    ll n = h + w;
    vector<string> lst(h);
    // vector<vector<vector<ll>>> dp(n, vector<vector<ll>>(h, vector<ll>(w)));
    vector<vector<long long>> dp(h+1, vector<long long>(w+1));
    // dp[0][0][0] = 1;
    dp[1][1] = 1;

    rep(i,h){
        cin >> lst[i];
    }

    reps(i,h){
        reps(j,w){
            if(!(i == 1 && j == 1)){
                if(lst[i-1][j-1] == '#'){
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod2;
                }
            }
        }
    }

    // rep(i,n){
    //     rep(j,h){
    //         rep(k,w){
    //             if (dp[i][j][k] > 0) {
    //                 if (j+1 < h && lst[j+1][k] == '.') {
    //                     dp[i+1][j+1][k] += dp[i][j][k];
    //                     dp[i+1][j+1][k] %= mod2;
    //                 }
    //                 if (k+1 < w && lst[j][k+1] == '.') {
    //                     dp[i+1][j][k+1] += dp[i][j][k];
    //                     dp[i+1][j][k+1] %= mod2;
    //                 }
    //             }
    //         }
    //     }
    // }
    cout << dp[h][w] << endl;
}
