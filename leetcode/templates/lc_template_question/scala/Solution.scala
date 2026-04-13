object Solution {
  def solve(input: String): String = input.trim
}

object SolutionMain {
  def main(args: Array[String]): Unit = {
    val in = scala.io.Source.stdin.mkString
    println(Solution.solve(in))
  }
}

