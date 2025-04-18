# MicroPython init system

This is a proposal for a Linux init system based on MicroPython.

## Design philosophy

Proposed MicroPython-based init system, called `mpy_init`, is designed to run on bare metal and in containers.

### Project assumptions:

0. **Cross-platform** – `mpy_init` inherits MicroPython's cross-platform nature, ensuring compatibility with all UNIX systems.

1. **Target-based** – `mpy_init` implements a current, target-based system initialization approach, similar to what is used in SystemD.

2. **In between OpenRC and SystemD** – `mpy_init` goes beyond the traditional scope of classic init systems like OpenRC and SysVinit. In addition to service initialization and control, it also manages: 

    a. **Time** – ensures OS runs with a correct time.

    b. **Network** – ensurec applications are capable of communication (necessary for time synchronization).

     c. **Periodic tasks** – cron functionality.
   
    We believe that the above scope defines a good balance in what a modern init system should do, what not.

3. **Provide build-in diagnosis service**


`myp_init` shall test if it is launched on bear-metal or in continued environment. It affects a launch process (that is much simpler in the second case).

## Advantages

### Performance
Having MicroPython's VM already loaded makes scripts (compiled to bytecodes) to be run fast – VM is 'ready' at any time.
MicroPython is light-weight and optimized for resource-poor devices. Therefore, even in the case of running it on slow hardware, it should be a suitable solution.

### Eficient development, debug and testing
Unlike shell scripts, Python provides robust Development tools.

## World of Python
Traditional shell (bash, ash) can be replaced with ipython or equivalent developed in Python.


# TODO

- Think about security.

