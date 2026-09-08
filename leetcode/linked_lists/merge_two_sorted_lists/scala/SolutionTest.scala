object SolutionTest {
  def main(args: Array[String]): Unit = {
    assert(Solution.solve(Array(1, 2, 4), Array(1, 3, 4)).sameElements(Array(1, 1, 2, 3, 4, 4)))
    assert(Solution.solve(Array(), Array(0)).sameElements(Array(0)))
    assert(Solution.solve(Array(1, 2, 3), Array()).sameElements(Array(1, 2, 3)))
    println("OK")
  }
}
