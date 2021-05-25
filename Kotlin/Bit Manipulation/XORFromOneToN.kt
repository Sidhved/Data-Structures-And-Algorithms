//A kotlin program to find the XOR of 1 to N

import java.util.Scanner;

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)

    println("Enter the limit till which XOR should be found : ")
    val n: Int = sc.nextInt()

    val res = XOROfOneToN(n)
    println("The XOR of 1 to N is : $res")
}

fun XOROfOneToN(n: Int): Int {
    //XOR of 1 to any multiple of 4 is always 0, thus it is just enough to find xor of remaining numbers
    return when{
        n % 4 == 0 -> {
            0
        }
        n % 4 == 1 -> {
            n
        }
        n % 4 == 2 -> {
            n xor (n - 1)
        }
        else -> {
            n xor (n - 1) xor (n - 2)
        }
    }
}