import { Component, OnInit } from '@angular/core';
import { DevicesRegistrys } from 'src/app/commons/models/registrys.model';
import { DevicesService } from '../../services/devices.service';
import { State } from '../../commons/models/registrys.model';
import { interval } from 'rxjs';
import { DevicesFacade } from '../../facades/devices.facade';

@Component({
  selector: 'app-list-devices-registrys',
  templateUrl: './list-devices-registrys.component.html',
  styleUrls: ['./list-devices-registrys.component.scss'],
})
export class ListDevicesRegistrysComponent implements OnInit {
  registryDevices!: DevicesRegistrys[];
  stateColorHigh: string = 'white';
  stateColorMedium: string = 'white';
  stateColorLow: string = 'white';

  constructor(
    private devicesService: DevicesService,
    private facadeDevices: DevicesFacade
  ) {}

  ngOnInit(): void {
    const _timeInterval = interval(1000);
    _timeInterval.subscribe(() => {
      this.devicesService.getLastRegistrys().subscribe((response) => {
        this.registryDevices = response;
        this.facadeDevices.loadRegistrys(this.registryDevices);
        if (this.registryDevices[0].state === State.High) {
          this.stateColorHigh = 'green';
          this.stateColorMedium = 'white';
          this.stateColorLow = 'white';
        }
        if (this.registryDevices[0].state === State.Medium) {
          this.stateColorMedium = 'yellow';
          this.stateColorHigh = 'white';
          this.stateColorLow = 'white';
        }
        if (this.registryDevices[0].state === State.Low) {
          this.stateColorLow = 'red';
          this.stateColorMedium = 'white';
          this.stateColorHigh = 'white';
        }
      });
    });
  }
}
