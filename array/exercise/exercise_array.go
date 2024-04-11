package main

import "fmt"

func main() {
	fmt.Println(reverse("Hello World"))

	first := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	second := []int{4, 4, 6, 22}

	fmt.Println(mergeSortedArray(first, second))
}

// Exercise 1 - reverse string
func reverse(str string) string {
	runeConverted := []rune(str)
	var result []rune

	for i := len(runeConverted) - 1; i >= 0; i-- {
		result = append(result, runeConverted[i])
	}

	return string(result)
}

// Exercise 2 - merge sorted array
func mergeSortedArray(first, second []int) []int {
	result := make([]int, 0)

	i := 0
	j := 0

	for i < len(first) && j < len(second) {
		if first[i] < second[j] {
			result = append(result, first[i])
			i++
		} else {
			result = append(result, second[j])
			j++
		}
	}

	for i < len(first) {
		result = append(result, first[i])
		i++
	}

	for j < len(second) {
		result = append(result, second[j])
		j++
	}

	return result
}
