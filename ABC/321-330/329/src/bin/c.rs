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
        s: String,
    }
    let mut last_char = ' ';
    let mut count = 0;
    let mut st = std::collections::HashSet::<String>::new();
    for c in s.chars() {
        if c != last_char {
            last_char = c;
            count = 1;
        } else {
            count += 1;
        }
        st.insert(format!("{}{}", c, count));
    }
    println!("{}", st.len());
}
