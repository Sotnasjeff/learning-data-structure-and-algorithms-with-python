package main

import "fmt"

func main() {
	fmt.Println(reverse("Hello World"))
}

func reverse(str string) string {
	runeConverted := []rune(str)
	var result []rune

	for i := len(runeConverted) - 1; i >= 0; i-- {
		result = append(result, runeConverted[i])
	}

	return string(result)
}
