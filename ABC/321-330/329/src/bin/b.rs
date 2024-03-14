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
        lst: [i64; n],
    }
    let mut ans = &MINF;
    let max = lst.iter().max().unwrap();
    for v in &lst {
        if v == max {
            continue;
        }
        ans = ans.max(v);
    }
    println!("{}", ans);
}
