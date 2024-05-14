package doublylinkedlist

type Node struct {
	Value    int
	Previous *Node
	Next     *Node
}

type DoublyLinkedList struct {
	Head   *Node
	Length int
}

func (dl *DoublyLinkedList) Append(value int) {
	newNode := &Node{
		Value:    value,
		Next:     nil,
		Previous: nil,
	}

	if dl.Head == nil {
		dl.Head = newNode
	} else {
		current := dl.Head
		for current.Next != nil {
			current = current.Next
		}
		newNode.Previous = current
		current.Next = newNode
	}

	dl.Length++
}

func (dl *DoublyLinkedList) Prepend(value int) {
	newNode := &Node{
		Value:    value,
		Next:     nil,
		Previous: nil,
	}

	newNode.Next = dl.Head
	dl.Head.Previous = newNode
	dl.Head = newNode
	dl.Length++
}

func (dl *DoublyLinkedList) InsertByIndex(index, value int) {
	newNode := &Node{
		Value:    value,
		Next:     nil,
		Previous: nil,
	}

	if index == 0 {
		dl.Prepend(value)
	} else {
		currentNode := dl.GetByIndex(index - 1)
		nextNodeFromCurrent := currentNode.Next

		newNode.Next = nextNodeFromCurrent
		newNode.Previous = currentNode

		currentNode.Next = newNode
		dl.Length++
	}
}

func (dl *DoublyLinkedList) Remove(index int) {
	if index == 0 {
		nextNode := dl.Head.Next
		dl.Head.Previous = nil
		dl.Head = nextNode
		dl.Length--
	} else {
		if index > dl.Length {
			index = dl.Length - 1
		}
		currentNode := dl.GetByIndex(index - 1)
		unwantedNode := currentNode.Next
		currentNode.Next = unwantedNode.Next
		dl.Length--
	}
}

func (dl *DoublyLinkedList) GetByIndex(index int) *Node {
	currentNode := dl.Head
	counter := 0
	for index != counter && currentNode.Next != nil {
		currentNode = currentNode.Next
		counter++
	}

	return currentNode
}

func (dl *DoublyLinkedList) PrintList() []int {
	array := []int{}
	currentNode := dl.Head
	for currentNode != nil {
		array = append(array, currentNode.Value)
		currentNode = currentNode.Next
	}
	return array
}
