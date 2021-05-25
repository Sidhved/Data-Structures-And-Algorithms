//kotlin program for insertion sort

fun insertionSort(list: MutableList<Int>): List<Int>{
    //go from the 2nd item in the list till the last item
    for(i in 1 until list.size){
        //store the value
        val value = list[i]
        //store the index of the value
        var temp = i
    //for every new value below the index of the value 
    //if the new value is greater than the value

    //if the value is not greater then the loop will end
    
    while((list[temp-1] > value) and (temp >= 2)){
        //put new value one index above the current value
        list[temp] = list[temp-1]
        //decrease the temp index
        temp -= 1
    }
    //when loop has ended we know that the value at index less, then current temp is lesser than current value so replace value at temp and close the loop
    list[temp] = value
    }
    return list
}

fun main() {
    print("Enter the number of items to sort: ")
    val lengthOfList = readLine()!!.toInt()
    val list = MutableList(lengthOfList){0}
    list.withIndex().forEach{
        print("Enter value ${it.index + 1} : ")
        list[it.index] = readLine()!!.toInt()
    }
    println("Unsorted List: $list")
    val sorted = insertionSort(list.toMutableList());
    println("Sorted List: $sorted")
}