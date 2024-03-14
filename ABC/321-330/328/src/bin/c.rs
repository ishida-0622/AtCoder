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
        q: usize,
        s: String,
    }
    let mut acc = vec![0];
    let s = s.chars().collect::<Vec<char>>();
    for i in 1..n {
        if &s[i] == &s[i - 1] {
            acc.push(acc[i - 1] + 1);
        } else {
            acc.push(acc[i - 1]);
        }
    }
    for _ in 0..q {
        input! {
            l: usize,
            r: usize,
        }
        println!("{}", acc[r - 1] - acc[l - 1]);
    }
}
