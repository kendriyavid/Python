// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"net"
// )

// func handle(conn net.Conn) {
// 	newScanner := bufio.NewScanner(conn)
// 	for newScanner.Scan() {
// 		line := newScanner.Text()
// 		fmt.Println(line)
// 	}
// 	defer conn.Close()
// 	_, err := conn.Write([]byte("harshdeepsingh"))
// 	if err != nil {
// 		panic(err)
// 	}

// }

// func main() {

// 	li, err := net.Listen("tcp", ":8080")
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer li.Close()
// 	for {
// 		conn, err := li.Accept()
// 		if err != nil {
// 			panic(err)
// 		}
// 		go handle(conn)
// 	}
// }

// package main

// import "fmt"

// func main() {
// 	var bs []byte = []byte("harshdeep")
// 	fmt.Println(bs)
// 	fmt.Print(string(fmt.Appendln(bs, "singh")))
// }

// package main

// import (
// 	"fmt"
// 	"io"
// 	"strings"
// )

// func main() {
// 	var name string
// 	var age int
// 	var added string = "harshdeepsingh 22"
// 	var reader io.Reader = strings.NewReader(added)
// 	fmt.Fscan(reader, &name, &age)
// 	fmt.Printf("%[2]T \n", name, age)
// 	fmt.Printf(name, age)

// }

// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"io"
// 	"strings"
// )

// func main() {

// 	var name string = "harshdeepsinghab"
// 	var r io.Reader = strings.NewReader(name)
// 	bfr := *bufio.NewReader(r)
// 	p := make([]byte, 10)
// 	_, err := bfr.Read(p)
// 	if err != nil {
// 		fmt.Println(err)
// 	}
// 	fmt.Println(bfr.Buffered())
// 	fmt.Println(string(p))
// }

// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"strings"
// )

// func main() {
// 	str := "ffff\n de\n d\n dd\n"
// 	r := strings.NewReader(str)
// 	scr := bufio.NewScanner(r)
// 	buf := make([]byte, 5)
// 	scr.Buffer(buf, 1)
// 	for scr.Scan() {
// 		fmt.Println(scr.Text())
// 	}
// 	fmt.Println("ended")
// }

// package main

// import (
// 	"context"
// 	"fmt"
// 	"time"
// )

// func main() {
// 	fmt.Println("started")
// 	ctx, cancleFunc := context.WithDeadline(context.Background(), time.Now().Add(10*time.Second))
// 	ctx2, cancleFunc := context.WithDeadline(context.Background(), time.Now().Add(5*time.Second))
// 	select {
// 	case <-ctx.Done():
// 		fmt.Println(<-ctx.Done())
// 		fmt.Println("first")
// 		cancleFunc()
// 	case <-ctx2.Done():
// 		fmt.Println("second")
// 		// default:
// 		// 	fmt.Println("default")
// 	}
// 	fmt.Println("exiting")
// }

// package main

// import (
// 	"context"
// 	"fmt"
// 	"time"
// )

// func main() {
// 	fmt.Println("started")
// 	ch := make(chan int)
// 	close(ch)
// 	ctx, _ := context.WithDeadline(context.Background(), time.Now().Add(2*time.Second))

// 	select {
// 	case <-ch:
// 		fmt.Println("inside the ch case")
// 	case <-ctx.Done():
// 		fmt.Println("inside the done channel")
// 	default:
// 		fmt.Println("none of the above")
// 	}

// }

// data race solutions

// package main

// import "fmt"

// func main() {
// 	fmt.Println("started")
// 	var count int = 0
// 	ch := make(chan int)

// 	for i := 0; i < 1000; i++ {
// 		go func(ch chan int) {
// 			ch <- 1
// 		}(ch)
// 	}

// 	for i := 0; i < 1000; i++ {
// 		count += <-ch
// 	}

// 	fmt.Println(count)
// }

// package main

// import (
// 	"fmt"
// 	"sync"
// )

// func main() {
// 	var wg sync.WaitGroup
// 	var counter int = 0
// 	sem := make(chan bool, 1)
// 	for i := 0; i < 1000; i++ {
// 		wg.Add(1)
// 		go func() {
// 			sem <- true
// 			counter++
// 			<-sem
// 			wg.Done()
// 		}()
// 	}
// 	wg.Wait()

// 	fmt.Println(counter)
// }

// mutex

// package main

// import (
// 	"fmt"
// 	"sync"
// )

// func main() {

// 	var counter int = 0
// 	var m sync.Mutex
// 	var wg sync.WaitGroup
// 	for i := 0; i < 1000; i++ {
// 		wg.Add(1)
// 		go func() {
// 			m.Lock()
// 			counter++
// 			m.Unlock()
// 			wg.Done()
// 		}()
// 	}
// 	wg.Wait()
// 	fmt.Println(counter)
// }

// package main

// import (
// 	"fmt"
// 	"net/http"
// )

// type foo int

// func (f *foo) ServeHTTP(res http.ResponseWriter, req *http.Request) {
// 	fmt.Println(req.Body)
// 	res.Header().Add("content-type", "text/plain")
// 	fmt.Println(res.Header())
// 	res.Write([]byte("<p>hi there<p>"))
// }

// func main() {
// 	f := new(foo)
// 	err := http.ListenAndServe(":8080", f)
// 	if err != nil {
// 		panic(err)
// 	}
// 	fmt.Println("server started")
// }

// basic applicatiton with docker
// url shortening service with redis and docker
// reverse proxy
// splitwise application with

// package main

// import (
// 	"io"
// 	"log"
// 	"net/http"
// 	"time"
// )

// type foo int

// func (f *foo) ServeHTTP(res http.ResponseWriter, req *http.Request) {
// 	// Safely read and close request body

// 	select{
// 	case <-req.Context().Done():
// 		return
// 	default:
// 		time.Sleep(10*time.Second)  // simulaTING BIG SEARCH
// 		defer req.Body.Close()
// 		body, _ := io.ReadAll(req.Body)

// 		// Log request details (safer than fmt.Println)
// 		log.Printf("Headers: %v", req.Header)
// 		log.Printf("Body: %s", body)

// 		// Correct MIME type
// 		res.Header().Add("Content-Type", "text/plain")
// 		res.WriteHeader(http.StatusOK)

// 		// Write response with error handling
// 		_, err := res.Write([]byte("This is harshdeepsingh"))
// 		if err != nil {
// 			log.Printf("Error writing response: %v", err)
// 		}
// 	}

// }

// func main() {
// 	f := new(foo)
// 	log.Println("Server starting on :8080")
// 	log.Fatal(http.ListenAndServe(":8080", f))
// }

// package main

// import (
// 	"context"
// 	"fmt"
// 	"log"
// 	"net/http"
// 	"time"
// )

// type foo int

// func (f *foo) ServeHTTP(res http.ResponseWriter, req *http.Request) {
// 	ctx, cancel := context.WithTimeout(req.Context(), 5*time.Second)
// 	defer cancel()

// 	resultChan := make(chan []byte, 1)

// 	go func() {
// 		time.Sleep(3 * time.Second)
// 		resultChan <- []byte("Search result for harshdeepsingh")
// 	}()

// 	select {
// 	case <-ctx.Done():
// 		// Context cancelled (timeout or client disconnection)
// 		fmt.Println("search cancelled")
// 		http.Error(res, "Search cancelled", http.StatusRequestTimeout)
// 		return
// 	case result := <-resultChan:
// 		// Successful result
// 		res.Header().Set("Content-Type", "text/plain")
// 		res.WriteHeader(http.StatusOK)
// 		res.Write(result)
// 	}
// }

// func main() {
// 	f := new(foo)
// 	log.Println("Server starting on :8080")
// 	log.Fatal(http.ListenAndServe(":8080", f))
// }

// package main

// import (
// 	"fmt"
// 	"net/http"
// )

// type foo int

// func (f *foo) ServeHTTP(res http.ResponseWriter, req *http.Request) {
// 	defer req.Body.Close()
// 	req.ParseForm()
// 	// fmt.Println(req.Body)
// 	value := req.Form["id"]
// 	fmt.Println(req.Form)
// 	res.WriteHeader(200)
// 	res.Header().Add("Content-Type", "text/html")
// 	res.Write([]byte(fmt.Sprintf("value was: %s", value)))
// }

// func main() {
// 	f := new(foo)
// 	err := http.ListenAndServe(":8080", f)
// 	if err != nil {
// 		panic(err)
// 	}
// }

package main

import (
	"crypto/sha256"
	"fmt"
)

func main() {
	// Original string
	input := "Hello, World!"

	// Generate hash
	hash := sha256.Sum256([]byte(input))

	// Different ways to view the hash
	fmt.Printf("Raw hash (byte array): %v\n", hash)
	fmt.Printf("Hash as bytes: %x\n", hash) // Hexadecimal representation
	fmt.Printf("Hash length: %d bytes\n", len(hash))
	fmt.Println(string(hash))
}
