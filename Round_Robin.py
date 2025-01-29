def round_robin(processes, quantum):
    n = len(processes)
    remaining_time = [p[2] for p in processes]  
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [-1] * n 
    
    time = 0
    queue = []
    completed = 0
    
    while completed < n:
        for i in range(n):
            if processes[i][1] <= time and remaining_time[i] > 0 and i not in queue:
                queue.append(i)
        
        if not queue:
            time += 1
            continue
        
        current = queue.pop(0)
        
        if response_time[current] == -1:
            response_time[current] = time - processes[current][1]
        
        if remaining_time[current] <= quantum:
            time += remaining_time[current]
            remaining_time[current] = 0
            completed += 1
            
            turnaround_time[current] = time - processes[current][1]
            waiting_time[current] = turnaround_time[current] - processes[current][2]
        else:
            time += quantum
            remaining_time[current] -= quantum
            
            for i in range(n):
                if processes[i][1] <= time and remaining_time[i] > 0 and i not in queue and i != current:
                    queue.append(i)
            
            queue.append(current)
    
    avg_turnaround_time = sum(turnaround_time) / n
    avg_waiting_time = sum(waiting_time) / n
    avg_response_time = sum(response_time) / n
    
    return (turnaround_time, waiting_time, response_time, 
            avg_turnaround_time, avg_waiting_time, avg_response_time)

def main():
    time_quantum = int(input("Enter the time quantum: "))
    processes = []
    n = int(input("Enter no of processes: "))
    
    for i in range(n):
        pid = i + 1
        arrival_time = int(input(f"Enter the arrival time of P{pid}: "))
        burst_time = int(input(f"Enter the burst time of P{pid}: "))
        processes.append([pid, arrival_time, burst_time])
    
    results = round_robin(processes, time_quantum)
    
    print("\nProcess\tArrival\tBurst\tTurnaround\tWaiting\t\tResponse")
    for i, p in enumerate(processes):
        print(f"P{p[0]}\t{p[1]}\t{p[2]}\t{results[0][i]}\t\t{results[1][i]}\t\t{results[2][i]}")
    
    print(f"\nAverage Turnaround Time: {results[3]:.2f}")
    print(f"Average Waiting Time: {results[4]:.2f}")
    print(f"Average Response Time: {results[5]:.2f}")

if __name__ == "__main__":
    main()