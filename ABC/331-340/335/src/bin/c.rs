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
    }
    let mut head: Vec<(i32, i32)> = vec![];
    for i in (0..n).rev() {
        head.push(((i + 1) as i32, 0));
    }

    for _ in 0..q {
        input! {
            a: usize,
            b: String
        }
        if a == 1 {
            let c = b.as_str();
            let prev = head.last().unwrap();
            match c {
                "U" => {
                    head.push((prev.0, prev.1 + 1));
                }
                "D" => {
                    head.push((prev.0, prev.1 - 1));
                }
                "L" => {
                    head.push((prev.0 - 1, prev.1));
                }
                "R" => {
                    head.push((prev.0 + 1, prev.1));
                }
                _ => {}
            }
        } else {
            let p = b.parse::<usize>().unwrap();
            let x = head[head.len() - p].0;
            let y = head[head.len() - p].1;
            println!("{} {}", x, y);
        }
    }
}
