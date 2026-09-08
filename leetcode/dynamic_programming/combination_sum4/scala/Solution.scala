object Solution {
  def solve(nums: Array[Int], target: Int): Int = {
    val dp = Array.fill(target + 1)(0)
    dp(0) = 1
    for (i <- 1 to target) {
      for (num <- nums) {
        if (i - num >= 0) dp(i) += dp(i - num)
      }
    }
    dp(target)
  }
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    println(Solution.solve(Array(1, 2, 3), 4))
  }
}
