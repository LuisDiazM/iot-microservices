import * as fromDevices from './devices.actions';

describe('yDevicess', () => {
  it('should return an action', () => {
    expect(fromDevices.yDevicess().type).toBe('[Devices] Y Devicess');
  });
});
