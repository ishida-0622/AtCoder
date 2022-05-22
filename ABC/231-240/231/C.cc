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
    ll n, q;
    cin >> n >> q;
    vi vec(n);
    rep(i, n){
        cin >> vec.at(i);
    }
    vvi lst(q, vi(3));
    rep(i, q){
        cin >> lst.at(i).at(0);
        lst.at(i).at(1) = i;
    }
    sort(ALL(vec));
    sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[0] < beta[0];});
    int cnt = 0;
    for(int i = q-1; i >= 0; i--){
        while(cnt < n-1 && vec.at(n-1-cnt) >= lst.at(i).at(0)){
            cnt++;
        }
        if(cnt == n-1 && vec.at(n-1-cnt) >= lst.at(i).at(0)){
            cnt++;
        }
        lst.at(i).at(2) = cnt;
    }
    sort(ALL(lst),[](const vector<int> &alpha,const vector<int> &beta){return alpha[1] < beta[1];});
    rep(i, q){
        cout << lst.at(i).at(2) << endl;
    }
}