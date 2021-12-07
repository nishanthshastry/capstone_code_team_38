import pandas as pd
import json

procs = 12
proc_1 = []
for i in range(1, procs+1):
    proc_1.append(i)

arr_1 = [1,1,2,3,4,5,6,7,8,9,10,11]
# arr_1 = [1,11,2,3,4,5,6,7,8,9,10,1]
burt_1 = [3,2,1,3,2,3,2,1,3,3,2,2]
# burt_1 = [10,2,2,6,7,9,2,9,3,6,3,2]
prt_1 = [3,2,1,5,4,6,8,9,7,10,11,12]
# prt_1 = [4,12,1,5,3,8,6,9,7,11,10,2]

dfa = pd.DataFrame(list(zip(proc_1, arr_1, burt_1, prt_1)), columns =['process_id', 'arrival', 'burst', 'priority'], index=None)
# print(dfa)
res = dfa.to_json(orient="records")
parsed = json.loads(res)
# print(json.dumps(parsed, indent=4))
with open("process.json", "w") as file:
    json.dump(parsed, file, indent=4)


df = pd.read_json('process.json')

df = pd.DataFrame(df)

procl = df['process_id']
arrl = df['process_id']
brtl = df['burst']
prtl = df['priority']

list_0 = []
list_1 = []
list_2 = []
list_3 = []

for i in range(len(procl)):
    list_0.append(procl[i])
    list_1.append(arrl[i])
    list_2.append(brtl[i])
    list_3.append(prtl[i])

# print(list_1, '\n', list_2, '\n', list_3)

arrt = []
brt = []
prt = []

for i in range(len(list_1)):
    arrt.append([procl[i], list_1[i]])
    brt.append([procl[i], list_2[i]])
    prt.append([procl[i], list_3[i]])

# print(arrt, '\n', brt, '\n', prt)

def make_channel(channel, arr):
    
    # channel = the required channel to be created - arrival, burst & priority respectively
    # arr = the input values from - arrt, brt & prt respectively
    
    channel = []
    channel = [arr[i:i + 3] for i in range(0, len(arr), 3)]
    
    return channel

arrival_time_channel = []
burst_time_channel = []
priority_channel = []

arrival_time_channel = make_channel(arrival_time_channel, arrt)
burst_time_channel = make_channel(burst_time_channel, brt)
priority_channel = make_channel(priority_channel, prt)

# print(arrival_time_channel)
# print(burst_time_channel)
# print(priority_channel)

l=[]
n=1

# print("The first hidden layer in the Network is a MinPool Layer")

while(n<len(procl)+1):
        
        print("Input Arrival Time Channel is:\n")

        for i in range(4):
            print(arrival_time_channel[i])
        ###
        # range is exclusive of the last number

        # print('Arrival Time Channel would be split up into the following parts while pooling:')
        print()

        ######
        # for i in range(0,3):
        #     for j in range(0,2):
        #         print(arrival_time_channel[i][j]," ",arrival_time_channel[i][j+1])
        #         print(arrival_time_channel[i+1][j]," ",arrival_time_channel[i+1][j+1])
        #         print()


        min_pool_layer_1_channel_1 = []

        for i in range(3):
            min_pool_layer_1_channel_1.append([])

        temp_2=[0,0]

        for i in range(0,3):
            for j in range(0,2):
                temp_list_1 = []
                temp_list_1.append(arrival_time_channel[i][j])
                temp_list_1.append(arrival_time_channel[i][j+1])
                temp_list_1.append(arrival_time_channel[i+1][j])
                temp_list_1.append(arrival_time_channel[i+1][j+1])


                min = 9999

                for k in temp_list_1:
                    if(k[1] < min and k[1]!=0 ):
                        min = k[1]
                        temp_2 = k
                min_pool_layer_1_channel_1[i].append(temp_2)        


        # This kernel picked the first arrived process in each of the blocks it worked on, the output supports the cause
        # of reducing the waiting time, because it picks the earliest arrived processes.

        ###
        # print("The resulting channel after Min Pooling is:")
        # print()
        # print("This step supports the cause of reducing the waiting time")
        # print()

        # print()
        # print("min_pool_layer_1_channel_1 created now is:")
        # print()
        # for i in range(3):
        #     print(min_pool_layer_1_channel_1[i])

        ###
        print("Input Burst Time Channel is:\n")

        for i in range(4):
            print(burst_time_channel[i])

        ###
        # print("The following parts of the Burst Time Channel will be considered for operation by the 1st MinPool layer")
        print()

        # for i in range(3):
        #     for j in range(2):
        #         print(burst_time_channel[i][j]," ",burst_time_channel[i][j+1])
        #         print(burst_time_channel[i+1][j]," ",burst_time_channel[i+1][j+1])
        #         print()

        ###
        min_pool_layer_1_channel_2 = []

        for i in range(3):
            min_pool_layer_1_channel_2.append([])
            
        temp_2=[0,0]
        for i in range(3):
            for j in range(2):
                temp_list_1 = []
                temp_list_1.append(burst_time_channel[i][j])
                temp_list_1.append(burst_time_channel[i][j+1])
                temp_list_1.append(burst_time_channel[i+1][j])
                temp_list_1.append(burst_time_channel[i+1][j+1])

                min = 9999

                for k in temp_list_1:
                    if(k[1] < min and k[1]!=0 ):
                        min = k[1]
                        temp_2 = k
                min_pool_layer_1_channel_2[i].append(temp_2)

        ###
        # print("The input Burst Time Channel was MinPooled \n")
        # print("The resulting channel 2 in the 1st MinPool Layer is: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_2[i])

        ###
        print("Input priority channel is:\n")

        for i in range(4):
            print(priority_channel[i])

        ###
        # print('The following parts of the Priority Channel will be considered for Min Pooling:')
        print()

        # for i in range(0,3):
        #     for j in range(0,2):
        #         print(priority_channel[i][j]," ",priority_channel[i][j+1])
        #         print(priority_channel[i+1][j]," ",priority_channel[i+1][j+1])
        #         print()

        ###
        min_pool_layer_1_channel_3 = []

        for i in range(3):
            min_pool_layer_1_channel_3.append([])

        temp_2=[0,0]
        for i in range(3):
            for j in range(2):
                temp_list_1 = []
                temp_list_1.append(priority_channel[i][j])
                temp_list_1.append(priority_channel[i][j+1])
                temp_list_1.append(priority_channel[i+1][j])
                temp_list_1.append(priority_channel[i+1][j+1])

                min = 9999
                c=0
                for k in temp_list_1:
                    if(k[1] < min and k[1]!=0 ):
                        min = k[1]
                        temp_2 = k
                        c=1
                if(c==0):
                    f=[0,0]
                    min_pool_layer_1_channel_3[i].append(f)
                else:
                    min_pool_layer_1_channel_3[i].append(temp_2)

        ###
        # print("The input Priority Channel was Min Pooled\n")
        # print("It supports the cause of selecting the processes with higher (lower numerically) priority value")

        # print()

        # print("min_pool_layer_1_channel_2 created now is: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_3[i])

        # ###
        # print("Manipulated channel of the input Arrival Time Channel: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_1[i])

        ###
        # print("Manipulated channel of the input Burst Time Channel: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_2[i])

        # ###
        # print("Manipulated channel of the input Priority Channel: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_3[i])

        # ###
        # print("3 channels are present at the input to the 1st Convolutional layer")

        # ###
        # print("Each Kernel applied in convolutional layer 1 will span across all the 3 channels")

        # ###
        # print("Kernels in the 1st convolutional layer are designed to assign different importance to the Kernels")

        # ###
        # print("3 Kernels are used in this layer")

        # ###
        # print("The 1st Kernel looks like:")

        # print("1 1    0 0    0 0 \n1 1    0 0    0 0 \n1 1    0 0    0 0")

        # ###
        # print("The 2nd Kernel looks like:")

        # print("0 0    1 1    0 0 \n0 0    1 1    0 0 \n0 0    1 1    0 0")

        # ###
        # print("The 3rd Kernel looks like:")

        # print("0 0    0 0    2 2 \n0 0    0 0    2 2 \n0 0    0 0    2 2")

        ###
        conv_layer_1_kernel_1 = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 

        conv_layer_1_channel_1 = []

        for i in range(3):
            conv_layer_1_channel_1.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (min_pool_layer_1_channel_1[i][j][1] * conv_layer_1_kernel_1[0][counter]) + (min_pool_layer_1_channel_2[i][j][1] * conv_layer_1_kernel_1[1][counter]) + (min_pool_layer_1_channel_3[i][j][1] * conv_layer_1_kernel_1[2][counter])
                temp_1 = [min_pool_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_1_channel_1[i].append(temp_1)

        print(conv_layer_1_channel_1)

        ###
        # print("conv_layer_1_channel_1 was formed after applying the above mentioned kernel 1 :\n")

        # for i in range(3):
        #     print(conv_layer_1_channel_1[i])

        ###
        conv_layer_1_kernel_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] 

        conv_layer_1_channel_2 = []

        for i in range(3):
            conv_layer_1_channel_2.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (min_pool_layer_1_channel_1[i][j][1] * conv_layer_1_kernel_2[0][counter]) + (min_pool_layer_1_channel_2[i][j][1] * conv_layer_1_kernel_2[1][counter]) + (min_pool_layer_1_channel_3[i][j][1] * conv_layer_1_kernel_2[2][counter])
                temp_1 = [min_pool_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_1_channel_2[i].append(temp_1)

        # print(conv_layer_1_channel_2)

        ###
        # print("conv_layer_1_channel_2 was formed after applying the above mentioned kernel 2 :\n")

        # for i in range(3):
        #     print(conv_layer_1_channel_2[i])

        ###
        conv_layer_1_kernel_3 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [2, 2, 2, 2, 2, 2]] 

        conv_layer_1_channel_3 = []

        for i in range(3):
            conv_layer_1_channel_3.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (min_pool_layer_1_channel_1[i][j][1] * conv_layer_1_kernel_3[0][counter]) + (min_pool_layer_1_channel_2[i][j][1] * conv_layer_1_kernel_3[1][counter]) + (min_pool_layer_1_channel_3[i][j][1] * conv_layer_1_kernel_3[2][counter])
                temp_1 = [min_pool_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_1_channel_3[i].append(temp_1)

        # print(conv_layer_1_channel_3)

        ###
        # print("conv_layer_1_channel_3 was formed after applying the above mentioned kernel 3 :\n")

        # print("Notice that all the values of min_pool_layer_1_channel_3 are multiplied by 2\n")

        # for i in range(3):
        #     print(conv_layer_1_channel_3[i])

        # ###
        # print("Inputs to convolutional layer 1 was: \n")

        # for i in range(3):
        #     print(min_pool_layer_1_channel_1[i], "\t", min_pool_layer_1_channel_2[i], "\t", min_pool_layer_1_channel_3[i] )

        # ###
        # print("This kernel weighted the different properties")

        # ###
        # print("Here, the weighting was done in 1:1:2 ratio")

        # ###
        # print("The values in this ratio could be changed to get better accuracy of the scheduler ")

        # ###
        # print("The above layer was an example of the use of FEATURE EXTRACTION KERNELS")

        # ###
        # print("The inputs in the burst time channel are maintained in a sorted fashion ")

        # ###
        # print("To trade off between long and short processes, we need a kernel like: \n")

        # print("0 0")
        # print("5 0")
        # print("0 0")

        # print("\nGiven the processes are in ascending order, this kernel picks the median process")

        # ###
        # print("This will also help all the processes get a FAIR SHARE OF CPU TIME, as long processes are not allowed to occupy the CPU for long intervals of time")

        # ###
        # print("The number 5 could be changed, the number should be selected such that the overall accuracy is the best")

        # ###
        # print("5 is used instead of 1 to emphasize the importance of the process")

        # ###
        # print("In convolutional layer 2 we'll change only the burst time channel")

        ###
        conv_layer_2_kernel_1 = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 

        conv_layer_2_channel_1 = []

        for i in range(3):
            conv_layer_2_channel_1.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (conv_layer_1_channel_1[i][j][1] * conv_layer_2_kernel_1[0][counter]) + (conv_layer_1_channel_2[i][j][1] * conv_layer_2_kernel_1[1][counter]) + (conv_layer_1_channel_3[i][j][1] * conv_layer_2_kernel_1[2][counter])
                temp_1 = [conv_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_2_channel_1[i].append(temp_1)

        # print(conv_layer_2_channel_1)

        ###
        conv_layer_2_kernel_2 = [[0, 0, 0, 0, 0, 0], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 

        conv_layer_2_channel_2 = []

        for i in range(3):
            conv_layer_2_channel_2.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (conv_layer_1_channel_1[i][j][1] * conv_layer_2_kernel_2[0][counter]) + (conv_layer_1_channel_2[i][j][1] * conv_layer_2_kernel_2[1][counter]) + (conv_layer_1_channel_3[i][j][1] * conv_layer_2_kernel_2[2][counter])
                temp_1 = [conv_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_2_channel_2[i].append(temp_1)

        # print(conv_layer_2_channel_2)

        ###
        conv_layer_2_kernel_3 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]] 

        conv_layer_2_channel_3 = []

        for i in range(3):
            conv_layer_2_channel_3.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (conv_layer_1_channel_1[i][j][1] * conv_layer_2_kernel_3[0][counter]) + (conv_layer_1_channel_2[i][j][1] * conv_layer_2_kernel_3[1][counter]) + (conv_layer_1_channel_3[i][j][1] * conv_layer_2_kernel_3[2][counter])
                temp_1 = [conv_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_2_channel_3[i].append(temp_1)

        # print(conv_layer_2_channel_3)

        ###

        # print("Outputs from convolutional layer 2 is: \n")

        # for i in range(3):
        #     print(conv_layer_2_channel_1[i], "\t", conv_layer_2_channel_2[i], "\t", conv_layer_2_channel_3[i] )

        # ###
        # print('Convolutional layer 3 is to merge all the layers')

        # ###
        # print("Kernel used for convolution layer 3 is:")

        # print("1 1    1 1    1 1 \n1 1    1 1    1 1 \n1 1    1 1    1 1")

        ###
        conv_layer_3_kernel_1 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]] 


        conv_layer_3_channel_1 = []

        for i in range(3):
            conv_layer_3_channel_1.append([])


        counter = 0

        for i in range(0, 3):
            for j in range(0, 2):

                temp_2 = (conv_layer_2_channel_1[i][j][1] * conv_layer_3_kernel_1[0][counter]) + (conv_layer_2_channel_2[i][j][1] * conv_layer_3_kernel_1[1][counter]) + (conv_layer_2_channel_3[i][j][1] * conv_layer_3_kernel_1[2][counter])
                temp_1 = [conv_layer_1_channel_1[i][j][0], temp_2]
                counter=counter+1

                conv_layer_3_channel_1[i].append(temp_1)

        # print(conv_layer_3_channel_1)

        ###
        # print("Outputs from convolutional layer 3 is: \n")
        l1=[]
        for i in range(3):
            # print(conv_layer_3_channel_1[i])
            l1.append(conv_layer_3_channel_1[i])


        ###
        conv_layer_3_channel_1

        ###
        min_pool_layer_2_channel_1 = []

        for i in range(2):
            min_pool_layer_2_channel_1.append([])


        for i in range(0, 2):
            for j in range(0, 1):
                temp_1 = []

                temp_1.append(conv_layer_3_channel_1[i][j])
                temp_1.append(conv_layer_3_channel_1[i][j+1])
                temp_1.append(conv_layer_3_channel_1[i+1][j])
                temp_1.append(conv_layer_3_channel_1[i+1][j+1])

                min = 9999

                for k in temp_1:
                    if(k[1] < min):
                        min = k[1]
                        temp_2 = k
                min_pool_layer_2_channel_1[i].append(temp_2)


        min_pool_layer_2_channel_1

        ###
        min_pool_layer_3_channel_1 = []

        mini = 9999

        for i in range(0, 2):
            if min_pool_layer_2_channel_1[i][0][1] < mini:
                mini = min_pool_layer_2_channel_1[i][0][1]
                temp_1 = min_pool_layer_2_channel_1[i][0]

        min_pool_layer_3_channel_1.append(temp_1)
        
        s1=[]
        minim=9999
        for i in range(len(l1)):
            for j in range(len(l1[0])):
                if l1[i][j][1]<minim and l1[i][j][1]!=0:
                    minim=l1[i][j][1]
                    t1=l1[i][j]
                  
        s1.append(t1)
        print("OUTPUT for this iteration:",s1)
        ###
        print("***************************************************************")
        print("\t\tCPU time is given to Process: ",s1[0][0])
        print("***************************************************************")

        x=s1[0][0]
        l.append(x)



        for i in range(len(arrival_time_channel)):
            for j in range(len(arrival_time_channel[i])):
                if arrival_time_channel[i][j][0]==x:
                    arrival_time_channel[i][j][0]=0
                    arrival_time_channel[i][j][1]=0
                    burst_time_channel[i][j][0]=0
                    burst_time_channel[i][j][1]=0
                    priority_channel[i][j][0]=0
                    priority_channel[i][j][1]=0
                    

        
        n+=1
        
print("CPU time is given to the process in this order:",l)


def findWaitingTime(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
 
    for i in range(1, n):
         
        service_time[i] = (service_time[i - 1] + bt[i - 1])
 
        wt[i] = service_time[i] - at[i]
 
    
        if (wt[i] < 0):
            wt[i] = 0
     
# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
     
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
 
def findavgTime(processes, n, bt, at):
    wt = [0] * n
    tat = [0] * n
 
    # Function to find waiting time
    # of all processes
    findWaitingTime(processes, n, bt, wt, at)
 
    # Function to find turn around time for
    # all processes
    findTurnAroundTime(processes, n, bt, wt, tat)
 
    # Display processes 
    print("Processes   Burst Time   Arrival Time     Waiting",
          "Time   Turn-Around Time  Completion Time \n")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],
              "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", compl_time)
 
    # print("Average waiting time = %.5f "%(total_wt /n))
    avg_wait_cnn = round((total_wt /n), 2)
    # print("\nAverage turn around time = ", total_tat / n)
    avg_tat_cnn = round((total_tat / n), 2)
    return avg_wait_cnn, avg_tat_cnn
 
     
processes = l
no_of_processes=len(processes)
 
# arrival = [1,1,2,3,4,5,6,7,8,9,10,11]
arrival = arr_1
# burst = [3,2,1,3,2,3,2,1,3,3,2,2]
burst = burt_1

avg_wait_cnn, avg_tat_cnn = findavgTime(processes, no_of_processes, burst, arrival)