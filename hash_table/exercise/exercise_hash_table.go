package main

import "fmt"

func main() {
	test1 := []int{2, 5, 1, 2, 3, 5, 1, 2, 4}
	test2 := []int{2, 1, 1, 2, 3, 5, 1, 2, 4}
	test3 := []int{2, 3, 4, 5}
	fmt.Println(firstRecurringCharacter(test1))
	fmt.Println(firstRecurringCharacter(test2))
	fmt.Println(firstRecurringCharacter(test3))
}

func firstRecurringCharacter(value []int) int {
	aux := make(map[int]bool)

	for _, v := range value {
		if aux[v] {
			return v
		}
		aux[v] = true
	}

	return 0
}
