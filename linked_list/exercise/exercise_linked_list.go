package main

import (
	"fmt"

	linkedlist "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/linked_list"
)

func main() {

	myLinkedList := linkedlist.LinkedList{}
	myLinkedList.Append(5)
	myLinkedList.Prepend(10)
	myLinkedList.Append(6)
	myLinkedList.Prepend(9)
	myLinkedList.Append(50)
	myLinkedList.Prepend(0)
	myLinkedList.Append(99)
	myLinkedList.InsertByIndex(0, 5555)

	fmt.Println(myLinkedList.Length)
	fmt.Println(myLinkedList.PrintList())

	fmt.Println(myLinkedList.GetByIndex(2))
}
