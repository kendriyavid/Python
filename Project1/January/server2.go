package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"time"
)

func readConn(ctx context.Context, cancleFunc context.CancelFunc, conn net.Conn) {
	scr := bufio.NewScanner(conn)
	for scr.Scan() {
		_, err := fmt.Fprintln(os.Stdout, scr.Text())
		if err != nil {
			log.Println("Error writing to stdout:", err)
			cancleFunc()
			return
		}
	}
	if err := scr.Err(); err != nil {
		if err == io.EOF {
			log.Println("client closed the connection gracefully")
		} else {
			log.Println("Error reading from connection:", err)
		}
		cancleFunc()
	}
}

func writeConn(ctx context.Context, cancleFunc context.CancelFunc, conn net.Conn) {
	writer := bufio.NewWriter(conn)
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		_, err := writer.WriteString(scanner.Text() + "\n")
		if err != nil {
			log.Println("Error writing to connection:", err)
			cancleFunc()
			return
		}

		if err := writer.Flush(); err != nil {
			log.Println("Error flushing writer:", err)
			cancleFunc()
			return
		}
	}
}

func handle(ctx context.Context, conn net.Conn) {
	defer conn.Close()
	ctx, cancleFunc := context.WithDeadline(ctx, time.Now().Add(1*time.Minute))
	defer cancleFunc()
	go readConn(ctx, cancleFunc, conn)
	go writeConn(ctx, cancleFunc, conn)
	<-ctx.Done()
}

func main() {
	var ctx context.Context = context.Background()
	li, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("Error listening:", err)
	}
	defer li.Close()

	log.Println("Server listening on :8080")

	for {
		conn, err := li.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err)
			continue
		}
		go handle(ctx, conn)
	}
}

// number of concurrent connections
// atomic values

// unique id
// map with uuid
// attach uuid with context
// do the getter and setter of the uuid closure type to protect the data

// map with adding and removing

// specifically sending to a client
// broadcast all and single and group

// encryption
// asymettric encryption aes
