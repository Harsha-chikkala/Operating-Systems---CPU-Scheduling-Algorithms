def sjf(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    
    while completed != n:
        idx = -1
        min_burst_time = float('inf')
        
        for i in range(n):
            if processes[i][1] <= current_time and not is_completed[i]:
                if processes[i][2] < min_burst_time:
                    min_burst_time = processes[i][2]
                    idx = i
                if processes[i][2] == min_burst_time:
                    if processes[i][1] < processes[idx][1]:
                        idx = i
        
        if idx != -1:
            completion_time[idx] = current_time + processes[idx][2]
            turnaround_time[idx] = completion_time[idx] - processes[idx][1]
            waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
            current_time = completion_time[idx]
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1  
    
    print(f"{'ProcessId':<12}{'Arrival Time':<15}{'Burst Time':<12}{'Completion Time':<18}{'Turn Around Time':<18}{'Waiting Time':<15}")
    print("-" * 85)
    
    for i in range(n):
        print(f"{processes[i][0]:<12}{processes[i][1]:<15}{processes[i][2]:<12}{completion_time[i]:<18}{turnaround_time[i]:<18}{waiting_time[i]:<15}")

if __name__ == "__main__":
    processes = []
    
    for i in range(5):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append([pid, arrival_time, burst_time])
    
    sjf(processes)
