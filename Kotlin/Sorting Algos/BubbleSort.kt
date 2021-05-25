//Kotlin Program for bubble sort

fun bubbleSort(list: MutableList<Int>): List<Int>{
    //noting list length
    val length = list.size -1

    //the first loop runs for the number of items there are in the list
    for(i in 0 until length){
        //a swapped variable which tracks if one of the variables was swapped in one iteration
        var swapped = false
        //inner loop going from first element till the last element
        //in each round we have the last element as the greatest number
        //so next round has one less element
        //i.e. equal to the number of iteration we are in currently
        for(j in 0 until (length-i)){
            //if the current element is bigger than the next element
            if(list[i]>list[j+1]){
                //do the swap
                list[j+1] = list[j].also{list[j] = list[j+1]}   //used also inbuilt function
                swapped = true
            }
        }
        //check if any swaps happened in this iteration. if there arent any swaps then leave the function and declare list as sorted
        if(!swapped){
            return list
        }
    }
    return list
}

fun main(args: Array<String>) {
    val list = listOf(11, 22, 33, 45, 34, 53, 27, 36)
    println("Unsorted list: $list")
    val sorted = bubbleSort(list.toMutableList());
    println("Sorted list: $sorted")
}