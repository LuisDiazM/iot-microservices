import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListDevicesRegistrysComponent } from './components/list-devices-registrys/list-devices-registrys.component';

const routes: Routes = [{ path: '', component: ListDevicesRegistrysComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
