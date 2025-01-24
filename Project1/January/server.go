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
