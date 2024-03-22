package main

import "fmt"

//Logic:
//IComposite is an interface implemented by Leaflet and Branch
//Branch is the main class which they use Leaflet struct to compose itself and itself too.
//So we can compose each branch with many branches and leafs together binded by a struct branch
//Example drawn

//Leaf1   Leaf2        Leaf3   Leaf4          Leaf5
// \       /             \       /            /
//  \     /               \     /            /
//   \   /                 Branch1      Branch2
//    \ /                  /              /
//	   /                  /              /
//   Branch --------------   ------------

type IComposite interface {
	perform()
}

type Leaflet struct {
	name string
}

func (lf *Leaflet) perform() {
	fmt.Println("Leaflet " + lf.name)
}

type Branch struct {
	leafs    []Leaflet
	name     string
	branches []Branch
}

func (b *Branch) perform() {
	fmt.Println("Branch: " + b.name)
	for _, leaf := range b.leafs {
		leaf.perform()
	}

	for _, branch := range b.branches {
		branch.perform()
	}
}

func (b *Branch) addBranch(newBranch Branch) {
	b.branches = append(b.branches, newBranch)
}

func (b *Branch) addLeaf(newLeaf Leaflet) {
	b.leafs = append(b.leafs, newLeaf)
}

func (b *Branch) getLeafLets() []Leaflet {
	return b.leafs
}

func main() {
	var branch = &Branch{name: "branch 1"}
	var leaf1 = Leaflet{name: "leaf 1"}
	var leaf2 = Leaflet{name: "leaf 2"}
	var branch2 = Branch{name: "branch 2"}
	branch.addLeaf(leaf1)
	branch.addLeaf(leaf2)
	branch.addBranch(branch2)
	branch2.addLeaf(leaf1)
	branch.perform()
	fmt.Println(branch.getLeafLets())
	fmt.Println(branch2.getLeafLets())

}
