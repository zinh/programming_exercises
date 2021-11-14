use std::io;
use std::io::Read;
use std::env;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    let mut buffer = String::new();
    io::stdin().read_to_string(&mut buffer)?;
    println!("{}", buffer);
    Ok(())
}
