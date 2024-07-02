package builtwithlinkedlist

type Node struct {
	Value int
	Next  *Node
}

type Stack struct {
	Top    *Node
	Bottom *Node
	Length int
}

func (s *Stack) Peek() *Node {
	return s.Top
}

func (s *Stack) Push(value int) {
	newNode := &Node{
		Value: value,
		Next:  nil,
	}

	if s.Length == 0 {
		s.Top = newNode
	} else {
		currentNode := s.Top
		for currentNode.Next != nil {
			currentNode = currentNode.Next
		}
		currentNode.Next = newNode
	}

	s.Bottom = newNode
	s.Length++
}

func (s *Stack) Pop() {
	if s.Top == nil {
		return
	} else if s.Length == 1 {
		s.Top = nil
		s.Bottom = nil
		s.Length--
		return
	}

	secondLastNode := s.getByIndex(s.Length - 2)
	unwantedNode := secondLastNode.Next
	secondLastNode.Next = unwantedNode.Next
	s.Bottom = secondLastNode
	s.Length--
}

func (s *Stack) getByIndex(index int) *Node {
	currentNode := s.Top
	counter := 0
	for counter != index && currentNode.Next != nil {
		currentNode = currentNode.Next
		counter++
	}

	return currentNode
}

func (s *Stack) PrintStack() []int {
	array := []int{}
	currentNode := s.Top
	for currentNode != nil {
		array = append(array, currentNode.Value)
		currentNode = currentNode.Next
	}
	return array
}

func (s *Stack) PrintStackTop() int {
	if s.Top == nil {
		return 0
	}
	return s.Top.Value
}

func (s *Stack) PrintStackBottom() int {
	if s.Bottom == nil {
		return 0
	}
	return s.Bottom.Value
}
