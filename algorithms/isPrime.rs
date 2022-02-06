use std::io;
use std::time::{Instant};

fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    for a in 2..n {
        if n % a == 0 {
            return false; // if it is not the last statement you need to use `return`
        }
    }
    true // last value to return
}

fn main() {
    println!("Enter a positive integer: ");
    let mut input_line = String::new();
    io::stdin()
        .read_line(&mut input_line)
        .expect("Failed to read line");
    let x: i32 = input_line.trim().parse().expect("Input not an integer");

    let start = Instant::now();
    let result = is_prime(x);
    let duration = start.elapsed();

    println!("{}", result);
    println!("{:?}", duration);
}
