def get_trace(file_name):
    trace = []
    timestamps = []
    directions = []
    with open(file_name) as rf:
        trace = rf.readlines()

    for t in trace:
        timestamp = t.split('\t')[0]
        direction = t.split('\t')[1]
     
        timestamps.append(timestamp)
        directions.append(direction)

    return (timestamps, directions)

def write_trace(file_name, timestamps, directions):
    with open(file_name, 'w') as wf:
        for i in range(len(timestamps)):
            wf.write(timestamps[i] + "\t" + directions[i] + "\n")

for i in range(0,95):
    for j in range(0, 25):
        for k in range(0,64):
            try:
                file_name = "outfolder/" + str(i) + "-" + str(j) + "_split_" + str(k) + ".cell"
                #file_name = "outfolder/" + str(i) + "_split_" + str(k) + ".cell"
                timestamps, directions = get_trace(file_name)

                out_file_name = "converted_dataset/" + str(i) + "-" + str(k + (64*j))
                write_trace(out_file_name, timestamps, directions)
            except:
                continue



#timestamps, directions = get_trace("outfolder/26-45_split_0.cell")
#write_trace("converted_dataset/1-1.cell", timestamps, directions)

