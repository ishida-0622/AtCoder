fun main() {
    var (n, m) = readLine()!!.split(".")
    var ans: String = ""
    if (m < "3"){
        ans += "-"
    } else if (m > "6") {
        ans += "+"
    }
    println(n + ans)
}