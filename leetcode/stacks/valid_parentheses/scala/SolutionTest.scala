object SolutionTest {
  def main(args: Array[String]): Unit = {
    assert(Solution.solve("()"))
    assert(Solution.solve("()[]{}"))
    assert(!Solution.solve("(]"))
    assert(!Solution.solve("([)]"))
    assert(!Solution.solve("("))
    println("OK")
  }
}
