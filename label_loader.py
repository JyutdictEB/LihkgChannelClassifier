def load_label_index(path):
    ret = {}
    with open(path,encoding='utf-8') as f:
        for l in f:
            grp = str(l).strip().split('\t')
            ret[grp[0]] = int(grp[1])
    return ret

def pack_data_with_n(labels,lines,n):
    ret = []
    recorder = {l:0 for l in labels.keys()}
    for l in lines:
        grp = l.strip().split('\t')
        if(grp[0] not in recorder.keys() or recorder.get(grp[0],0) > n):
            continue
        recorder[grp[0]] = recorder.get(grp[0],0) + 1
        ret.append(l)
    print(recorder)
    return ret