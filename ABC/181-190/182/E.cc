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
    ll h, w, n, m;
    cin >> h >> w >> n >> m;
    ll ans = 0;
    vector<vector<ll>> light_h(h);
    vector<vector<ll>> light_w(w);
    vector<vector<ll>> block_h(h);
    vector<vector<ll>> block_w(w);
    set<pair<ll, ll>> light;
    set<pair<ll, ll>> block;
    rep(i, h) {
        light_h[i].push_back(-3000LL);
        light_h[i].push_back(3000LL);
        block_h[i].push_back(-2000LL);
        block_h[i].push_back(2000LL);
    }
    rep(i, w) {
        light_w[i].push_back(-3000LL);
        light_w[i].push_back(3000LL);
        block_w[i].push_back(-2000LL);
        block_w[i].push_back(2000LL);
    }
    rep(i, n) {
        ll a, b;
        cin >> a >> b;
        pair<ll, ll> ab = {--a, --b};
        light.insert(ab);
        light_h[a].push_back(b);
        light_w[b].push_back(a);
    }
    rep(i, m) {
        ll c, d;
        cin >> c >> d;
        pair<ll, ll> cd = {--c, --d};
        block.insert(cd);
        block_h[c].push_back(d);
        block_w[d].push_back(c);
    }
    rep(i, h) {
        sort(ALL(light_h[i]));
        sort(ALL(block_h[i]));
    }
    rep(i, w) {
        sort(ALL(light_w[i]));
        sort(ALL(block_w[i]));
    }

    // rep(i, h) {
    //     for (auto j : light_h[i]){
    //         cout << j << endl;
    //     }
    //     cout << endl;
    // }

    rep(i, h) {
        rep(j, w) {
            pair<ll, ll> ij = {i, j};
            if (light.find(ij) != light.end()) {
                ans++;
                continue;
            }
            if (block.find(ij) != block.end()) {
                continue;
            }
            ll a = distance(light_h[i].begin(), lower_bound(light_h[i].begin(), light_h[i].end(), j));
            ll b = distance(light_w[j].begin(), lower_bound(light_w[j].begin(), light_w[j].end(), i));
            ll c = distance(block_h[i].begin(), lower_bound(block_h[i].begin(), block_h[i].end(), j));
            ll d = distance(block_w[j].begin(), lower_bound(block_w[j].begin(), block_w[j].end(), i));
            if (light_h[i][a-1] > block_h[i][c-1]) {
                ans++;
                continue;
            }
            if (light_h[i][a] < block_h[i][c]) {
                ans++;
                continue;
            }
            if (light_w[j][b-1] > block_w[j][d-1]) {
                ans++;
                continue;
            }
            if (light_w[j][b] < block_w[j][d]) ans++;
        }
    }

    cout << ans << endl;
}
