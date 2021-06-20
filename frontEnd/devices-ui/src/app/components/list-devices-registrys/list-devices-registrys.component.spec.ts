import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListDevicesRegistrysComponent } from './list-devices-registrys.component';

describe('ListDevicesRegistrysComponent', () => {
  let component: ListDevicesRegistrysComponent;
  let fixture: ComponentFixture<ListDevicesRegistrysComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListDevicesRegistrysComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListDevicesRegistrysComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
