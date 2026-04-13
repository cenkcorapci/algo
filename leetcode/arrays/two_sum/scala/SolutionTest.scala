object SolutionTest {
  def main(args: Array[String]): Unit = {
    val got = Solution.solve(Array(2,7,11,15), 9)
    assert(got.sameElements(Array(0,1)))
    val got2 = Solution.solve(Array(1,2,3), 99)
    assert(got2.isEmpty)
    println("OK")
  }
}

