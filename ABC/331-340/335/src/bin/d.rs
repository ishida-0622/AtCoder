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
    }
    let mut v = vec![vec![0; n]; n];
    let mut cnt = 1;
    let mut loop_cnt = 0;
    while loop_cnt < n / 2 {
        for i in loop_cnt..n - loop_cnt {
            v[loop_cnt][i] = cnt;
            cnt += 1;
        }
        cnt -= 1;
        for i in loop_cnt..n - loop_cnt {
            v[i][n - loop_cnt - 1] = cnt;
            cnt += 1;
        }
        cnt -= 1;
        for i in loop_cnt..n - loop_cnt {
            v[n - loop_cnt - 1][n - i - 1] = cnt;
            cnt += 1
        }
        cnt -= 1;
        for i in loop_cnt..n - loop_cnt - 1 {
            v[n - i - 1][loop_cnt] = cnt;
            cnt += 1;
        }
        loop_cnt += 1;
    }
    for i in 0..n {
        for j in 0..n {
            if i == j && i == (n - 1) / 2 {
                print!("T ");
                continue;
            }
            if j == n - 1 {
                print!("{}", v[i][j]);
                continue;
            }
            print!("{} ", v[i][j]);
        }
        println!();
    }
}
