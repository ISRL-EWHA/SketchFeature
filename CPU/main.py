from sketchfeature import *

def read_dataset(csv_file_path, num_pkts):
    dtype_dict = {i: int for i in range(6)}
    dtype_dict[6] = float
    all_trace = pd.read_csv(csv_file_path, nrows = num_pkts, header=None, dtype=dtype_dict)
    return all_trace
    
m = 3
d = 3
m_bf = 2
d_bf = 3
num_ql = 50
min_q = 0
max_q = 1500

sketchfeature = SketchFeature(m, d, m_bf, d_bf, num_ql, min_q, max_q)

trace = read_dataset("./dataset.csv",2598503)
for flow in trace.itertuples(index=False):
    flow_id = get_flow_id(flow)
    value = get_packet_size(flow)
    sketchfeature.encoding(flow_id,value)
