from math import log, e
import numpy as np

def cost(r, config):
    m = config['m']
    n = config['n']
    omega = config['omega']
    tmp = n / (2**omega * m)
    p = m / (1 - tmp) + tmp**r * ((m + n) / 2 - m / (1-tmp))
    return p

def breaking_condition(r, config):
    n = config['n']
    delta = config['delta']
    c = config['delta']
    omega = config['omega'] 
    m = config['m']
    t = n / (m * m)
    p = -1 * m / (1-t) + delta * m / t * c
    q = (m + n) / 2 - m / (1-t)
    i_0 = 1 + log(p/q) / log(t)
    return i_0

def trace(r, config):
    t = config['n'] / (config['m']*2**config['omega']) * cost(r-1, config)
    return t

def m_in_bound(config):
    m_lower_bound = 2 ** config['omega']
    m_upper_bound = 2 ** (2 - config['omega'] + 2*config['omega']/config['delta'])*config['n']/(config['delta'] * e)
    return (config['m'] >= m_lower_bound) and (config['m'] <= m_upper_bound)

def main():
    S_COST_SHIFT = 22 
    DELTA = 7.0
    C = 1000.0
    OMEGA = 3.0
    M_SHIFT = 17
    config = {'n': 2.0**S_COST_SHIFT,
        'm': 2.0**M_SHIFT,
        'c': C,
        'delta': DELTA,
        'omega': OMEGA
        }

    print 'm in bound == %s' % m_in_bound(config)
    for r in range(1, 10):
        print 'layer: %d' % r
        print 'cost == %0.2f' % cost(r, config)
        print 'cost in trace == %0.2f' % trace(r, config)
        print 'memory latency for trace <= %0.2f' % (config['delta'] * config['m'] * config['c'])
        print 'ratio >= %0.2f' % (trace(r, config) / (config['delta'] * config['m'] * config['c']))
        print 

if __name__ == '__main__':
    main()
