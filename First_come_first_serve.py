def main():
    n = int(input("Enter the number of processes: "))

    arrivalTime = [0] * n
    burstTime = [0] * n
    completionTime = [0] * n
    turnaroundTime = [0] * n
    waitingTime = [0] * n
    responseTime = [0] * n

    for i in range(n):
        arrivalTime[i] = int(input(f"Enter arrival time for process {i + 1}: "))
        burstTime[i] = int(input(f"Enter burst time for process {i + 1}: "))

    completionTime[0] = arrivalTime[0] + burstTime[0]

    for i in range(1, n):
        if arrivalTime[i] > completionTime[i - 1]:
            completionTime[i] = arrivalTime[i] + burstTime[i]
        else:
            completionTime[i] = completionTime[i - 1] + burstTime[i]

    for i in range(n):
        turnaroundTime[i] = completionTime[i] - arrivalTime[i]
        waitingTime[i] = turnaroundTime[i] - burstTime[i]
        responseTime[i] = waitingTime[i]
    
    avg_turnaroundtime = sum(turnaroundTime) / n
    avg_waitingtime = sum(waitingTime) / n

    print(f"\nAverage Turnaround time of all processes is {avg_turnaroundtime}")
    print(f"Average Waiting time of all processes is {avg_waitingtime}\n")

    print("\n{:<10} {:<15} {:<12} {:<18} {:<18} {:<15} {:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time", "Response Time"))
    
    for i in range(n):
        print("{:<10} {:<15} {:<12} {:<18} {:<18} {:<15} {:<15}".format(
            i + 1, arrivalTime[i], burstTime[i], completionTime[i], turnaroundTime[i], waitingTime[i], responseTime[i]))

if __name__ == "__main__":
    main()
