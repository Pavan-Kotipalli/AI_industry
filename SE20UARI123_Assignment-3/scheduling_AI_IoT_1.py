def calculate_waiting_turnaround_time(processes, n, burst_time, priority, time_quantum):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = burst_time.copy()
    current_time = 0
    completed_processes = 0

    while completed_processes < n:
        # FCFS
        for i in range(n):
            if current_time >= processes[i][1] and remaining_time[i] > 0:
                waiting_time[i] = current_time - processes[i][1]
                current_time += remaining_time[i]
                turnaround_time[i] = waiting_time[i] + burst_time[i]
                remaining_time[i] = 0
                completed_processes += 1

        # SJF
        min_burst_time = float('inf')
        shortest_job = -1
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] < min_burst_time and remaining_time[i] > 0:
                min_burst_time = remaining_time[i]
                shortest_job = i

        if shortest_job == -1:
            current_time += 1
        else:
            waiting_time[shortest_job] += current_time - processes[shortest_job][1]
            current_time += remaining_time[shortest_job]
            turnaround_time[shortest_job] = waiting_time[shortest_job] + burst_time[shortest_job]
            remaining_time[shortest_job] = 0
            completed_processes += 1

        # PS
        min_priority = float('inf')
        highest_priority_job = -1
        for i in range(n):
            if processes[i][1] <= current_time and priority[i] < min_priority and remaining_time[i] > 0:
                min_priority = priority[i]
                highest_priority_job = i

        if highest_priority_job == -1:
            current_time += 1
        else:
            waiting_time[highest_priority_job] += current_time - processes[highest_priority_job][1]
            current_time += remaining_time[highest_priority_job]
            turnaround_time[highest_priority_job] = waiting_time[highest_priority_job] + burst_time[highest_priority_job]
            remaining_time[highest_priority_job] = 0
            completed_processes += 1

        # RR
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0:
                if remaining_time[i] <= time_quantum:
                    current_time += remaining_time[i]
                    turnaround_time[i] = waiting_time[i] + burst_time[i]
                    remaining_time[i] = 0
                    completed_processes += 1
                else:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum

    return waiting_time, turnaround_time

# Process information
processes = [
    ("P1", 0, 24, 3),
    ("P2", 4, 3, 1),
    ("P3", 5, 3, 4),
    ("P4", 6, 12, 2)
]

n = len(processes)
burst_time = [process[2] for process in processes]
priority = [process[3] for process in processes]
time_quantum = 4

waiting_time, turnaround_time = calculate_waiting_turnaround_time(processes, n, burst_time, priority, time_quantum)

# Print results
print("Process\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i][0]}\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Calculate average waiting time and average turnaround time for all schedules
avg_waiting_time_fcfs = sum(waiting_time) / n
avg_turnaround_time_fcfs = sum(turnaround_time) / n

# SJF
processes_sjf = sorted(processes, key=lambda x: (x[1], x[2]))
burst_time_sjf = [process[2] for process in processes_sjf]
waiting_time_sjf, turnaround_time_sjf = calculate_waiting_turnaround_time(processes_sjf, n, burst_time_sjf, priority, time_quantum)
avg_waiting_time_sjf = sum(waiting_time_sjf) / n
avg_turnaround_time_sjf = sum(turnaround_time_sjf) / n

# PS
processes_ps = sorted(processes, key=lambda x: (x[3], x[1]))
burst_time_ps = [process[2] for process in processes_ps]
waiting_time_ps, turnaround_time_ps = calculate_waiting_turnaround_time(processes_ps, n, burst_time_ps, priority, time_quantum)
avg_waiting_time_ps = sum(waiting_time_ps) / n
avg_turnaround_time_ps = sum(turnaround_time_ps) / n

# RR
waiting_time_rr, turnaround_time_rr = calculate_waiting_turnaround_time(processes, n, burst_time, priority, time_quantum)
avg_waiting_time_rr = sum(waiting_time_rr) / n
avg_turnaround_time_rr = sum(turnaround_time_rr) / n

# Display average waiting times and average turnaround times for all schedules
print("\nAverage Waiting Times:")
print(f"FCFS: {avg_waiting_time_fcfs}")
print(f"SJF: {avg_waiting_time_sjf}")
print(f"PS: {avg_waiting_time_ps}")
print(f"RR: {avg_waiting_time_rr}")

print("\nAverage Turnaround Times:")
print(f"FCFS: {avg_turnaround_time_fcfs}")
print(f"SJF: {avg_turnaround_time_sjf}")
print(f"PS: {avg_turnaround_time_ps}")
print(f"RR: {avg_turnaround_time_rr}")

# Determine the best scheduling algorithm based on average waiting time
scheduling_algorithms = ["FCFS", "SJF", "PS", "RR"]
avg_waiting_times = [avg_waiting_time_fcfs, avg_waiting_time_sjf, avg_waiting_time_ps, avg_waiting_time_rr]

avg_turnaround_time = [avg_turnaround_time_fcfs, avg_turnaround_time_sjf, avg_turnaround_time_ps, avg_turnaround_time_rr]

best_schedule = scheduling_algorithms[avg_waiting_times.index(min(avg_waiting_times)) and avg_turnaround_time.index(min(avg_turnaround_time))]
print(f"\nThe best schedule is: {best_schedule} (Minimum Average Waiting Time and Minimum Average Turnaround Time )")
