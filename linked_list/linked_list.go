package linkedlist

type Node struct {
	Value int
	Next  *Node
}

type LinkedList struct {
	Head   *Node
	Length int
}

func (ll *LinkedList) Append(value int) {
	newNode := &Node{
		Value: value,
		Next:  nil,
	}

	if ll.Head == nil {
		ll.Head = newNode
	} else {
		current := ll.Head
		for current.Next != nil {
			current = current.Next
		}
		current.Next = newNode
	}

	ll.Length++
}

func (ll *LinkedList) Prepend(value int) {
	newNode := &Node{
		Value: value,
		Next:  nil,
	}

	newNode.Next = ll.Head
	ll.Head = newNode
	ll.Length++
}

func (ll *LinkedList) InsertByIndex(index, value int) {
	newNode := &Node{
		Value: value,
		Next:  nil,
	}

	if index == 0 {
		ll.Prepend(value)
	} else {
		currentNode := ll.GetByIndex(index - 1)
		currentNextNode := currentNode.Next
		newNode.Next = currentNextNode
		currentNode.Next = newNode
		ll.Length++
	}
}

func (ll *LinkedList) Remove(index int) {
	if index == 0 {
		nextNode := ll.Head.Next
		ll.Head = nextNode
		ll.Length--
	} else {
		if index > ll.Length {
			index = ll.Length - 1
		}
		currentNode := ll.GetByIndex(index - 1)
		unwantedNode := currentNode.Next
		currentNode.Next = unwantedNode.Next
		ll.Length--
	}
}

func (ll *LinkedList) GetByIndex(index int) *Node {
	currentNode := ll.Head
	counter := 0
	for index != counter && currentNode.Next != nil {
		currentNode = currentNode.Next
		counter++
	}

	return currentNode
}

func (ll *LinkedList) PrintList() []int {
	array := []int{}
	currentNode := ll.Head
	for currentNode != nil {
		array = append(array, currentNode.Value)
		currentNode = currentNode.Next
	}
	return array
}
