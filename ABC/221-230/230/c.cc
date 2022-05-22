// #include <bits/stdc++.h>
// #define rep(i, n) for (int i = 0, i##_len = (n); i < i##_len; i++)
// #define ALL(x) (x).begin(), (x).end()
// #define SZ(x) ((int)(x).size())
// #define pb push_back
// using namespace std;
// typedef vector<int> vi;
// typedef vector<string> vs;
// typedef vector<vi> vvi;
// typedef long long ll;
// typedef long double ld;
// typedef int itn;
// int main(void){
//     ll n,a,b,p,q,r,s;
//     cin >> n >> a >> b >> p >> q >> r >> s;
//     p--;
//     r--;
//     ll x,y,z;
//     x = 1 - a;
//     y = 1 - b;
//     if(x < y){
//         x = y*1;
//     }
//     y = n - a;
//     z = n - b;
//     if(y > z){
//         y = z;
//     }
//     // x--;
//     // y--;
//     vector<vs> vec(q-p, vs(s-r));
//     for(ll i = 0; i < q-p; i++){
//         for(ll j = 0; j < s-r; j++){
//             vec.at(i).at(j) = ".";
//         }
//     }
//     ll aa,bb;
//     if(x)
//     for(ll i = x; i <= y; i++){
//         aa = a+i-p-1;
//         bb = b+i-r-1;
//         if(aa >= 0 && aa <= q-p+1 && bb >= 0 && bb <= s-r+1){
//             vec.at(aa).at(bb) = "#";
//         }
//     }
//     x = 1 - a;
//     y = b - n;
//     if(x < y){
//         x = y;
//     }
//     y = n - a;
//     z = b - 1;
//     if(y > z){
//         y = z;
//     }
//     // x--;
//     // y--;
//     for(ll i = x; i <= y; i++){
//         aa = a+i-p-1;
//         bb = b-i-r-1;
//         if(aa >= 0 && bb >= 0){
//             vec.at(aa).at(bb) = "#";
//         }
//     }
//     for(ll i = 0; i < q-p; i++){
//         for(ll j = 0; j < s-r; j++){
//             cout << vec.at(i).at(j);
//         }
//         cout << endl;
//     }
// }