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
    string s;
    cin >> s;
    vector<set<char>> stack;
    stack.push_back({});
    rep(i, s.length()) {
        if (s[i] == '(') {
            stack.push_back(stack[stack.size()-1]);
        } else if (s[i] == ')') {
            stack.pop_back();
        } else {
            if (stack[stack.size()-1].find(s[i]) != stack[stack.size()-1].end()) {
                cout << "No" << endl;
                return 0;
            }
            stack[stack.size()-1].insert(s[i]);
        }
    }
    cout << "Yes" << endl;
}
