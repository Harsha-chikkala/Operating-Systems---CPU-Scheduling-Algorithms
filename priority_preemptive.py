def preemptive_priority_scheduling(processes):
    n = len(processes)
    remaining_time = [p[2] for p in processes]  
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [-1] * n 
    
    current_time = 0
    completed = 0
    prev = 0
    
    while completed != n:
       
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0:
                if processes[i][3] < highest_priority:
                    highest_priority = processes[i][3]
                    idx = i
                elif processes[i][3] == highest_priority and processes[i][1] < processes[idx][1]:
                    idx = i
        
        if idx != -1:
            if response_time[idx] == -1:
                response_time[idx] = current_time - processes[idx][1]
            
            remaining_time[idx] -= 1
            current_time += 1
            prev = current_time
            
            if remaining_time[idx] == 0:
                completed += 1
                completion_time[idx] = current_time
                turnaround_time[idx] = completion_time[idx] - processes[idx][1]
                waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
        else:
            current_time += 1
    
    avg_turnaround_time = sum(turnaround_time) / n
    avg_waiting_time = sum(waiting_time) / n
    avg_response_time = sum(response_time) / n
    
    return (completion_time, turnaround_time, waiting_time, response_time, 
            avg_turnaround_time, avg_waiting_time, avg_response_time)


processes = [
    # Format: [pid, arrival_time, burst_time, priority]
    [1, 0, 3, 3],
    [2, 1, 4, 2],
    [3, 2, 6, 4],
    [4, 3, 4, 6],
    [5, 5, 2, 10]
]

results = preemptive_priority_scheduling(processes)

print("Process\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting\t\tResponse")
for i, p in enumerate(processes):
    print(f"P{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t\t{results[0][i]}\t\t{results[1][i]}\t\t{results[2][i]}\t\t{results[3][i]}")

print(f"\nAverage Turnaround Time: {results[4]:.2f}")
print(f"Average Waiting Time: {results[5]:.2f}")
print(f"Average Response Time: {results[6]:.2f}")