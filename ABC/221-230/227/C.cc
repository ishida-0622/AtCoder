// #include <bits/stdc++.h>
// #define rep(i, n) for(int i=0, i##_len=(n); i<i##_len; i++)
// # define ALL(x) (x).begin(), (x).end()
// # define SZ(x) ((int)(x).size())
// # define pb push_back
// using namespace std;
// using ll = long long;

// int main(void){
//     ll n;
//     cin >> n;
//     int m = floor(sqrt(n));
//     ll cnt = 0;
//     ll i = 0;
//     while (i * i * i <= n){
//         i++;
//         for (ll j = i; j < m; j++){
//             for (ll k = j; k < n; k++){
//                 if (i * j * k <= n){
//                     cnt++;
//                 }else{
//                     break;
//                 }
//             }
//             if (i * j * j > n){
//                 break;
//             }
//         }
//     }
//     cout << cnt;
// }