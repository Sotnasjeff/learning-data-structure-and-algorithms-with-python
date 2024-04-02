package array

type Array struct {
	length int64
	data   []int64
}

func NewArray() *Array {
	return &Array{
		length: 0,
		data:   make([]int64, 0),
	}
}

func (a *Array) Get(index int64) int64 {
	return a.data[index]
}

func (a *Array) Push(item int64) int64 {
	a.data = append(a.data, item)
	a.length++
	return a.length
}

func (a *Array) Pop() {
	a.data = a.data[:a.length-1]
	a.length--
}

func (a *Array) Delete(index int64) int64 {
	item := a.data[index]
	a.shiftItems(index)
	return item
}

func (a *Array) shiftItems(index int64) {
	for i := index; i < a.length-1; i++ {
		a.data[i] = a.data[i+1]
	}
	a.data = a.data[:a.length-1]
	a.length--
}
