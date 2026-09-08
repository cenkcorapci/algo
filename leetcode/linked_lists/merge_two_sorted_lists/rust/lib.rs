#[derive(Debug, PartialEq, Eq)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

pub fn merge_two_lists(
    mut list1: Option<Box<ListNode>>,
    mut list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0));
    let mut tail = &mut dummy;

    while list1.is_some() && list2.is_some() {
        let l1_val = list1.as_ref().unwrap().val;
        let l2_val = list2.as_ref().unwrap().val;
        if l1_val <= l2_val {
            let mut node = list1.take().unwrap();
            list1 = node.next.take();
            tail.next = Some(node);
        } else {
            let mut node = list2.take().unwrap();
            list2 = node.next.take();
            tail.next = Some(node);
        }
        tail = tail.next.as_mut().unwrap();
    }

    tail.next = if list1.is_some() { list1 } else { list2 };
    dummy.next
}

pub fn build_list(values: &[i32]) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode::new(0));
    let mut tail = &mut dummy;
    for &value in values {
        tail.next = Some(Box::new(ListNode::new(value)));
        tail = tail.next.as_mut().unwrap();
    }
    dummy.next
}

pub fn to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = Vec::new();
    while let Some(node) = head {
        values.push(node.val);
        head = node.next;
    }
    values
}

pub fn solve(list1: &[i32], list2: &[i32]) -> Vec<i32> {
    to_vec(merge_two_lists(build_list(list1), build_list(list2)))
}

#[cfg(test)]
mod tests {
    use super::solve;

    #[test]
    fn test_examples() {
        assert_eq!(solve(&[1, 2, 4], &[1, 3, 4]), vec![1, 1, 2, 3, 4, 4]);
        assert_eq!(solve(&[], &[0]), vec![0]);
        assert_eq!(solve(&[1, 2, 3], &[]), vec![1, 2, 3]);
    }
}
