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
        s: String,
    }
    println!(
        "{}",
        s.chars()
            .map(|c| c.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
