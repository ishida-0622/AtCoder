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
int main(void){
    int n,k;
    cin >> n >> k;
    vi v = vi(n);
    rep(i,n){
        cin >> v[i];
    }
    vector<bool> flg = vector<bool>(n+1);
    rep(i,n){
        flg[i+1] = false;
    }
    rep(i,k){
        flg[v[i]] = true;
    }
    int m,l;
    l = 100000000;
    rep(i,k){
        if(l > v[i]){
            l = v[i];
        }
    }
    cout << l << endl;
    _rep(i,k,n){
        m = v[i];
        flg[m] = true;
        if(m > l){
            _rep(j,l+1,n+1){
                if(flg[j]){
                    l = j;
                    break;
                }
            }
        }
        cout << l << endl;
    }
}