import pandas as pd
import numpy as np
import binascii
import math
from collections import defaultdict
import hashlib

def calc_hash_val(flow_id, ql, i):
    sip = "%08x" % flow_id[0]
    dip = "%08x" % flow_id[1]
    port = "%08x" % ((flow_id[2] << 16) + flow_id[3])
    proto = "%02x" % flow_id[4]
    ql = "%06x" % (ql<<8 + i)
    data = sip + dip + port + proto + ql
    hash_val = hash(data) & 0xFFFFFFFFFFFFFFFF
    return hash_val

def calc_hash_val_mt(flow_id, ql, i):
    sip = "%08x" % flow_id[0]
    dip = "%08x" % flow_id[1]
    port = "%08x" % ((flow_id[2] << 16) + flow_id[3])
    proto = "%02x" % flow_id[4]
    ql = "%06x" % (ql<<8 + i + 137)
    data = sip + dip + port + proto + ql
    hash_val = hash(data) & 0xFFFFFFFFFFFFFFFF
    return hash_val

def get_flow_id(flow):
    return flow[0:5]

def get_packet_size(flow):
    return flow[5]
    
class SketchFeature():
    def __init__(self, m, d, m_bf, d_bf, num_ql, min_q, max_q):
        self.name = "SketchFeature"
        self.memory_bf = m_bf * 1024 * 1024 * 8
        self.memory = m * 1024 * 1024 * 8 - self.memory_bf
        self.d = d
        self.d_bf = d_bf
        self.num_ql = num_ql
        self.ql_list = np.linspace(0, max_q, num = num_ql+1)
        self.w = int(self.memory / 32 / d)
        self.w_bf = int(self.memory_bf / d_bf)
        self.sketch = [[0 for y in range(self.w)] for x in range(d)]
        self.bloom_filter = [[0 for y in range(self.w_bf)] for x in range(d_bf)]

    def get_ql(self, value):
        left = 0
        right = self.num_ql-1
        while left <= right:
            mid = (left+right)//2
            if self.ql_list[mid] <= value < self.ql_list[mid+1]:
                return mid
            elif self.ql_list[mid] <= value <= self.ql_list[mid+1] and mid == self.num_ql-1:
                return mid
            elif value < self.ql_list[mid]:
                right = mid - 1
            else:
                left = mid + 1

    def membership_test(self, flow_id, ql):
        flag = True
        for i in range(self.d_bf):
            loc = calc_hash_val_mt(flow_id, ql, i) % self.w_bf
            if self.bloom_filter[i][loc] == 0:
                flag = False
                break
        return flag
    
    def encoding(self, flow_id, value):
        ql = self.get_ql(value)
        if ql == None:
            return
        for i in range(self.d_bf):
            loc = calc_hash_val_mt(flow_id, ql, i) % self.w_bf
            self.bloom_filter[i][loc] = 1
        for i in range(self.d):
            loc = calc_hash_val(flow_id, ql, i) % self.w
            self.sketch[i][loc] += 1
    
    def decoding(self, flow_id, ql):
        if self.membership_test(flow_id,ql) == True:
            value = 4294967295
            for i in range(self.d):
                loc = calc_hash_val(flow_id, ql, i) % self.w
                value = min(self.sketch[i][loc],value)
        return value
