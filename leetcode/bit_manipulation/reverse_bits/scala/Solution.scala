object Solution {
  def solve(n: Long): Long = {
    var value = n
    var result = 0L
    var i = 0
    while (i < 32) {
      result = (result << 1) | (value & 1L)
      value >>= 1
      i += 1
    }
    result
  }
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    println(Solution.solve(43261596L))
  }
}
