import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { DevicesRegistrys } from '../commons/models/registrys.model';

@Injectable({
  providedIn: 'root',
})
export class DevicesService {
  constructor(private http: HttpClient) {}

  getLastRegistrys(): Observable<DevicesRegistrys[]> {
    return this.http.get<DevicesRegistrys[]>(
      `${environment.interactionsCoreBackendURL}/readers`
    );
  }
}
