package app

import (
	"net/http"
	"sync"
)

type Application struct {
}

func NewApplication() *Application {
	return &Application{}
}

func (app Application) Start() {
	wg := new(sync.WaitGroup)
	wg.Add(2)

	go func() {
		http.HandleFunc("/", app.Route)
		http.ListenAndServe(":8080", nil)
		wg.Done()
	}()
	wg.Wait()
}
