package main

import (
	"fmt"
)

//Logic:
//DrawShape implements IDrawShape and its method
//DrawContour implements IDrawContour and its method, in addition to it, DrawContour composes its struct with DrawShape struct
//so DrawShape becomes a bridge to DrawContour to use drawShape method
//                                                IDrawContour(drawContour(), resizeByFactor())
//															|
//															v
//IDrawShape(drawShape()) -> DrawShape(drawShape()) -> DrawContour(drawContour(->DrawShape.drawShape()), resizeByFactor(), DrawShape)

type IDrawShape interface {
	drawShape(x [5]float32, y [5]float32)
}

type DrawShape struct {
}

func (ds DrawShape) drawShape(x [5]float32, y [5]float32) {
	fmt.Println("Drawing Shape")
}

type IContour interface {
	drawContour(x [5]float32, y [5]float32)
	resizeByFactor(factor int)
}

type DrawContour struct {
	x      [5]float32
	y      [5]float32
	shape  DrawShape
	factor int
}

func (dc DrawContour) drawContour(x [5]float32, y [5]float32) {
	fmt.Println("Drawing Contour")
	dc.shape.drawShape(x, y)
}

func (dc DrawContour) resizeByFactor(factor int) {
	dc.factor = factor
}

func main() {
	var x = [5]float32{1, 2, 6, 8, 4}
	var y = [5]float32{5, 2, 6, 4, 8}
	var contour IContour = DrawContour{x, y, DrawShape{}, 2}
	contour.drawContour(x, y)
	contour.resizeByFactor(2)
}
