package main

import (
	"fmt"
	"log"
	"net/http"
)

// mp:=make(map)

func handleRequest(res http.ResponseWriter, req *http.Request) {
	log.Println("got new reqeuest")
	defer req.Body.Close()
	req.ParseForm()
	fmt.Println(req.PostForm)
	fmt.Println(req.Form)
	values := req.PostForm
	fmt.Println(values["link"])
	res.Header().Set("Content-Type", "text/html")
	res.Header().Set("custom-Header", "memh")
	res.WriteHeader(200)
	res.Write([]byte("the new link is :"))
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/newlink/", handleRequest)
	err := http.ListenAndServe(":8080", mux)
	if err != nil {
		panic(err)
	}
}
