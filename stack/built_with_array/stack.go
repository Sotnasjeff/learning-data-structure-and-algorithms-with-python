package builtwitharray

type Stack struct {
	Top []int
}

func(s *Stack) Push(value int) {
	s.Top = append(s.Top, value)
}

func(s *Stack) Pop(){
	s.Top = s.Top[:len(s.Top) - 1]
}

func(s *Stack) PrintLength() int {
	return len(s.Top)
}

func(s *Stack) PrintStack() []int {
	stack := []int{}
	stack = append(stack, s.Top...)
	return stack
}

func(s *Stack) PrintStackTop() int {
	if len(s.Top) == 0 {
		return 0
	}
	return s.Top[0]
}

func(s *Stack) PrintStackBottom() int {
	if len(s.Top) == 0 {
		return 0
	}
	return s.Top[len(s.Top) - 1]
}