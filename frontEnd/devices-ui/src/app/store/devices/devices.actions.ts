import { createAction, props } from '@ngrx/store';
import { DevicesRegistrys } from '../../commons/models/registrys.model';

export const devicesAction = createAction(
  '[Devices] Add List Registrys',
  props<{ registrys: DevicesRegistrys[] }>()
);
