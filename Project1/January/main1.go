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

package main

import (
	"log"
	"time"
)

func helloResponse(channel chan int, id int) {
	time.Sleep(time.Duration(id) * time.Second)
	channel <- id
}

func main() {
	var channelArray = []chan int{make(chan int), make(chan int)}
	for id, channel := range channelArray {
		go helloResponse(channel, id+1)
	}

	for {
		select {
		case <-channelArray[0]:
			log.Println("reciving from: ", <-channelArray[0])

		case <-channelArray[1]:
			log.Println("recieving from ", <-channelArray[1])
		}
	}
}
