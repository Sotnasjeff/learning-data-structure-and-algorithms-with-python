package main

import (
	"fmt"

	"github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/array"
	hashtable "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/hash_table"
)

func main() {
	fmt.Println("Hello World")
	testingArray()
	testingHashTable()
}

func testingHashTable() {
	myHashTable := hashtable.NewHashTable()
	myHashTable.Add(5, "amor")
	myHashTable.Add(4, true)
	myHashTable.Add(0, 2024)
	fmt.Println(myHashTable)
	fmt.Println(myHashTable.Get(5))

}

func testingArray() {
	var myArray array.Array
	myArray.Push(25)
	myArray.Push(63)
	myArray.Push(50)
	fmt.Println(myArray)
	fmt.Println(myArray.Get(1))
	myArray.Pop()
	fmt.Println(myArray)
	myArray.Push(66)
	myArray.Push(80)
	myArray.Push(53)
	fmt.Println(myArray)
	myArray.Delete(4)
	fmt.Println(myArray)
}
