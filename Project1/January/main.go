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

// package main

// import (
// 	"fmt"
// 	"io"
// )
// type NewReader struct {
// 	p   []byte
// 	pos int
// }
// func allocator(data []byte) (newReader *NewReader) {
// 	newReader = &NewReader{
// 		p:   data,
// 		pos: 0,
// 	}
// 	return
// }
// func (r *NewReader) Read(p []byte) (n int, err error) {
// 	if r.pos >= len(r.p) {
// 		return 0, io.EOF
// 	}

// 	n = copy(p, r.p[r.pos:])
// 	r.pos += n
// 	return n, nil
// }
// func main() {
// 	name := []byte("harshdeepsingh")
// 	fmt.Println("Input data:", string(name))

// 	newReader := allocator(name)

// 	// Buffer to read into
// 	buffer := make([]byte, 5)
// 	for {
// 		n, err := newReader.Read(buffer)
// 		if err == io.EOF {
// 			break
// 		}
// 		fmt.Printf("Read %d bytes: %s\n", n, string(buffer[:n]))
// 	}
// }

// Concurrency in The Golang Patterns and all the things

// package main

// import "fmt"

// func hello(channel chan int) {

// 	fmt.Println("hello there")
// 	channel <- 10
// }

// func main() {
// 	fmt.Println("started")
// 	channel := make(chan int)
// 	go hello(channel)
// 	// value := <-channel
// 	// fmt.Println(value)A
// 	fmt.Println("ended")
// }

// package main

// import "fmt"

// func hell(channel chan int) {
// 	for i := 0; i < 10; i++ {
// 		channel <- i
// 	}
// 	close(channel)
// }

// func main() {
// 	channel := make(chan int)
// 	gohell(channel)
// 	for x := range channel {
// 		fmt.Println(x)
// 	}
// }

// package main

// import "fmt"

// func main() {
// 	// Create a buffered channel with a capacity of 3
// 	channel := make(chan string, 3)

// 	// Send 3 items, buffer will become full
// 	channel <- "harshdeepsingh"

// 	fmt.Println("Sent harsh")

// 	// Now the buffer is full, and this line will block until space is freed up
// 	channel <- "s" // This will block the execution here

// 	fmt.Println("Sent s") // This will never be printed unless a receiver reads from the channel
// }

// package main

// import "fmt"

// func hello(channel chan int) {
// 	fmt.Println("hi there")
// 	fmt.Println("inside the hello: ", <-channel)
// 	// channel <- 0
// }

// func main() {
// 	channel := make(chan int)
// 	// go hello(channel)
// 	channel <- 11
// 	channel <- 12
// 	fmt.Println(<-channel)
// 	fmt.Println("ending")
// }

// package main

// import (
// 	"fmt"
// 	"time"
// )

// func sender(channel chan int) {
// 	fmt.Println("Sending 10...")
// 	channel <- 10 // Will block here if there's no receiver
// 	fmt.Println("Sent 10!")
// }

// func receiver(channel chan int) {
// 	time.Sleep(2 * time.Second) // Simulate delay
// 	fmt.Println("Receiving value...")
// 	value := <-channel // Will block here if there's no sender
// 	fmt.Println("Received:", value)
// }

// func main() {
// 	channel := make(chan int)

// 	go sender(channel)
// 	go receiver(channel)

// 	// This part of the code is not dependent on the channel operations
// 	fmt.Println("Main function doing other work...")
// 	time.Sleep(5 * time.Second) // Wait for goroutines to complete
// 	fmt.Println("Main function ending")
// }

// package main

// import (
// 	"fmt"
// 	"sync"
// )

// func hello(i int, g *sync.WaitGroup) {
// 	fmt.Println("hi there ", i)
// 	fmt.Println("ending ", i)
// 	g.Done()
// }

// func main() {
// 	var g sync.WaitGroup
// 	for i := 0; i < 10; i++ {
// 		go hello(i, &g)
// 		g.Add(1)
// 	}
// 	g.Wait()
// 	fmt.Println("ending the program")
// }

// package main

// import "fmt"

// func main(){

// }