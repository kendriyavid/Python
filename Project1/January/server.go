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

package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	fmt.Println("started")
	ctx, cancleFunc := context.WithDeadline(context.Background(), time.Now().Add(10*time.Second))
	select {
	case <-ctx.Done():
		fmt.Println(<-ctx.Done())
		cancleFunc()
	}
}
