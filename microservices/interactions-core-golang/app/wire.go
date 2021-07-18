package app

import "github.com/google/wire"

func CreateApp() *Application {
	wire.Build(
		AppProvider,
	)
	return new(Application)
}
