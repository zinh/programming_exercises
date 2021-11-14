extern crate clap;
use std::io;
use std::io::Read;
use clap::{App,Arg};

fn main() -> io::Result<()> {
    let matches = App::new("Sample App")
        .arg(Arg::with_name("input file")
             .short("f")
             .long("file")
             .value_name("FILE")
             .takes_value(true))
        .get_matches();
    println!("{:?}", matches);
    let mut buffer = String::new();
    io::stdin().read_to_string(&mut buffer)?;
    println!("{}", buffer);
    Ok(())
}
