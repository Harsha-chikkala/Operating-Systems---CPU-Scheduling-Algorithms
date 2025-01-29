def sort_by_priority(arrival, burst, priority, pid):
    processes = list(zip(arrival, burst, priority, pid))
    processes.sort(key=lambda x: (x[0], x[2])) 
    return zip(*processes)

def calculate_times(arrival, burst, priority):
    n = len(arrival)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    executed = [False] * n
    current_time = 0
    completed = 0

    while completed < n:
        highest_priority = float('inf')
        next_process = -1

        for i in range(n):
            if not executed[i] and arrival[i] <= current_time and priority[i] < highest_priority:
                highest_priority = priority[i]
                next_process = i

        if next_process == -1:
            current_time += 1
        else:
            completion_time[next_process] = current_time + burst[next_process]
            turnaround_time[next_process] = completion_time[next_process] - arrival[next_process]
            waiting_time[next_process] = turnaround_time[next_process] - burst[next_process]
            executed[next_process] = True
            current_time = completion_time[next_process]
            completed += 1

    return waiting_time, turnaround_time, completion_time

pid = [1, 2, 3, 4, 5, 6, 7]
arrival = [0, 2, 1, 4, 6, 5, 7]
burst = [3, 5, 4, 2, 9, 4, 10]
priority = [2, 6, 3, 5, 7, 4, 10]  

arrival, burst, priority, pid = sort_by_priority(arrival, burst, priority, pid)

waiting_time, turnaround_time, completion_time = calculate_times(arrival, burst, priority)

print("PID\tArrival Time\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(len(pid)):
    print(f"{pid[i]}\t{arrival[i]}\t\t{burst[i]}\t\t{priority[i]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

avg_waiting_time = sum(waiting_time) / len(waiting_time)
avg_turnaround_time = sum(turnaround_time) / len(turnaround_time)
print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")