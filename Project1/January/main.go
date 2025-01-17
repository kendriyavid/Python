// // package main

// // import (
// // 	"fmt"
// // 	"io"
// // 	"os"
// // )

// // func main() {
// // 	file, err := os.Open("test.txt")
// // 	if err != nil {
// // 		panic(err)
// // 	}
// // 	defer file.Close()

// // 	buffer := make([]byte, 10)
// // 	for {
// // 		n, err := file.Read(buffer)
// // 		if err != nil {
// // 			if err == io.EOF {
// // 				break
// // 			}
// // 			panic(err)
// // 		}
// // 		fmt.Print(string(buffer[:n])) // Print as a string instead of a byte slice
// // 	}
// // }

// package main

// import (
// 	"io"
// 	"os"
// )

// func main() {

// 	f1, err := os.OpenFile("test1.txt", os.O_WRONLY|os.O_CREATE, 0644)
// 	if err != nil {
// 		panic(err)
// 	}
// 	f2, err := os.OpenFile("test2.txt", os.O_WRONLY|os.O_CREATE, 0644)
// 	if err != nil {
// 		panic(err)
// 	}

// 	defer f1.Close()
// 	defer f2.Close()

// 	io.MultiWriter(f1, f2).Write([]byte("harshdeepsingh"))

// }

// package main

// import "fmt"

// type point struct{
// 	x int
// 	y int
// }

// type circle struct{
// 	radius int
// 	center *pointer
// }

// func main(){

// }

/// custom implementation of the io reader interface on the slices

// io reader interface

// type reader interface{
// 	func Read (p []bytes)(n int, err)
// }

package main

import (
	"fmt"
	"io"
)

type NewReader struct {
	p   []byte
	pos int
}

// Allocator function to create a new NewReader
func allocator(data []byte) (newReader *NewReader) {
	newReader = &NewReader{
		p:   data,
		pos: 0,
	}
	return
}

// Read method to implement io.Reader
func (r *NewReader) Read(p []byte) (n int, err error) {
	if r.pos >= len(r.p) {
		return 0, io.EOF // Nothing more to read
	}

	// Determine how many bytes to read
	n = copy(p, r.p[r.pos:])
	r.pos += n
	return n, nil
}

func main() {
	name := []byte("harshdeepsingh")
	fmt.Println("Input data:", string(name))

	// Create a new reader
	newReader := allocator(name)

	// Buffer to read into
	buffer := make([]byte, 5) // Adjust buffer size as needed

	for {
		n, err := newReader.Read(buffer)
		if err == io.EOF {
			break
		}
		fmt.Printf("Read %d bytes: %s\n", n, string(buffer[:n]))
	}
}
