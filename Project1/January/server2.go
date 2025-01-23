package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"sync"
	"time"
)

func readConn(ctx context.Context, cancelFunc context.CancelFunc, conn net.Conn) {
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		select {
		case <-ctx.Done():
			return
		default:
			_, err := fmt.Fprintln(os.Stdout, scanner.Text())
			if err != nil {
				log.Println("Error writing to stdout:", err)
				cancelFunc()
				return
			}
		}
	}
	if err := scanner.Err(); err != nil && err != io.EOF {
		log.Println("Error reading from connection:", err)
		cancelFunc()
	}
}

func writeConn(ctx context.Context, cancelFunc context.CancelFunc, conn net.Conn) {
	writer := bufio.NewWriter(conn)
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		select {
		case <-ctx.Done():
			return
		default:
			_, err := writer.WriteString(scanner.Text() + "\n")
			if err != nil {
				log.Println("Error writing to connection:", err)
				cancelFunc()
				return
			}
			if err := writer.Flush(); err != nil {
				log.Println("Error flushing writer:", err)
				cancelFunc()
				return
			}
		}
	}
}

func handle(wg *sync.WaitGroup, semaphore chan bool, ctx context.Context, conn net.Conn) {
	defer func() {
		conn.Close()
		<-semaphore
		wg.Done()
	}()
	ctx, cancelFunc := context.WithDeadline(ctx, time.Now().Add(1*time.Minute))
	defer cancelFunc()

	go readConn(ctx, cancelFunc, conn)
	go writeConn(ctx, cancelFunc, conn)

	<-ctx.Done()
}

func main() {
	var wg sync.WaitGroup
	semaphore := make(chan bool, 10)
	ctx := context.Background()

	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("Error listening:", err)
	}
	defer listener.Close()

	log.Println("Server listening on :8080")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Println("Error accepting connection:", err)
			continue
		}

		wg.Add(1)
		semaphore <- true
		go handle(&wg, semaphore, ctx, conn)
	}

}
