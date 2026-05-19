# 'yInit' – Unix init system developed in Python

This is (wh)YInit – Unix init system developed in Python. 

> **Q:**
> 
> What's the point of developing an init system using hi-level language that additionally requires VM (an overhead)? Init systems, after all, should be light and responsive pieces of software.
> 
> **A:**
> 
> Let's use Cython! 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.
> 
> Currently, init systems go beyond simply being a launch platform. Tasks such as job scheduling, monitoring, log handling, reporting, remote control, and system integration are essential, regardless of whether the environment is a container or a bare-metal system.

Python - and inherently Cython provides a vast diversity of modules that can be used to build: 
- web control panel
- hardware support of hardware such as mini-displays and keypards (via GPIO - on boards such as Raspberry Pi)
- communication protocols for system integrations (via e.g. MQTT)

The goal is to develop a modern, feature-rich, and user-friendly init system for Unix that integrates with both **bare-metal** and **containerized** environments.

## YInit scope

'YInit' goes beyond the scope of a key Init System functinality that is: 'start/stop & monitor' services.

It provides the following functinalities: 

**For all setyups (bare-metal & container VMs):**
1. **Periodic tasks** – Provides cron functionality.
2. **Web-configurator & REST API** – Administrative module for managing configuration over web/api.
3. **MQTT and mDNS** – 'YInit' advertises it's IP using mDNS and provides MQTT for monitoring.

**For bare-metal setups:**
2. **Time** – Ensures OS runs with a correct time.

3. **Network** – Ensures applications are capable of communication (necessary also for a time synchronization).

4. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.

5. **Hardware support** – GPIO support to provide: display and keypad interface (for a selected hardware).


### 'yInit' features

Planned 'yInit' feature: 

- **Parallel boot** – boot services in parallel (if no dependency bound).

## Documentation

### 'yInit' targets

`yInit` defines the following targets that are used to classify services by task and also determinate at what boot stage service is to be loaded. Below-defined targets and its scopes, targets are in order of actual boot: 

1. **init** – does initializations of special filesystems: devfs, procfs, sysfs, 
2. **launch** – cheks and mounts root and user filesystems, loads drivers, sets up hardware settings, launches logging capability
3. **network** – initializes network
4. **network.online** – brings up network services that require network access; fullfilling this target means that the machine is probably online
5. **system** – starts system services such as SSH server
6. **user** – runs user related services: login manager, task scheduler.

