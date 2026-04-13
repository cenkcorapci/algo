pppub fn solve(nums: &[i32], target: i32) -> Vec<usize> {
    use std::collections::HashMap;
    let mut seen: HashMap<i32, usize> = HashMap::new();
    for (i, &v) in nums.iter().enumerate() {
        let complement = target - v;
        if let Some(&j) = seen.get(&complement) {
            return vec![j, i];
        }
        seen.insert(v, i);
    }
    vec![]
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_examples() {
        assert_eq!(solve(&[2,7,11,15], 9), vec![0,1]);
        assert!(solve(&[1,2,3], 99).is_empty());
    }
}

