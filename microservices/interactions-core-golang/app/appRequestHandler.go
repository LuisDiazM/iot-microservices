package app

import "net/http"

func (app Application) Index(responseWriter http.ResponseWriter, request *http.Request) {
	data := "buenos dias"
	responseWriter.Write([]byte(data))
}
