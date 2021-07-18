package app

import (
	"net/http"

	"github.com/gorilla/mux"
)

var httpMux = mux.NewRouter()

func (app Application) SetUp() {

}

func (app Application) Route(responseWriter http.ResponseWriter, request *http.Request) {
	apiRouter := httpMux.PathPrefix("/api-v1").Subrouter()
	apiRouter.Path("").HandlerFunc(app.Index).Methods(http.MethodGet)
	httpMux.ServeHTTP(responseWriter, request)
}
