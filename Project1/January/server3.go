package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
	"time"
)

type response struct {
	OldLink   string    `json:"old_link"`
	NewLink   string    `json:"new_link"`
	Expire    time.Time `json:"expire"`
	CreatedAt time.Time `json:"created_at"`
}

type safeMap struct {
	mu sync.RWMutex
	mp map[string]string
}

func urlShortener(res http.ResponseWriter, req *http.Request) {
	log.Println("recieved at")
	defer req.Body.Close()
	req.ParseForm()
	oldURL := req.PostForm["link"][0]
	lch := make(chan string)
	go func() {
		fmt.Print("inside the function")
		time.Sleep(5 * time.Second) //simulating  the work
		safemp.mu.Lock()
		safemp.mp[oldURL] = "thiis is new URL"
		safemp.mu.Unlock()
		lch <- "this is new URL"
	}()
	fmt.Println("before the select")
	select {
	case newURL := <-lch:
		fmt.Println("inside the first case")
		fmt.Println(safemp.mp)
		fmt.Println(newURL)
		// res.WriteHeader(200)
		res.Header().Set("Content-Type", "application/json")
		res.Header().Add("Custom-Header", "Harshdeep'sProject")
		fmt.Println("here")
		v := response{
			OldLink:   oldURL,
			NewLink:   newURL,
			Expire:    time.Now().Add(24 * time.Hour),
			CreatedAt: time.Now(),
		}
		resbody, err := json.Marshal(v)
		fmt.Println(resbody)
		if err != nil {
			panic(err)
		}
		res.Write([]byte(resbody))
		fmt.Println("finished")
	case <-req.Context().Done():
		fmt.Println("cancelling")
		http.Error(res, "operation cancelled", http.StatusRequestTimeout)
	}

}

var safemp *safeMap = new(safeMap)

func main() {
	var baseMux *http.ServeMux = http.NewServeMux()
	baseMux.Handle("POST /shorten/", http.HandlerFunc(urlShortener))
	err := http.ListenAndServe(":8080", baseMux)
	if err != nil {
		panic(err)
	}
}
