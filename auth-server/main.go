package main

import (
	"fmt"
	"net/http"
)

func verifyCredential(w http.ResponseWriter, req *http.Request) {
	authToken := req.Header.Get("X-Auth-Token")

	if authToken == "xxx" {
		w.Header().Set("X-Auth-User", "admin")
		w.Header().Set("X-Secret", "xxx")
		w.WriteHeader(200)
	} else {
		w.WriteHeader(http.StatusUnauthorized)
	}
}

func checkHeaders(w http.ResponseWriter, req *http.Request) {
	username, password, ok := req.BasicAuth()
	fmt.Print(username)
	fmt.Print(password)
	fmt.Print(ok)
	// for name, headers := range req.Header {
	// 	for _, h := range headers {
	// 		fmt.Fprintf(w, "%v: %v\n", name, h)
	// 		fmt.Printf("%v: %v\n", name, h)
	// 	}
	// }
}

func main() {
	http.HandleFunc("/", verifyCredential)
	http.HandleFunc("/h", checkHeaders)
	http.ListenAndServe(":8090", nil)
}
