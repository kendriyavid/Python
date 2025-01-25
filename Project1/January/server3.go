package main

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
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

func readURL(res http.ResponseWriter, req *http.Request) {
	fmt.Println("redirecting")
	defer req.Body.Close()
	key, _ := strings.CutPrefix(req.URL.Path, "/")
	safemp.mu.RLock()
	target, ok := safemp.mp[key]
	safemp.mu.RUnlock()
	fmt.Println(target)
	if !ok {
		http.NotFoundHandler()
	}
	http.Redirect(res, req, target, http.StatusMovedPermanently)
}

func urlShortener(res http.ResponseWriter, req *http.Request) {
	defer req.Body.Close()
	req.ParseForm()
	oldURL := req.PostFormValue("link")
	if oldURL == "" {
		http.Error(res, "no url provided", http.StatusBadRequest)
	}
	lch := make(chan string)
	go func() {
		hash := sha256.Sum256([]byte(oldURL + time.Now().String()))
		shortCode := base64.URLEncoding.EncodeToString(hash[:6])
		safemp.mu.Lock()
		safemp.mp[shortCode] = oldURL
		safemp.mu.Unlock()
		lch <- shortCode
	}()
	select {
	case newURL := <-lch:
		fmt.Println(safemp.mp)
		fmt.Println(newURL)
		res.Header().Set("Content-Type", "application/json")
		res.Header().Add("Custom-Header", "Harshdeep'sProject")
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

var safemp safeMap = safeMap{
	mu: sync.RWMutex{},
	mp: make(map[string]string),
}

func main() {
	var baseMux *http.ServeMux = http.NewServeMux()
	baseMux.Handle("POST /shorten/", http.HandlerFunc(urlShortener))
	baseMux.Handle("GET /", http.HandlerFunc(readURL))
	err := http.ListenAndServe(":8080", baseMux)
	if err != nil {
		panic(err)
	}
}
