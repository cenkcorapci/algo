case class ListNode(var x: Int = 0, var next: ListNode = null)

object Solution {
  def mergeTwoLists(list1: ListNode, list2: ListNode): ListNode = {
    val dummy = ListNode(0)
    var tail = dummy
    var a = list1
    var b = list2
    while (a != null && b != null) {
      if (a.x <= b.x) {
        tail.next = a
        a = a.next
      } else {
        tail.next = b
        b = b.next
      }
      tail = tail.next
    }
    tail.next = if (a != null) a else b
    dummy.next
  }

  def buildList(values: Array[Int]): ListNode = {
    val dummy = ListNode(0)
    var tail = dummy
    for (value <- values) {
      tail.next = ListNode(value)
      tail = tail.next
    }
    dummy.next
  }

  def toArray(head: ListNode): Array[Int] = {
    val values = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      values += cur.x
      cur = cur.next
    }
    values.toArray
  }

  def solve(list1: Array[Int], list2: Array[Int]): Array[Int] =
    toArray(mergeTwoLists(buildList(list1), buildList(list2)))
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    println(Solution.solve(Array(1, 2, 4), Array(1, 3, 4)).mkString("[", ", ", "]"))
  }
}
