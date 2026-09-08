pub fn solve(nums: &[i32], target: i32) -> i32 {
    let target = target as usize;
    let mut dp = vec![0; target + 1];
    dp[0] = 1;
    for i in 1..=target {
        for &num in nums {
            let num = num as usize;
            if i >= num {
                dp[i] += dp[i - num];
            }
        }
    }
    dp[target]
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_example() {
        assert_eq!(solve(&[1, 2, 3], 4), 7);
    }
}
