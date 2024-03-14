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
    let mut stack: Vec<char> = vec![];
    for c in s.chars() {
        if stack.len() >= 2 {
            let ln = stack.len();
            if stack[ln - 2] == 'A' && stack[ln - 1] == 'B' && c == 'C' {
                stack.pop();
                stack.pop();
            } else {
                stack.push(c);
            }
        } else {
            stack.push(c);
        }
    }
    println!(
        "{}",
        stack
            .iter()
            .map(|v| v.to_string())
            .collect::<Vec<_>>()
            .join("")
    );
}
