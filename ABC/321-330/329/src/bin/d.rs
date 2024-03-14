use proconio::input;
use std::{
    collections::{BTreeSet, HashMap},
    vec,
};

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
        m: usize,
        lst: [usize; m],
    }
    let mut max = 0;
    let mut a = vec![0; n + 1];
    let mut mp = HashMap::<usize, BTreeSet<usize>>::new();
    mp.insert(0, BTreeSet::new());
    for v in lst {
        a[v] += 1;
        let key = a[v];
        max = max.max(key);
        if !mp.contains_key(&key) {
            let mut st = BTreeSet::<usize>::new();
            st.insert(v);
            mp.insert(key, st);
        } else {
            mp.get_mut(&key).unwrap().insert(v);
        }
        mp.get_mut(&(key - 1)).unwrap().remove(&v);
        println!("{}", mp.get(&max).unwrap().iter().min().unwrap());
    }
}
