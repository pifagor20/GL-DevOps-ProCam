#!/usr/bin/env python3

import psutil
import argparse

def get_cpu_metrics():
    #scputimes(user=0.0, nice=0.0, system=0.0, idle=100.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
    cpu_metrics = tuple(psutil.cpu_times_percent(interval=1))

    user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = cpu_metrics
    #printed_metrics = [idle, user, guest, iowait, steal, system]

    print(
        f'system.cpu.idle {idle}',
        f'system.cpu.user {user}',
        f'system.cpu.guest {guest}',
        f'system.cpu.iowait {iowait}',
        f'system.cpu.steal {steal}',
        f'system.cpu.system {system}',
        sep='\n'
        )

def get_memory_metrics():

    # getting mem stat
    memory_metrics = tuple(psutil.virtual_memory())
    virtual_total, virtual_available, virtual_percent, virtual_used, virtual_free, virtual_active, virtual_inactive, virtual_buffers, virtual_cached, virtual_shared, virtual_slab = memory_metrics
    print(
         f'virtual total {virtual_total}',
         f'virtual used {virtual_used}',
         f'virtual free {virtual_free}',
         f'virtual shared {virtual_shared}',
         sep='\n'
        )

    # getting swap stat
    swap_metrics = tuple(psutil.swap_memory())
    swap_total, swap_used, swap_free, swap_percent, swap_sin, swap_sout = swap_metrics

    print(
         f'swap total {swap_total}',
         f'swap used {swap_used}',
         f'swap free {swap_free}',
         sep='\n'
        )

def main():
    description = "The script will print cpu and memory usage information."
    usage = './metrics cpu, ./metrics mem, ./metrics cpu mem'
    parser = argparse.ArgumentParser(description=description, usage=usage)
    parser.add_argument('input', action='store', nargs='*',
                        help="enter cpu or memory or both pf them to get the metrics")

    args = parser.parse_args()

    if 'cpu' in args.input:
        get_cpu_metrics()
    if 'mem' in args.input:
        get_memory_metrics()

if __name__ == '__main__':
    main()
