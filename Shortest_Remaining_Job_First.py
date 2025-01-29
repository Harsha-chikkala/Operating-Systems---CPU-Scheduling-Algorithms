def srtf(processes):
    n = len(processes)
    
    remaining_time = [processes[i][2] for i in range(n)]  
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    start_time = [-1] * n  
    current_time = 0
    completed = 0
    prev = -1
    
    while completed != n:
        idx = -1
        min_remaining_time = float('inf')
        
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0: 
                if remaining_time[i] < min_remaining_time:
                    min_remaining_time = remaining_time[i]

                    idx = i
        
        if idx != -1:
            if start_time[idx] == -1:
                start_time[idx] = current_time
            
            remaining_time[idx] -= 1
            
            if remaining_time[idx] == 0:  
                completion_time[idx] = current_time + 1
                turnaround_time[idx] = completion_time[idx] - processes[idx][1]
                waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
                completed += 1
        
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
    
    srtf(processes)