#include <bits/stdc++.h>
#define rep(i, n) for(int i=0, i##_len=(n); i<i##_len; i++)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define pb push_back
using namespace std;
using ll = long long;
int main(void){
    ll n, k;
    cin >> n >> k;
    vector<ll> lst;
    rep(i, n){
        ll a,b,c;
        cin >> a >> b >> c;
        lst.pb(a+b+c);
    }
    vector<ll> lst2 = lst;
    sort(ALL(lst));
    ll point = lst[SZ(lst) - k];
    ll point2;
    rep(i, n){
        point2 = lst2[i] + 300;
        if (point2 >= point){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
    }
}