//Kotlin program to find the element is occuring onn number of times
//It is given that there is only 1 element that is occurring odd number of times
//Time Complexity: O(n) Space Complexity: O(1)

import java.util.Scanner;
import java.util.ArrayList

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    
    println("Enter the size of the array: ")
    val arraySize: Int = sc.nextInt()

    val array = arrayListOf<Int>()
    println("Enter the elements of the array: ")
    for(i in 0 until arraySize){
        val element = sc.nextInt()
        array.add(element)
    }

    val res = findSingleNumber(array)
    println("The single number that is occurring odd no. of times is : $res")
}

fun findSingleNumber(array: ArrayList<Int>): Int {
    var res = 0
    for(element in array){
        res = res xor element 
    }
    return res
}   