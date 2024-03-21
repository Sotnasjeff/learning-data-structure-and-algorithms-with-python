package main

import (
	"container/heap"
	"fmt"
)

type IntegerHeap []int

func (ih IntegerHeap) Len() int {
	return len(ih)
}

func (ih IntegerHeap) Less(i, j int) bool {
	return ih[i] < ih[j]
}

func (ih IntegerHeap) Swap(i, j int) {
	ih[i], ih[j] = ih[j], ih[i]
}

func (ih *IntegerHeap) Push(heapintf interface{}) {
	*ih = append(*ih, heapintf.(int))
}

func (ih *IntegerHeap) Pop() interface{} {
	var n int
	var x1 int
	var previous IntegerHeap = *ih
	n = len(previous)
	x1 = previous[n-1]
	*ih = previous[0 : n-1]

	return x1
}

func main() {
	var intHeap *IntegerHeap = &IntegerHeap{2, 5, 9, 3}
	heap.Init(intHeap)
	heap.Push(intHeap, 2)
	fmt.Printf("minimum: %d\n", (*intHeap)[0])
	for intHeap.Len() > 0 {
		fmt.Printf("%d\n", heap.Pop(intHeap))
	}
}
