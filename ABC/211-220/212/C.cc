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
// sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[1] < beta[N];}); <- N番目の要素でソート



int main(void){
    int n,m;
    cin >> n >> m;
    vi a = vi(n);
    vi b = vi(m);
    rep(i,n){
        cin >> a[i];
    }
    rep(i,m){
        cin >> b[i];
    }
    sort(ALL(a));
    sort(ALL(b));
    int ans = 1000000001;
    int tmp = 0;
    int i = 0;
    int j = 0;
    while(i<n && j<m){
        ans = min(ans, abs(a[i] - b[j]));
        if(a[i] > b[j]){
            j++;
        }else{
            i++;
        }
    }
    cout << ans;
}