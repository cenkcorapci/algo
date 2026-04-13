object Solution {
  def solve(nums: Array[Int], target: Int): Array[Int] = {
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    for (i <- nums.indices) {
      val complement = target - nums(i)
      if (seen.contains(complement)) return Array(seen(complement), i)
      seen(nums(i)) = i
    }
    Array()
  }
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    val res = Solution.solve(Array(2,7,11,15), 9)
    println(res.mkString("[", ", ", "]"))
  }
}

