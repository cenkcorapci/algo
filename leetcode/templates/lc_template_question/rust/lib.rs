pub fn solve(input: &str) -> String {
    input.trim().to_string()
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_trim() {
        assert_eq!(solve("  abc  \n"), "abc");
    }
}

