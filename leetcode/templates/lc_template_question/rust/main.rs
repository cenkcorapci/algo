fn main() {
    use std::io::{self, Read};
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    println!("{}", algo_templates::solve(&s));
}

