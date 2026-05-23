## Documentation

### 'yInit' targets

`yInit` defines the following targets that are used to classify services by task and also determinate at what boot stage service is to be loaded. Below-defined targets and its scopes, targets are in order of actual boot: 

1. **init** – does initializations of special filesystems: devfs, procfs, sysfs, 
2. **launch** – cheks and mounts root and user filesystems, loads drivers, sets up hardware settings, launches logging capability
3. **network** – initializes network
4. **network.online** – brings up network services that require network access; fullfilling this target means that the machine is probably online
5. **system** – starts system services such as SSH server
6. **user** – runs user related services: login manager, task scheduler.

