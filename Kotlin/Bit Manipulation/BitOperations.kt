//Bitwise and bit shift operators are used on only two integral types
//(Int and Long) to perform bit-level operations.
//Time Complexity O(1), Space Comeplexity O(1)

import java.util.Scanner

fun main(args: Array<String>){
    val sc = Scanner(System.`in`)
    println("Enter Two numbers : ")
    val num1 : Int = sc.nextInt()
    val num2 : Int = sc.nextInt()

    var res : Int

    println("Basic Bit Operations are")

    res = num1 or num2
    println("OR Operation :$res")

    res = num1 and num2
    println("AND Operation :$res")

    res = num1 xor num2
    println("XOR Operation :$res")

    res = num1.inv()
    println("Complement Operation :$res")
}