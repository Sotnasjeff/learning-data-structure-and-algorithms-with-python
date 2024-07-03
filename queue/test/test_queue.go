package main

import (
	"fmt"

	builtwithlinkedlist "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/queue/built_with_linked_list"
)

func main(){
	myQueue := builtwithlinkedlist.Queue{}
	myQueue.Enqueue(5)
	myQueue.Enqueue(10)
	myQueue.Enqueue(20)
	myQueue.Enqueue(999)
	fmt.Println("Top:", myQueue.PrintQueueTop())
	fmt.Println("Bottom:", myQueue.PrintQueueBottom())
	fmt.Println("Queue:", myQueue.PrintQueue())
	fmt.Println("Length:", myQueue.Length)
	fmt.Println("------------------------------")
	myQueue.Dequeue()
	fmt.Println("Top:", myQueue.PrintQueueTop())
	fmt.Println("Bottom:", myQueue.PrintQueueBottom())
	fmt.Println("Queue:", myQueue.PrintQueue())
	fmt.Println("Length:", myQueue.Length)
	fmt.Println("------------------------------")
	myQueue.Dequeue()
	fmt.Println("Top:", myQueue.PrintQueueTop())
	fmt.Println("Bottom:", myQueue.PrintQueueBottom())
	fmt.Println("Queue:", myQueue.PrintQueue())
	fmt.Println("Length:", myQueue.Length)
	fmt.Println("------------------------------")
	myQueue.Dequeue()
	fmt.Println("Top:", myQueue.PrintQueueTop())
	fmt.Println("Bottom:", myQueue.PrintQueueBottom())
	fmt.Println("Queue:", myQueue.PrintQueue())
	fmt.Println("Length:", myQueue.Length)
	fmt.Println("------------------------------")

}