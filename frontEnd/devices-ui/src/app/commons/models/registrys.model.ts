export interface DevicesRegistrys {
    _id:        ID;
    state:      State;
    voltage:    number;
    created_at: CreatedAt;
    device:     Device;
}

export interface ID {
    $oid: string;
}

export interface CreatedAt {
    $date: number;
}

export enum Device {
    IotDevicesEsp32 = "iot.devices.esp32",
}

export enum State {
    High = "HIGH",
    Low = "LOW",
    Medium = "MEDIUM"
}
