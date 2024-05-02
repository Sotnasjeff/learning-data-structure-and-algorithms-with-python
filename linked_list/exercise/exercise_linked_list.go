package main

import (
	"fmt"

	linkedlist "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/linked_list"
)

func main() {

	myLinkedList := linkedlist.LinkedList{}
	myLinkedList.Insert(5)
	myLinkedList.Insert(10)
	myLinkedList.Insert(6)
	myLinkedList.Insert(9)
	myLinkedList.InsertByIndex(2, 99)
	myLinkedList.InsertByIndex(0, 100000)

	fmt.Println(myLinkedList.Length)
	fmt.Println(myLinkedList.PrintList())
}
