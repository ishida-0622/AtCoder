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
    ll n;
    cin >> n;
    string ans;
    while (n > 0) {
        if (n % 2 == 0) {
            ans += "B";
            n /= 2;
        } else {
            ans += "A";
            n -= 1;
        }
    }
    reverse(ALL(ans));
    cout << ans << endl;
}