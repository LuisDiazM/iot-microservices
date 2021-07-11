import { Injectable } from '@angular/core';
import { Store } from '@ngrx/store';
import { DevicesRegistrys } from '../commons/models/registrys.model';
import * as actions from '../store/devices/devices.actions';

@Injectable()
export class DevicesFacade {
  constructor(private store: Store) {}

  loadRegistrys(registrys: DevicesRegistrys[]) {
    this.store.dispatch(actions.devicesAction({ registrys }));
  }
}
