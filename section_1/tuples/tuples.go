package main

import (
	"fmt"
)

func main() {
	square, cube := powerSeries(5)

	fmt.Println("Square:", square, "Cube:", cube)

	square, cube = anotherWayPowerSeries(5)

	fmt.Println("Square:", square, "Cube:", cube)

	square, cube, err := anotherWayButWithErrorPowerSeries(5)

	fmt.Println("Square:", square, "Cube:", cube, "Error:", err)
}

func powerSeries(a int) (int, int) {
	return a * a, a * a * a
}

func anotherWayPowerSeries(a int) (square int, cube int) {
	square = a * a
	cube = square * a

	return
}

func anotherWayButWithErrorPowerSeries(a int) (int, int, error) {
	square := a * a
	cube := square * a

	return square, cube, nil
}
