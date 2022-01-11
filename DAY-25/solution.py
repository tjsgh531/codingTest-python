from collections import deque

def solution(bridge_length, weight, truck_weights):
    inbridge = deque([0 for i in range(bridge_length)])
    wait_trucks = deque(truck_weights)
    
    time =0;
    inbridge_weight = 0

    while(1):
        if wait_trucks: # 들어올 차가 남아 있는 경우
            leave_truck_weight = inbridge.popleft()
            inbridge_weight -= leave_truck_weight
          
            if inbridge_weight + wait_trucks[0] <= weight: #다음 차가 들어와도 될 경우
                enter_truck_weight = wait_trucks.popleft()      
                inbridge_weight += enter_truck_weight
                inbridge.append(enter_truck_weight)
            else : #다음 차가 들어오면 안되는 경우
                inbridge.append(0)
        else: # 들어올 차는 없지만 다리위에 차가 남아 있을 때
            for i in range(bridge_length):
                if inbridge[bridge_length - i -1] != 0 :
                    time += bridge_length - i
                    break;
            break
        time += 1
    return time