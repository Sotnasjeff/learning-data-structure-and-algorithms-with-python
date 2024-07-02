package main

import (
	"fmt"

	builtwitharray "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/stack/built_with_array"
	builtwithlinkedlist "github.com/Sotnasjeff/learning-data-structure-and-algorithms-with-golang/stack/built_with_linked_list"
)

func main() {
	built_with_linked_list()
	built_with_array()

}

func built_with_linked_list() {
	myStack := builtwithlinkedlist.Stack{}
	myStack.Push(1)
	myStack.Push(2)
	myStack.Push(3)
	myStack.Push(4)
	fmt.Println("Stack:", myStack.PrintStack())
	fmt.Println("Top:", myStack.PrintStackTop())
	fmt.Println("Bottom:", myStack.PrintStackBottom())
	fmt.Println("---------------------")
	myStack.Pop()
	fmt.Println("Stack:", myStack.PrintStack())
	fmt.Println("Top:", myStack.PrintStackTop())
	fmt.Println("Bottom:", myStack.PrintStackBottom())
	fmt.Println("---------------------")
	myStack.Pop()
	fmt.Println("Stack:", myStack.PrintStack())
	fmt.Println("Top:", myStack.PrintStackTop())
	fmt.Println("Bottom:", myStack.PrintStackBottom())
	fmt.Println("---------------------")
	myStack.Pop()
	fmt.Println("Stack:", myStack.PrintStack())
	fmt.Println("Top:", myStack.PrintStackTop())
	fmt.Println("Bottom:", myStack.PrintStackBottom())
	fmt.Println("---------------------")
	myStack.Pop()
	fmt.Println("Stack:", myStack.PrintStack())
	fmt.Println("Top:", myStack.PrintStackTop())
	fmt.Println("Bottom:", myStack.PrintStackBottom())
	fmt.Println("---------------------")
}

func built_with_array() {
	myArrayStack := builtwitharray.Stack{}
	myArrayStack.Push(1)
	myArrayStack.Push(2)
	myArrayStack.Push(3)
	myArrayStack.Push(4)
	fmt.Println("Stack:", myArrayStack.PrintStack())
	fmt.Println("Top:", myArrayStack.PrintStackTop())
	fmt.Println("Bottom:", myArrayStack.PrintStackBottom())
	fmt.Println("Length:", myArrayStack.PrintLength())
	fmt.Println("---------------------")
	myArrayStack.Pop()
	fmt.Println("Stack:", myArrayStack.PrintStack())
	fmt.Println("Top:", myArrayStack.PrintStackTop())
	fmt.Println("Bottom:", myArrayStack.PrintStackBottom())
	fmt.Println("Length:", myArrayStack.PrintLength())
	fmt.Println("---------------------")
	myArrayStack.Pop()
	fmt.Println("Stack:", myArrayStack.PrintStack())
	fmt.Println("Top:", myArrayStack.PrintStackTop())
	fmt.Println("Bottom:", myArrayStack.PrintStackBottom())
	fmt.Println("Length:", myArrayStack.PrintLength())
	fmt.Println("---------------------")
	myArrayStack.Pop()
	fmt.Println("Stack:", myArrayStack.PrintStack())
	fmt.Println("Top:", myArrayStack.PrintStackTop())
	fmt.Println("Bottom:", myArrayStack.PrintStackBottom())
	fmt.Println("Length:", myArrayStack.PrintLength())
	fmt.Println("---------------------")
	myArrayStack.Pop()
	fmt.Println("Stack:", myArrayStack.PrintStack())
	fmt.Println("Top:", myArrayStack.PrintStackTop())
	fmt.Println("Bottom:", myArrayStack.PrintStackBottom())
	fmt.Println("Length:", myArrayStack.PrintLength())
	fmt.Println("---------------------")
}
