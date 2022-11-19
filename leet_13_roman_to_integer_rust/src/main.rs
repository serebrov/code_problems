// https://leetcode.com/problems/roman-to-integer/

pub fn romans(number: char) -> i32 {
    match number {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M'=> 1000,
        _ => panic!()
    }
}

pub fn roman_value(current: char, previous: char) -> i32 {
    let value = romans(current);
    let need_subtract = previous == 'V' && current == 'I' ||
        previous == 'X' && current == 'I' ||
        previous == 'X' && current == 'I' ||
        previous == 'L' && current == 'X' ||
        previous == 'C' && current == 'X' ||
        previous == 'D' && current == 'C' ||
        previous == 'M' && current == 'C';
    if need_subtract {
       -1 * value
    } else {
       value
    }
}

struct Solution {}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut result = 0;
        let mut prev_roman = ' ';
        for curr_roman in s.chars().rev() {
          result += roman_value(curr_roman, prev_roman);
          prev_roman = curr_roman;
        }
        return result
    }
}

fn main() {
    println!("III: {:?}", Solution::roman_to_int("III".to_string()));
    println!("LVIII: {:?}", Solution::roman_to_int("LVIII".to_string()));
    println!("MCMXCIV: {:?}", Solution::roman_to_int("MCMXCIV".to_string()));
}
