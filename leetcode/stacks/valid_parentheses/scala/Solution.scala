object Solution {
  def solve(s: String): Boolean = {
    val open = scala.collection.mutable.Stack[Char]()
    val pairs = Map(')' -> '(', ']' -> '[', '}' -> '{')
    for (c <- s) {
      if (c == '(' || c == '[' || c == '{') {
        open.push(c)
      } else {
        if (open.isEmpty || open.pop() != pairs(c)) return false
      }
    }
    open.isEmpty
  }
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    println(Solution.solve("()[]{}"))
  }
}
