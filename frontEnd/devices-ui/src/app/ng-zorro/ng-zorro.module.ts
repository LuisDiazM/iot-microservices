import { NgModule } from '@angular/core';
import { NzMenuModule } from 'ng-zorro-antd/menu';
import { NzGridModule } from 'ng-zorro-antd/grid';


@NgModule({
  exports: [NzMenuModule, NzGridModule],
})
export class NgZorroModule {}
