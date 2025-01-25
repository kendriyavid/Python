package main

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"log"
	"net/http"
	"sync"
	"time"
)

type URLShortener struct {
	mu      sync.RWMutex
	storage map[string]string
}

func NewURLShortener() *URLShortener {
	return &URLShortener{
		storage: make(map[string]string),
	}
}

func (us *URLShortener) GenerateShortURL(originalURL string) string {
	// Generate a unique short URL using SHA-256 hash
	hash := sha256.Sum256([]byte(originalURL + time.Now().String()))
	shortCode := base64.URLEncoding.EncodeToString(hash[:6])

	us.mu.Lock()
	defer us.mu.Unlock()
	us.storage[shortCode] = originalURL

	return shortCode
}

type response struct {
	OldLink   string    `json:"old_link"`
	NewLink   string    `json:"new_link"`
	Expire    time.Time `json:"expire"`
	CreatedAt time.Time `json:"created_at"`
}

func (us *URLShortener) HandleShorten(res http.ResponseWriter, req *http.Request) {
	if req.Method != http.MethodPost {
		http.Error(res, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	if err := req.ParseForm(); err != nil {
		http.Error(res, "Invalid form data", http.StatusBadRequest)
		return
	}

	oldURL := req.PostForm.Get("link")
	if oldURL == "" {
		http.Error(res, "Missing URL", http.StatusBadRequest)
		return
	}

	// Simulate some processing time
	time.Sleep(500 * time.Millisecond)

	shortURL := us.GenerateShortURL(oldURL)

	resp := response{
		OldLink:   oldURL,
		NewLink:   shortURL,
		Expire:    time.Now().Add(24 * time.Hour),
		CreatedAt: time.Now(),
	}

	res.Header().Set("Content-Type", "application/json")
	res.WriteHeader(http.StatusOK)
	json.NewEncoder(res).Encode(resp)
}

func main() {
	shortener := NewURLShortener()
	mux := http.NewServeMux()
	mux.HandleFunc("POST /shorten/", shortener.HandleShorten)

	log.Println("Starting server on :8080")
	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Fatal(err)
	}
}
