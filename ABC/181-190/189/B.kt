fun main() {
    val (N, X) = readLine()!!.split(" ").map { it.toInt() }
    var ans = -1
    var tmp = 0
    for (i: Int in 1..N) {
        val (v, p) = readLine()!!.split(" ").map { it.toInt() }
        tmp += v * p
        if (tmp > X * 100) {
            ans = i
            break
        }
    }
    println(ans)
}
