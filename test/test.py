bridge_length=2
weight=10
truck_weights=[7,4,5,6]

answer = 1
pass_truck = []
over_bridge = []
sequence=0
current=0
for i in range(bridge_length):
    over_bridge.append(0)
while truck_weights!=pass_truck:
    for i in range(-1, -(bridge_length)-1, -1):
        if over_bridge[i]!=0:
            if i==-1:
                pass_truck.append(over_bridge[i])
                over_bridge[i]=0
            else:
                over_bridge[i+1]=over_bridge[i]
                over_bridge[i]=0
        print(pass_truck)
        print(over_bridge)
    for i in over_bridge:
        current+=i
    if sequence<len(truck_weights):
        if current+truck_weights[sequence]<=weight:
            over_bridge[0]=truck_weights[sequence]
            sequence+=1
    current=0
    answer+=1