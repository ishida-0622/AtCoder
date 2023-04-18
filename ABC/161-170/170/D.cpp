#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define _rep(i, a, b) for (int i = a, i##_len = (int)(b); i < i##_len; i++)
#define rep(i, n) _rep(i,0,n)
#define reps(i, n) _rep(i,1,n+1)
#define rrep(i, n) for (int i = n-1; i >= 0; i--)
#define rreps(i, n) for (int i = n; i >= 1; i--)
#define ALL(x) (x).begin(), (x).end()
#define YesNo(flag) if(flag){cout<<"Yes"<<endl;}else{cout<<"No"<<endl;}
#define _10_5 100010
#define _2_10_5 200010
#define mod 998244353
#define mod2 1000000007
#define inf 1000000000
#define INF 1000000000000000000L
// sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[N] < beta[N];}); <- N番目の要素でソート


int cnt[1000010];

set<int> f(int n) {
    set<int> res;
    reps(i, ceil(sqrt(n))) {
        if (n % i == 0) {
            res.insert(i);
            res.insert(n / i);
        }
    }
    res.insert(n);
    if (cnt[n] == 1) {
        res.erase(n);
    }
    return res;
}

int main(void){
    int n;
    cin >> n;
    vector<int> lst(n);
    set<int> st;
    rep(i, n) {
        int a;
        cin >> a;
        lst[i] = a;
        st.insert(a);
        cnt[a]++;
    }
    vector<set<int>> p(n);
    rep(i, n) p[i] = f(lst[i]);
    int ans = 0;
    for (auto val : p) {
        bool ok = true;
        for (auto v : val) {
            if (st.count(v)) {
                ok = false;
                break;
            }
        }
        if (ok) ans++;
    }
    cout << ans << endl;
}
