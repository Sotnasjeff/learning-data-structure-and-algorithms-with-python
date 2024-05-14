package main

import (
	"fmt"

	doublylinkedlist "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/doubly_linked_list"
)

func main() {

	myDoublyLinkedList := doublylinkedlist.DoublyLinkedList{}
	myDoublyLinkedList.Append(5)
	myDoublyLinkedList.Append(6)
	myDoublyLinkedList.Prepend(8)
	myDoublyLinkedList.Prepend(8)
	myDoublyLinkedList.InsertByIndex(3, 999)
	myDoublyLinkedList.Remove(4)

	fmt.Println(myDoublyLinkedList.PrintList())
}
