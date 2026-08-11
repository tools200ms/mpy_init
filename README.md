![caption](logo.svg)
*Unix init system developed in Python.*

> **Q:**
> 
> What's the point of developing an init system using hi-level language that additionally requires VM (an overhead)? Init systems, after all, should be light and responsive pieces of software.
> 
> **A:**
> 
> Let's use **Cython!** 
> 
> Python is a flexible object-oriented language, great for expressing complexity – that Init System must deal with.
> 
> Currently, init system's scope goes beyond of simply being a service start/stop supervisor. Tasks such as job scheduling, monitoring and log handling are essential. Python - and inherently Cython comes with a solid module base that can be used for these tasks.

The goal is to develop Python init system for Linux and BSD systems that also provides capabilities to support deployment pipelines for Python projects.

Moreover, Python is well-known form GPIO projects, see [README-raspberrypi.md](README-raspberrypi.md) to check out how `YInit` might be integrated with a bare-metal hardware!

## Flexibility

1. `YInit` can work as **Cython compiled binary**, or be launched in **Python VM**.

2. `YInit` is split into:
   - Host OS services - Everything that is requied by bare-metal or VM.
   - Init facilities - Services provided by Python
   - Network services - User services that interact with network sockets
   - User services - 

### Host OS services (init)


Host OS services are the basic services that provide: 

- root fileststem check and mounting
- provides special fileystems: `/dev`, `/sys`, `/pro`c
- device initialization and drivers

These are the services to be run while running `YInit` on bare-metal or in virtual machine.

### Service facilities
These are `YInit` functions that provide: 
- Monitoring and scheduling
- Logging
- Configuration provider
- Messaging

Any sevice, regardless if it's running binary such as SSH server, or Python Project run in VM requiers above 4 factors, more details in [WIKI](...).

### User services

In `YInit` user services are programs that directly provide functions requied by user.

**Python VM** mode is designated for deploying Python projects that run in containers.

Simply speaking, init system that runs in a container reuiers just a subset of features (host OS provides the rest). By developing project in Python YInit can work as a platform for deploing Python projects in containers.

### Enviroments
Containerized enviroment is a subset of bare-metal 

### Bare-metal

**For bare-metal setups:**
2. **Time** – Ensures OS runs with a correct time.
3. **Network** – Ensures applications are capable of communication (necessary also for a time synchronization).
4. **mDNS** – 'YInit' advertises it's IP using mDNS and provides MQTT for monitoring.
5. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.
5. **GPIO support** – GPIO support to provide: display and keypad interface (for a selected hardware).

### Python modules
It provides the following modules: 

**For all setups (bare-metal & container VMs):**
1. **Task scheduler** – Provides cron functionality.
2. **Log handler** – 
3. **Web-configurator & REST API** – Administrative module for managing configuration over web/api.
4. **Messaging [e-mail, MQTT]** – 
5. Exception handling and automatic restarts of services

It can be thought as the platform for launching Python projects.


### 'yInit' features

Planned 'yInit' feature: 

- **Parallel boot** – boot services in parallel (if no dependency bound).

# References

[Cython Project page](https://cython.org/)
