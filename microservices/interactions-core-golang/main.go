package main

import (
	"log"

	"github.com/LuisDiazM/iot-microservices/app"
)

func main() {

	log.Println("http server start ...")
	app := app.CreateApp()
	app.Start()
}
