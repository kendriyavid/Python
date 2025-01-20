// package main

// import "fmt"

// func hello(channel chan int) {
// 	fmt.Println("inside the function")
// 	// fmt.Println(<-channel)
// 	// channel <- 0
// }

// func main() {
// 	var channel chan int = make(chan int)
// 	go hello(channel)
// 	// channel <- 2
// 	fmt.Println(<-channel)
// }

// package main

// import (
// 	"fmt"
// 	"log"
// 	"time"
// )

// func sendHello(id int, channel chan int) {
// 	fmt.Println("startingGO: ", id)
// 	channel <- id
// 	fmt.Println("endingGO: ", id)
// }

// func main() {
// 	channel := make(chan int)
// 	for i := 0; i < 5; i++ {
// 		go sendHello(i, channel)
// 	}
// 	for i := 0; i < 5; i++ {
// 		time.Sleep(5 * time.Second)
// 		log.Println("recieving: ", <-channel)
// 		log.Println("ending")

// 	}
// }

// package main

// import (
// 	"log"
// 	"time"
// )

// func helloResponse(channel chan int, id int) {
// 	time.Sleep(time.Duration(id) * time.Second)
// 	channel <- id
// }

// func main() {
// 	var channelArray = []chan int{make(chan int), make(chan int)}
// 	for id, channel := range channelArray {
// 		go helloResponse(channel, id+1)
// 	}

// 	for {
// 		select {
// 		case <-channelArray[0]:
// 			log.Println("reciving from: ", <-channelArray[0])

// 		case <-channelArray[1]:
// 			log.Println("recieving from ", <-channelArray[1])
// 		}
// 	}
// }

// package main

// import (
// 	"fmt"
// 	"time"
// )

// func helloThere(ch chan int) {
// 	fmt.Println("Inside Hello")
// 	ch <- 22
// 	fmt.Println("ending the hellother function")
// }

// func main() {
// 	fmt.Println("starting the main")
// 	ch := make(chan int)
// 	go helloThere(ch)
// 	time.Sleep(5 * time.Second)
// 	fmt.Println("recieveing: ", <-ch)
// 	fmt.Println("finishing the main")
// }

// package main

// import (
// 	"fmt"
// 	"time"
// )

// func hello(ch chan int) {
// 	fmt.Println("starting the func")
// 	ch <- 10
// 	ch <- 10
// 	ch <- 10
// 	fmt.Println("ending func")
// }

// func main() {
// 	fmt.Println("starting the main")
// 	ch := make(chan int, 3)
// 	go hello(ch)
// 	time.Sleep(3 * time.Second)
// 	fmt.Println(<-ch)
// 	fmt.Println(<-ch)
// 	fmt.Println(<-ch)

// 	fmt.Println("ending the main")
// }

// multiple channels select waitgroup

// package main

// import "fmt"

// func hello(id int, channel chan int) {
// 	fmt.Println("starting: ", id)
// 	channel <- id

// }

// func main() {
// 	var arr [2]chan int = [2]chan int{make(chan int), make(chan int)}
// 	ending := make(chan int)
// 	for i := 0; i < 10; i++ {
// 		go hello(i, arr[i%2])
// 	}
// 	ending <- 0
// 	for {
// 		select {
// 		case <-arr[0]:
// 			fmt.Println("recieving from: ", <-arr[0])
// 		case <-arr[1]:
// 			fmt.Println("recieving from: ", <-arr[1])
// 		case <-ending:
// 			break
// 		}
// 	}
// }

// package main

// import (
// 	"fmt"
// )

// func hello(id int, channel chan int) {
// 	fmt.Println("starting:", id)
// 	channel <- id
// }

// func main() {
// 	// Create an array of 2 channels
// 	var arr [2]chan int = [2]chan int{make(chan int), make(chan int)}
// 	ending := make(chan bool)

// 	// Launch 10 goroutines
// 	for i := 0; i < 10; i++ {
// 		go hello(i, arr[i%2]) // Alternate between arr[0] and arr[1]
// 	}

// 	go func() {
// 		// Signal completion after a delay
// 		ending <- true
// 	}()

// 	// Loop to receive values from channels
// 	for {
// 		select {
// 		case val := <-arr[0]:
// 			fmt.Println("receiving from arr[0]:", val)
// 		case val := <-arr[1]:
// 			fmt.Println("receiving from arr[1]:", val)
// 		case <-ending:
// 			fmt.Println("Exiting loop.")
// 			return // Exit the loop
// 		}
// 	}
// }

package main

import (
	"fmt"
	"sync"
)

func hello(id int, channel chan int, wg *sync.WaitGroup) {
	defer wg.Done() // Decrement the counter when the goroutine completes
	fmt.Println("starting:", id)
	channel <- id
}

func main() {
	// Create an array of 2 channels
	var arr [2]chan int = [2]chan int{make(chan int), make(chan int)}
	done := make(chan bool)
	var wg sync.WaitGroup

	// Launch 10 goroutines
	for i := 0; i < 10; i++ {
		wg.Add(1) // Increment the counter for each goroutine
		go hello(i, arr[i%2], &wg)
	}

	// Close the channels after all goroutines finish
	go func() {
		wg.Wait() // Wait for all goroutines to complete
		close(arr[0])
		close(arr[1])
		done <- true // Signal the main loop to exit
	}()

	// Loop to receive values from channels
	for {
		select {
		case val, ok := <-arr[0]:
			if ok {
				fmt.Println("receiving from arr[0]:", val)
			}
		case val, ok := <-arr[1]:
			if ok {
				fmt.Println("receiving from arr[1]:", val)
			}
		case <-done:
			fmt.Println("Exiting loop.")
			return // Exit the loop
		}
	}
}
