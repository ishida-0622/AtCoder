fun intIn() = readLine()!!.toInt()

fun mapInt() = readLine()!!.split(" ").map { it.toInt() }

fun min(x: Int, y: Int) = if (x < y) x else y

fun max(x: Int, y: Int) = if (x > y) x else y

fun main() {
    val n = intIn()
    val lst = mapInt()
    var ans = 0
    for (i in 0..n - 1) {
        var _min = lst[i]
        for (j in i..n - 1) {
            _min = min(_min, lst[j])
            ans = max(ans, _min * (j - i + 1))
        }
    }
    println(ans)
}
