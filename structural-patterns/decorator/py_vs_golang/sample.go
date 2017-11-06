package main

import (
  "fmt"
  "net/http"
)

//函数的入口
var hi_handler = authRequired (
  func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "hi, %v", r.FormValue("user"))
  },
)

//函数的装饰器
func authRequired(f http.HandlerFunc) http.HandlerFunc {
  return func(w http.ResponseWriter, r *http.Request) {
    if r.FormValue("user") == "" {
      http.Error(w, "unknow user", http.StatusForbidden)
      return
    } else {
      fmt.Fprintf(w, "先经过装饰器<br>")
    }
    f(w, r)
  }
}

func main() {
  http.HandleFunc("/hi", hi_handler)
  http.ListenAndServe(":8999", nil)
}



