pub fn solve(mut n: u32) -> u32 {
    let mut result = 0u32;
    for _ in 0..32 {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }
    result
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_example() {
        assert_eq!(solve(43261596), 964176192);
    }
}
