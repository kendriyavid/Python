package main

import (
	"bufio"
	"fmt"
	"net"
)

func handle(conn net.Conn) {
	newScanner := bufio.NewScanner(conn)
	for newScanner.Scan() {
		line := newScanner.Text()
		fmt.Println(line)
	}
	defer conn.Close()
	_, err := conn.Write([]byte("harshdeepsingh"))
	if err != nil {
		panic(err)
	}

}

func main() {

	li, err := net.Listen("tcp", ":8080")
	if err != nil {
		panic(err)
	}
	defer li.Close()
	for {
		conn, err := li.Accept()
		if err != nil {
			panic(err)
		}
		go handle(conn)
	}
}
