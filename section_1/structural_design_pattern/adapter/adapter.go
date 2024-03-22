package main

import "fmt"

//Logic:
// Adapter implements IProcessor which they have an Adaptee instance inside in their struct
// Adapter implements the contract from IProcessor and they use the instance of adaptee to convert
// IProcessor(process()) -> Adapter(process(-> adaptee.convert())) -> Adaptee(convert())

type IProcessor interface {
	process()
}

type Adaptee struct {
	adapterType int
}

func (adpt Adaptee) convert() {
	fmt.Println("Adaptee convert method")
}

type Adapter struct {
	adaptee Adaptee
}

func (ad Adapter) process() {
	fmt.Println("Adapter process")
	ad.adaptee.convert()
}

func main() {
	var processor IProcessor = Adapter{}
	processor.process()
}
