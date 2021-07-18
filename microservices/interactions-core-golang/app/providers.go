package app

import "github.com/google/wire"

var AppProvider = wire.NewSet(NewApplication)
