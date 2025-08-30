# MicroPython init system [Proposal + experimental code]

This is a proposal for a Linux init system based on MicroPython. **Notice: included source code is an experimental, proof-of-concept working version to be available soon.**

## Design philosophy

Proposed MicroPython-based init system, called `mpy_init`, is designed to run on bare metal and in containers.

### Project assumptions:

1. **Cross-platform** – `mpy_init` inherits MicroPython's cross-platform nature, ensuring compatibility with all UNIX systems.

2. **Target-based** – `mpy_init` implements a current, target-based system initialization approach, similar to what is used in SystemD.

3. **In between OpenRC and SystemD** – `mpy_init` goes beyond the traditional scope of classic init systems like OpenRC and SysVinit. In addition to service initialization and control, it also manages: 

    a. **Time** – ensures OS runs with a correct time.

    b. **Network** – ensures applications are capable of communication (necessary also for time synchronization).

     c. **Periodic tasks** – provides cron functionality.

     d. **SSD trimming** – Ensure partitions located on flash storage are mounted with a TRIM option, and/or periodic trims are enabled.
3. **Parallel boot** – boot services in parallel (if no dependency bound).

We believe that the above scope defines a good balance in what a modern init system should do, what not.

## Features

Micropython brings the following interesting features to initsystem:

**API out-of-the-box** — Micropython's VM is available since boot time throughout the entire OS run-time. Integration with init-system allows on bringing in API and web access that is handled by isolated VM. That simplifies device initialization and configuration over network, providing a layer of security.


## Security

Micropython lacks a built-in mechanism for process separation. Therefore, project elevates Unix kernel features to ensure proper privilabe and separation handling.



1. **Performance** - having MicroPython's VM already loaded makes scripts (compiled to bytecodes) to be run fast. Moreover, MicroPython is light-weight and optimized for resource-poor devices. Therefore, even in the case of running it on slow hardware, it should be a suitable solution.

2. **Security through simplification** - shell scripts can be replaced by Python code that is easier to read and audit.

3. **Efficient development: debug and testing tools** - Python provides robust development and testing tools.

4. **More powerful shell** - traditional shell (bash, ash) can be replaced with [ipython](https://github.com/ipython/ipython) or [Xonsh](https://xon.sh/) - shells developed in Python. These projects keep compatibility with traditional shells (and theirs pros), while providing also Python features (even more Pros!).





# References

- The MicroPython Project repository [link](https://github.com/micropython/micropython).
