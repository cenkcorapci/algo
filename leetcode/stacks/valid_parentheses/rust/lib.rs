pub fn solve(s: &str) -> bool {
    let mut open = Vec::new();
    for c in s.chars() {
        match c {
            '(' | '[' | '{' => open.push(c),
            ')' => {
                if open.pop() != Some('(') {
                    return false;
                }
            }
            ']' => {
                if open.pop() != Some('[') {
                    return false;
                }
            }
            '}' => {
                if open.pop() != Some('{') {
                    return false;
                }
            }
            _ => return false,
        }
    }
    open.is_empty()
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_examples() {
        assert!(solve("()"));
        assert!(solve("()[]{}"));
        assert!(!solve("(]"));
        assert!(!solve("([)]"));
        assert!(!solve("("));
    }
}
