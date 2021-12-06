import pandas as pd
import numpy as np
import json

import CNN_OS as cnnos

df = pd.read_json('process.json')

df = pd.DataFrame(df)

class fcfs:
    def __init__(self):
        self.processes = df['process_id']
        self.bt = df['burst']
        self.at = df['arrival']
        self.n = len(df['process_id'])
    
    def findWaitingTime(processes, n, bt, wt, at):
        service_time = [0] * n
        service_time[0] = 0
        wt[0] = 0

        for i in range(1, n):
            service_time[i] = (service_time[i - 1] + bt[i - 1])
            wt[i] = service_time[i] - at[i]

            if (wt[i] < 0):
                wt[i] = 0
    
    def findTurnAroundTime(processes, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def findavgTime(processes, n, bt, at):
        wt = [0] * n
        tat = [0] * n

        fcfs.findWaitingTime(processes, n, bt, wt, at)
        fcfs.findTurnAroundTime(processes, n, bt, wt, tat)

        total_wt = 0
        total_tat = 0
        for i in range(n):
    
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            compl_time = tat[i] + at[i]
    
        avg_wt = round(total_wt/n, 2)
        avg_tat = round(total_tat/n, 2)
        avg_comp = round(compl_time/n, 2)

        return avg_wt, avg_tat, avg_comp

proc_fcfs = fcfs()
fcfs_avg_wt, fcfs_avg_tat, fcfs_comp = proc_fcfs.findavgTime(proc_fcfs.n, proc_fcfs.bt, proc_fcfs.at)
# print("FCFS")
# print(avg_wt, '\n', avg_tat, '\n', avg_comp)
# print("------------\n\n")

class sjfnp:

    def arrangeArrival(n, array):
        for i in range(0, n):
            for j in range(i, n-i-1):
                if array[1][j] > array[1][j+1]:
                    for k in range(0, n):
                        array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
    
    
    def CompletionTime(n, array):
        value = 0
        array[3][0] = array[1][0] + array[2][0]
        array[5][0] = array[3][0] - array[1][0]
        array[4][0] = array[5][0] - array[2][0]
        for i in range(1, n):
            temp = array[3][i-1]
            mini = array[2][i]
            for j in range(i, n):
                if temp >= array[1][j] and mini >= array[2][j]:
                    mini = array[2][j]
                    value = j
            array[3][value] = temp + array[2][value]
            array[5][value] = array[3][value] - array[1][value]
            array[4][value] = array[5][value] - array[2][value]
            for k in range(0, 6):
                array[k][value], array[k][i] = array[k][i], array[k][value]
    
    def calc():
        n = len(df['process_id'])
        proc_i = df['process_id']
        ar = df['arrival']
        br = df['burst']
        proc_id = []
        art = []
        brt = []
        for i in range(len(proc_i)):
            proc_id.append(proc_i[i])
            art.append(ar[i])
            brt.append(br[i])
        
        arr = [proc_id, art, brt, [0]*n, [0]*n, [0]*n]
        sjfnp.arrangeArrival(n, arr)
        sjfnp.CompletionTime(n, arr)
        waitingtime = 0
        turaroundtime = 0
        # completiontime = 0
        for i in range(0, n):
            # completiontime += arr[3][i] 
            waitingtime += arr[4][i]
            turaroundtime += arr[5][i]
        
        # print("Average waiting time is ", round((waitingtime/n), 2))
        sjfnp_avg_wt = round((waitingtime/n), 2)
        # print("Average Turnaround Time is  ", (turaroundtime/n))
        sjfnp_tat = round((turaroundtime/n), 2)
        # print("Average Completion Time is  ", (completiontime/n))
        # sjfnp_comp = round((completiontime/n), 2)
        return sjfnp_avg_wt, sjfnp_tat

# res_sjfnp = sjfnp()
# print("SJF - NP")
sjfnp_avg_wt, sjfnp_avg_tat = sjfnp.calc()
# print("------------\n\n")

class sjfp:
    def findWaitingTime(processes, n, wt):
        proc = processes
        rt = [0] * n
        for i in range(n):
            rt[i] = processes[i][1]
            complete = 0
            t = 0
            minm = 999999999
            short = 0
            check = False

        while (complete != n):
            for j in range(n):
                if ((processes[j][2] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue

            rt[short] -= 1

            minm = rt[short]
            if (minm == 0):
                minm = 999999999

            if (rt[short] == 0):
                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - proc[short][1] - proc[short][2])
    
                if (wt[short] < 0):
                    wt[short] = 0
            
            # Increment time
            t += 1
    
    def findTurnAroundTime(processes, n, wt, tat):
        for i in range(n):
            tat[i] = processes[i][1] + wt[i]

    def display():
        process_id = df['process_id']
        burst = df['burst']
        arrival = df['arrival']
        total_p_no = len(process_id)
        proc = []
        for i in range(total_p_no):
            pid, brt, art = process_id[i], burst[i], arrival[i]
            proc.append([pid, brt, art])
        # print(proc)
        wt = [0] * total_p_no
        tat = [0] * total_p_no
        sjfp.findWaitingTime(proc, total_p_no, wt)
        sjfp.findTurnAroundTime(proc, total_p_no, wt, tat)
        total_wt = 0
        total_tat = 0
        for i in range(total_p_no):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
        # print(proc.sort)
        # print(total_p_no)
        # print("\nAverage waiting time = %.5f "%(total_wt /total_p_no))
        sjfp_avg_wt = round((total_wt /total_p_no), 2)
        # print("Average turn around time = ", total_tat /total_p_no)
        sjfp_avg_tat = round((total_tat /total_p_no), 2)
        return sjfp_avg_wt, sjfp_avg_tat

# print("SJF - P")
sjfp_avg_wt, sjfp_avg_tat = sjfp.display()
# print("------------\n\n")

class rr:
    def calc(time_quantum):
        process_id = df['process_id']
        burst = df['burst']
        arrival = df['arrival']
        total_p_no = len(process_id)
        total_time = 0
        total_time_counted = 0
        proc = []
        wait_time = 0
        turnaround_time = 0
        for i in range(total_p_no):
            art, brt, remaining_time = arrival[i], burst[i], burst[i]
            proc.append([art, brt, remaining_time, 0])
            total_time += brt
        
        while total_time != 0:
            for i in range(len(proc)):
                if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                    total_time_counted += proc[i][2]
                    total_time -= proc[i][2]
                    proc[i][2] = 0
                elif proc[i][2] > 0:
                    proc[i][2] -= time_quantum
                    total_time -= time_quantum
                    total_time_counted += time_quantum
                if proc[i][2] == 0 and proc[i][3] != 1:
                    wait_time += total_time_counted - proc[i][0] - proc[i][1]
                    turnaround_time += total_time_counted - proc[i][0]
                    proc[i][3] = 1
        
        # print("Average waiting time is : ", end = " ")
        # print(wait_time/total_p_no)
        rr_avg_wt = round((wait_time/total_p_no), 2)
        # print("average turnaround time : " , end = " ")
        # print(turnaround_time/total_p_no)
        rr_avg_tat = round((turnaround_time/total_p_no), 2)
        return rr_avg_wt, rr_avg_tat


# print("RR - quantum 1")
rr_avg_wt_q1, rr_avg_tat_q1 = rr.calc(1)
# print("RR - quantum 2")
rr_avg_wt_q2, rr_avg_tat_q2 = rr.calc(2)
# print("------------\n\n")

class priorityNP:

    def get_wt_time(wt, totalprocess, proc):
        service = [0] * totalprocess
        service[0] = 0
        wt[0] = 0
        for i in range(1, totalprocess):
            service[i] = proc[i - 1][1] + service[i - 1]
            wt[i] = service[i] - proc[i][0] + 1
            if(wt[i] < 0) :    
                wt[i] = 0
    
    def get_tat_time(tat, wt, totalprocess, proc):
        for i in range(totalprocess):
            tat[i] = proc[i][1] + wt[i]
    
    def calc():
        process_id = df['process_id']
        burst = df['burst']
        arrival = df['arrival']
        pr = df['priority']
        totalprocess = len(df['process_id'])
        proc = []
        for i in range(totalprocess):
            l = []
            for j in range(4):
                l.append(0)
            proc.append(l)
        
        for i in range(totalprocess):
            proc[i][0] = arrival[i]
            proc[i][1] = burst[i]
            proc[i][2] = pr[i]
            proc[i][3] = process_id[i]
        
        proc = sorted (proc, key = lambda x:x[2])
        proc = sorted (proc)
        wt = [0] * totalprocess
        tat = [0] * totalprocess
        wavg = 0
        tavg = 0
        cavg = 0
        priorityNP.get_wt_time(wt, totalprocess, proc)
        priorityNP.get_tat_time(tat, wt, totalprocess, proc)
        stime = [0] * totalprocess
        ctime = [0] * totalprocess
        stime[0] = 1
        ctime[0] = stime[0] + tat[0]
        
        # calculating starting and ending time
        for i in range(1, totalprocess):
            stime[i] = ctime[i - 1]
            ctime[i] = stime[i] + tat[i] - wt[i]
    
        # display the process details
        for i in range(totalprocess):
            wavg += wt[i]
            tavg += tat[i]
            cavg += ctime[i]
        # display the average waiting time
        # and average turn around time
        # print("Average waiting time is : ", end = " ")
        # print(wavg / totalprocess)
        prt_avg_wt = round((wavg / totalprocess), 2)
        # print("average turnaround time : " , end = " ")
        # print(tavg / totalprocess)
        prt_avg_tat = round((tavg / totalprocess), 2)
        # print("average completion time : " , end = " ")
        # print(cavg / totalprocess)
        prt_avg_ct = round((cavg / totalprocess), 2)
        return prt_avg_wt, prt_avg_tat, prt_avg_ct

# print("Priority")
prtnp_avg_wt, prtnp_avg_tat, prtnp_avg_ct = priorityNP.calc()
# print("------------\n\n")

class priorityP:
    def calc():
        process_data = []
        n = len(df['process_id'])
        proc_i = df['process_id']
        ar = df['arrival']
        br = df['burst']
        pr = df['priority']
        proc_id = []
        art = []
        brt = []
        prt = []
        for i in range(len(proc_i)):
            proc_id.append(proc_i[i])
            art.append(ar[i])
            brt.append(br[i])
            prt.append(pr[i])
        
        for i in range(n):
            temporary = []
            temporary.extend([proc_id[i], art[i], brt[i], prt[i], 0, brt[i]])
            process_data.append(temporary)
        
        t_time, w_time = priorityP.schedulingProcess(process_data)
        return t_time, w_time
    
    def schedulingProcess(process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
        
        t_time = priorityP.calculateTurnaroundTime(process_data)
        w_time = priorityP.calculateWaitingTime(process_data)
        t_time = round(t_time/2, 2)
        w_time = round(w_time/2, 2)
        return t_time, w_time

    def calculateTurnaroundTime(process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][6] - process_data[i][5]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time
    
    def calculateWaitingTime(process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time
    
prtp_avg_wt, prtp_avg_tat = priorityP.calc()

avg_wt = []
avg_tat = []
# prtp_avg_wt = 0
# prtp_avg_tat = 0
our_avg_wt = cnnos.avg_wait_cnn
our_avg_tat = cnnos.avg_tat_cnn
avg_wt.append([fcfs_avg_wt, sjfnp_avg_wt, sjfp_avg_wt, rr_avg_wt_q1, rr_avg_wt_q2, prtnp_avg_wt, prtp_avg_wt, our_avg_wt])
avg_tat.append([fcfs_avg_tat, sjfnp_avg_tat, sjfp_avg_tat, rr_avg_tat_q1, rr_avg_tat_q2, prtnp_avg_tat, prtp_avg_tat, our_avg_tat])

avg_wt = avg_wt[0]
avg_tat = avg_tat[0]

# print(avg_wt)
# print(avg_tat)
names = ['FCFS', 'SJF (NP)', 'SJF (P)', 'RR Q=1', 'RR Q=2', 'Priority (NP)', 'Priority (P)', 'CPU_CNN']
dfa = pd.DataFrame(list(zip(names, avg_wt, avg_tat)), columns =['algo', 'avg_wait', 'avg_tat'], index=None)
# print(dfa)
res = dfa.to_json(orient="records")
parsed = json.loads(res)
# print(json.dumps(parsed, indent=4))
with open("calc_res.json", "w") as file:
    json.dump(parsed, file, indent=4)

seq_of_procs = cnnos.l
dfa = pd.DataFrame(list(zip(seq_of_procs)), columns =['procs'], index=None)
# print(dfa)
res = dfa.to_json(orient="records")
parsed = json.loads(res)
# print(json.dumps(parsed, indent=4))
with open("sequence.json", "w") as file:
    json.dump(parsed, file, indent=4)