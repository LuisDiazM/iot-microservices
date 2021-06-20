import { Component, OnInit } from '@angular/core';
import { DevicesRegistrys } from 'src/app/commons/models/registrys.model';
import { DevicesService } from '../../services/devices.service';
import {State} from '../../commons/models/registrys.model'
import {interval} from 'rxjs'

@Component({
  selector: 'app-list-devices-registrys',
  templateUrl: './list-devices-registrys.component.html',
  styleUrls: ['./list-devices-registrys.component.scss'],
})
export class ListDevicesRegistrysComponent implements OnInit {
  registryDevices!: DevicesRegistrys[];
  stateColorHigh: string = 'white';
  constructor(private devicesService: DevicesService) {}

  ngOnInit(): void {

    const _timeInterval = interval(1000)
    _timeInterval.subscribe(()=>{
      this.devicesService.getLastRegistrys().subscribe((response) => {
        this.registryDevices = response;
        console.log(this.registryDevices[0].state)
        if(this.registryDevices[0].state===State.High){
          this.stateColorHigh = "green"
        }
        if(this.registryDevices[0].state===State.Medium){
          this.stateColorHigh = "yellow"
        }
        if(this.registryDevices[0].state===State.Low){
          this.stateColorHigh = "red"
        }
      });
    })
  }
}
