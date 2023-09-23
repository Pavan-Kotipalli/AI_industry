def fcfs(patients, current_time=0):
    if not patients:
        return []
    
    patients.sort(key=lambda p: p[1])  # Sort by arrival time
    patient = patients.pop(0)
    
    waiting_time = max(0, current_time - patient[1])
    turnaround_time = waiting_time + patient[2]
    
    return [(patient[0], waiting_time, turnaround_time)] + fcfs(patients, current_time + patient[2])

def sjf(patients, current_time=0):
    if not patients:
        return []

    patients.sort(key=lambda p: p[2])  # Sort by burst time
    patient = patients.pop(0)
    
    waiting_time = max(0, current_time - patient[1])
    turnaround_time = waiting_time + patient[2]
    
    return [(patient[0], waiting_time, turnaround_time)] + sjf(patients, current_time + patient[2])

def ps(patients, current_time=0):
    if not patients:
        return []

    patients.sort(key=lambda p: (p[1], -p[3]))  # Sort by arrival time and priority (higher priority first)
    patient = patients.pop(0)
    
    waiting_time = max(0, current_time - patient[1])
    turnaround_time = waiting_time + patient[2]
    
    return [(patient[0], waiting_time, turnaround_time)] + ps(patients, current_time + patient[2])

# Example usage:
patients = [
    ('A', 0, 30, 3),
    ('B', 10, 20, 5),
    ('C', 15, 40, 2),
    ('D', 20, 15, 4)
]

fcfs_patients = fcfs(patients.copy())
sjf_patients = sjf(patients.copy())
ps_patients = ps(patients.copy())

# Calculate and print average waiting time for FCFS, SJF, and PS
avg_waiting_time_fcfs = sum(p[1] for p in fcfs_patients) / len(fcfs_patients)
avg_waiting_time_sjf = sum(p[1] for p in sjf_patients) / len(sjf_patients)
avg_waiting_time_ps = sum(p[1] for p in ps_patients) / len(ps_patients)

# Calculate and print average turnaround time for FCFS, SJF, and PS
avg_turnaround_time_fcfs = sum(p[2] for p in fcfs_patients) / len(fcfs_patients)
avg_turnaround_time_sjf = sum(p[2] for p in sjf_patients) / len(sjf_patients)
avg_turnaround_time_ps = sum(p[2] for p in ps_patients) / len(ps_patients)

# Print results including waiting time and turnaround time for FCFS, SJF, and PS
print('FCFS:')
for patient in fcfs_patients:
    print(f'{patient[0]} - WT: {patient[1]}, TT: {patient[2]}')
print(f'Average WT (FCFS): {avg_waiting_time_fcfs}')
print(f'Average TT (FCFS): {avg_turnaround_time_fcfs}')
print()

print('SJF:')
for patient in sjf_patients:
    print(f'{patient[0]} - WT: {patient[1]}, TT: {patient[2]}')
print(f'Average WT (SJF): {avg_waiting_time_sjf}')
print(f'Average TT (SJF): {avg_turnaround_time_sjf}')
print()

print('PS:')
for patient in ps_patients:
    print(f'{patient[0]} - WT: {patient[1]}, TT: {patient[2]}')
print(f'Average WT (PS): {avg_waiting_time_ps}')
print(f'Average TT (PS): {avg_turnaround_time_ps}')
print()
