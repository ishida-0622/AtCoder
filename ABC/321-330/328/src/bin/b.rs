use std::collections::HashSet;

use proconio::input;

const MOD: i32 = 998244353;
const MOD2: i32 = 1000000007;
const INF: i64 = 1 << 60;
const MINF: i64 = -(1 << 60);

fn yes() {
    println!("Yes");
    std::process::exit(0);
}

fn no() {
    println!("No");
    std::process::exit(0);
}

fn yes_no(b: bool) {
    if b {
        println!("Yes");
    } else {
        println!("No");
    }
}

fn main() {
    input! {
        n: usize,
        lst: [usize; n],
    }
    let mut ans = 0;
    for i in 1..n + 1 {
        let v = lst[i - 1];
        for j in 1..v + 1 {
            let s = format!("{}{}", i, j);
            let st: HashSet<char> = HashSet::from_iter(s.chars().into_iter());
            if st.len() == 1 {
                ans += 1;
            }
        }
    }
    println!("{}", ans);
}
