package hashtable

type HashTable struct {
	hash map[int]interface{}
}

func NewHashTable() *HashTable {
	return &HashTable{
		hash: make(map[int]interface{}),
	}
}

func (ht *HashTable) Add(key int, value interface{}) {
	ht.hash[key] = value
}

func (ht *HashTable) Get(key int) interface{} {
	return ht.hash[key]
}
