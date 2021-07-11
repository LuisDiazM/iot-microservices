import { Action, createReducer, on } from '@ngrx/store';
import * as actions from './devices.actions';
import { DevicesRegistrys } from '../../commons/models/registrys.model';

export interface DevicesReducerState {
  listRegistrys: DevicesRegistrys[];
}

export const initialState: DevicesReducerState = {
  listRegistrys: [],
};

export const _devicesReducer = createReducer(
  initialState,
  on(actions.devicesAction, (state, { registrys }) => {
    return {
      ...state,
      listRegistrys: [...registrys],
    };
  })
);

export function devicesReducer(
  state: DevicesReducerState | undefined,
  action: Action
) {
  return _devicesReducer(state, action);
}
