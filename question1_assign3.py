
processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 4, 5, 6]
burst_time = [24, 3, 3, 12]
priority = [3, 1, 4, 2]


n = len(processes)
# all the functions names and the variable names are self explanatory 
def calculate_waiting_time(bt, wt, tat):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = tat[i-1] - bt[i-1]

def calculate_turnaround_time(bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def fcfs_scheduling():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0

    # Calculate waiting time
    for i in range(1, n):
        wt[i] = burst_time[i-1] + wt[i-1]

    # Calculate turnaround time
    calculate_turnaround_time(burst_time, wt, tat)

    return wt, tat

def sjf_scheduling():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0

    for i in range(n):
        wt[i] = 0
        for j in range(i):
            wt[i] += burst_time[j]

    calculate_turnaround_time(burst_time, wt, tat)

    return wt, tat

def priority_scheduling():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0

    for i in range(1, n):
        wt[i] = burst_time[i-1] + wt[i-1]

    calculate_turnaround_time(burst_time, wt, tat)

    return wt, tat


def round_robin_scheduling(quantum):
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0
    remaining_time = [0] * n

    for i in range(n):
        remaining_time[i] = burst_time[i]

    t = 0
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False

                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t = t + remaining_time[i]
                    wt[i] = t - burst_time[i]
                    remaining_time[i] = 0

        if done:
            break

    calculate_turnaround_time(burst_time, wt, tat)

    return wt, tat

fcfs_wt, fcfs_tat = fcfs_scheduling()
sjf_wt, sjf_tat = sjf_scheduling()
priority_wt, priority_tat = priority_scheduling()
rr_wt, rr_tat = round_robin_scheduling(4)

def display_schedule_results(algorithm_name, wt, tat):
    print(f"\n{algorithm_name} Scheduling:")
    print("Process\t\tWT\t\tTAT")
    for i in range(n):
        print(f"{processes[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"Average WT: {sum(wt)/n}")
    print(f"Average TAT: {sum(tat)/n}")

display_schedule_results("FCFS", fcfs_wt, fcfs_tat)
display_schedule_results("SJF", sjf_wt, sjf_tat)
display_schedule_results("Priority", priority_wt, priority_tat)
display_schedule_results("Round Robin", rr_wt, rr_tat)

average_waiting_time = {
    "FCFS": sum(fcfs_wt) / n,
    "SJF": sum(sjf_wt) / n,
    "Priority": sum(priority_wt) / n,
    "Round Robin": sum(rr_wt) / n
}

average_turnaround_time = {
    "FCFS": sum(fcfs_tat) / n,
    "SJF": sum(sjf_tat) / n,
    "Priority": sum(priority_tat) / n,
    "Round Robin": sum(rr_tat) / n
}

most_suitable_algorithm = min(average_waiting_time, key=average_waiting_time.get)

print(f"\nMost suitable scheduling algorithm is {most_suitable_algorithm} with average waiting time of {average_waiting_time[most_suitable_algorithm]} and average turnaround time of {average_turnaround_time[most_suitable_algorithm]}")
