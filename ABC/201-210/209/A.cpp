#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef int itn;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef vector<string> vs;
#define _rep(i, a, b) for (ll i = a, i##_len = (ll)(b); i < i##_len; i++)
#define rep(i, n) _rep(i,0,n)
#define reps(i, n) _rep(i,1,n+1)
#define rrep(i, n) for (ll i = n-1; i >= 0; i--)
#define rreps(i, n) for (ll i = n; i >= 1; i--)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define pb push_back
#define YesNo(flag) if(flag){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}
#define YESNO(flag) if(flag){cout<<"YES"<<endl;}else{cout<<"NO"<<endl;}
#define yesno(flag) if(flag){cout<<"yes"<<endl;}else{cout<<"no"<<endl;}
#define N 100010
#define N2 200010
#define mod 1000000007
// sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[1] < beta[N];}); <- N番目の要素でソート



int main(void){
    int a, b; cin >> a >> b;
    int ans = b-a+1;
    if(ans < 0){
        ans = 0;
    }
    cout << ans;
}