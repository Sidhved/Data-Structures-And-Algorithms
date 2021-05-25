import java.util.Scanner;
//Kotlin program to find if the given number is a power of two
//Time Complexity: O(log n) Space Complexity: O(1)

fun isPowerOfTwo(n:Int): Boolean {
    //A number is said to be a Power of 2 if it has only 1 set bit.
    var setBitsCount = 0
    var num = n

    while(num>0){
        if(num%2 == 1)
            setBitsCount++
        num /= 2
    }
    return setBitsCount == 1
}

fun main(args: Array<String>) {
    
    val sc = Scanner(System.`in`)

    println("Enter the number to check whether it is a power of 2 or not : ")
    val n: Int = sc.nextInt()

    val res = isPowerOfTwo(n)
    if(res)
        println("Number: $n is power of 2")
    else
        println("Number: $n is not power of 2") 
}

