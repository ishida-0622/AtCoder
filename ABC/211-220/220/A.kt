fun main() {
    val reader = System.`in`.bufferedReader()
    var (a,b,c) = reader.readLine()!!.split(" ").map {it.toInt()}
    var ans = -1
    for (i in a..b) {
        if (i % c == 0){
            ans = i
            break
        }
    }
    print(ans)
}