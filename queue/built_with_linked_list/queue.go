package builtwithlinkedlist

type Node struct {
	Value int
	Next  *Node
}

type Queue struct {
	Top    *Node
	Bottom *Node
	Length int
}

func(q *Queue) Enqueue(value int) {
	newNode := &Node{
		Value: value,
		Next: nil,
	}

	if q.Length == 0 {
		q.Top = newNode
	} else {
		currentNode := q.Top
		for currentNode.Next != nil {
			currentNode = currentNode.Next
		}

		currentNode.Next = newNode
	}
	q.Bottom = newNode
	q.Length++
}

func(q *Queue) Dequeue(){
	if q.Length == 1 {
		q.Bottom = nil
	}
	newHead := q.Top.Next
	q.Top = newHead
	q.Length--		
}

func(q *Queue) PrintQueue() []int {
	array := []int{}
	currentNode := q.Top
	for currentNode != nil {
		array = append(array, currentNode.Value)
		currentNode = currentNode.Next
	}
	return array
}

func(q *Queue) PrintQueueTop() int {
	if q.Top == nil {
		return 0
	}
	return q.Top.Value
}

func(q *Queue) PrintQueueBottom() int {
	if q.Bottom == nil {
		return 0
	}
	return q.Bottom.Value
}