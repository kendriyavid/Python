// package main

// import (
// 	"fmt"
// )

// func main() {

// 	// var name string = "harshdeepsingh"
// 	// var n2 string = name[:4]
// 	// var new string = n2 + name
// 	// fmt.Println(unsafe.StringData(name))
// 	// fmt.Println(unsafe.StringData(n2))
// 	// fmt.Println(unsafe.StringData(new))

// 	// var age uint8 = 88
// 	// var nage byte = 99
// 	// fmt.Println(age + nage)

// 	// var array []int = []int{1, 2, 3, 4, 5}
// 	// fmt.Println(array)

// 	// var slice []int = []int{}
// 	// fmt.Println((slice))

// }

// package main

// import (
// 	"log"
// 	"os"
// )

// func main() {

// 	file, err := os.Open("t")
// 	if err != nil {
// 		log.Println(err)
// 	}
// 	file.Write([]byte("hasrhdeepsingh"))
// 	file.Close()
// }

// channels

// package main

// import (
// 	"fmt"
// 	"time"
// )

// func c(ch chan int) {
// 	fmt.Println("starting")
// 	fmt.Println(<-ch)
// 	fmt.Println("ending")
// }

// func main() {
// 	ch := make(chan int)
// 	go c(ch)
// 	time.Sleep(4 * time.Second)
// 	ch <- 2
// 	fmt.Println("writtne")
// 	time.Sleep(2 * time.Second)
// }

// package main

// import "fmt"

// func goroutine(ch chan int, id int) {
// 	fmt.Println("starting", id)
// 	ch <- id
// 	fmt.Println("ending", id)
// }

// func main() {
// 	ch := make(chan int)
// 	for i := 0; i < 10; i++ {
// 		go goroutine(ch, i)
// 	}
// 	for i := 0; i < 10; i++ {
// 		fmt.Println(<-ch)
// 	}
// }

package main

import (
	"bytes"
	"fmt"
)

func main() {

	// file, err := os.OpenFile("testfile", os.O_RDONLY, 0644)
	// defer file.Close()
	// if err != nil {
	// 	panic(err)
	// }
	// // var name string = "harshdeepsingh will succeed"
	// // n, err := file.Write([]byte(name))
	// // if err != nil {
	// // 	panic(err)
	// // }
	// // fmt.Println(n)
	// var bs []byte = make([]byte, 5)
	// for {
	// 	_, err := file.Read(bs)
	// 	if err == io.EOF {
	// 		break
	// 	} else if err != nil {
	// 		panic(err)
	// 	}
	// 	fmt.Println(bs)
	// }

	buf := new(bytes.Buffer)
	buf.Write([]byte("harshdeep"))
	buf.Write([]byte("singh"))
	b := make([]byte, 2)
	fmt.Println(buf.Next(2))
	buf.Read(b)
	fmt.Println(string(b))
}
