import {ActionReducerMap, MetaReducer} from '@ngrx/store'
import { DevicesReducerState, devicesReducer } from './devices/devices.reducer';


export interface AppState {
    devices: DevicesReducerState
}

export const reducers: ActionReducerMap<AppState> = {
    devices: devicesReducer
}