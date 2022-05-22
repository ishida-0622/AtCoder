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
    ll ans = 0,cnt = 0;
    ll n;
    cin >> n;
    string s;
    cin >> s;
    rep(i,n-1){
        if(s[i] == s[i+1]){
            cnt++;
        }else{
            ans += (cnt+1) * cnt / 2;
            cnt = 0;
        }
    }
    ans += (cnt+1) * cnt / 2;
    cout << ans;
}