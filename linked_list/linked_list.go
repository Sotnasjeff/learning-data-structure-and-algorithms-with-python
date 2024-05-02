package linkedlist

type Node struct {
	Value int
	Next  *Node
}

type LinkedList struct {
	Head   *Node
	Length int
}

func (ll *LinkedList) Insert(value int) {
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

func (ll *LinkedList) InsertByIndex(index, value int) {
	newNode := &Node{
		Value: value,
		Next:  nil,
	}

	leader := ll.traverseToIndex(index - 1)

	holdingPoint := leader.Next
	leader.Next = newNode
	newNode.Next = holdingPoint
	ll.Length++
}

func (ll *LinkedList) traverseToIndex(index int) *Node {
	counter := 0
	currentNode := ll.Head
	for counter != index && currentNode.Next != nil {
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
