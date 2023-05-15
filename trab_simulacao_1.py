#%% imports
import random
import heapq

#%% simulador 1
def simulador_1(var_lambda, var_mi):
    n = 0
    simultime = 0
    total_waiting_time = 0
    arrival_count = 0
    total_clients = 0
    
    for i in range(1, 41):
        sample_arrival = random.expovariate(var_lambda)
        sample_departure = random.expovariate(1 / var_mi)
        
        if n == 0:
            simultime += sample_arrival
            print(f'{simultime:08.4f} {"arrival":10s} {n}=>{n+1}')
            n += 1
        else:
            if sample_arrival < sample_departure:
                simultime += sample_arrival
                total_waiting_time += simultime
                arrival_count += 1
                print(f'{simultime:08.4f} {"arrival":10s} {n}=>{n+1}')
                n += 1
            else:
                simultime += sample_departure
                print(f'{simultime:08.4f} {"departure":10s} {n}=>{n-1}')
                n -= 1
        
        total_clients += n
    
    avg_waiting_time = total_waiting_time / arrival_count if arrival_count > 0 else 0
    avg_clients = total_clients / 40
    
    print(f'\nAverage Arrival Waiting Time: {avg_waiting_time:.4f}')
    print(f'Average Number of Clients in the System: {avg_clients:.2f}')

#%% simulador 2
def simulador_2(var_lambda, var_mi):
    n = 0
    random.seed(1)
    simultime = 0

    ARRIVAL = 1
    DEPARTURE = 2

    eventqueue = []
    heapq.heapify(eventqueue)

    def add_event(time, event_type):
        heapq.heappush(eventqueue, (time, event_type))

    def get_next_event():
        return heapq.heappop(eventqueue)

    add_event(random.expovariate(1), ARRIVAL)

    iteration = 1
    max_iterations = 100

    while eventqueue and iteration <= max_iterations:
        current_event_time, current_event_type = get_next_event()

        simultime = current_event_time

        if current_event_type == ARRIVAL:
            print(f'{simultime:08.4f} {"arrival":10s} {n}=>{n+1}')
            n += 1

            time_next_arrival = random.expovariate(var_lambda)

            if not eventqueue:
                time_next_service = random.expovariate(1/var_mi)

                if time_next_arrival < time_next_service:
                    add_event(simultime + time_next_service, DEPARTURE)
                    add_event(simultime + time_next_arrival, ARRIVAL)
                else:
                    add_event(simultime + time_next_arrival, ARRIVAL)
                    add_event(simultime + time_next_service, DEPARTURE)
            elif eventqueue[0][0] > simultime + time_next_arrival:
                add_event(simultime + time_next_arrival, ARRIVAL)
            else:
                add_event(simultime + time_next_arrival, ARRIVAL)

        else:
            print(f'{simultime:08.4f} {"departure":10s} {n}=>{n-1}')
            n -= 1

            if n > 0:
                time_next_service = random.expovariate(0.5)

                if eventqueue[0][0] < simultime + time_next_service:
                    add_event(simultime + time_next_service, DEPARTURE)
                else:
                    add_event(simultime + time_next_service, DEPARTURE)
                    heapq.heappush(eventqueue, (simultime + time_next_service, DEPARTURE))

        iteration += 1
        
        if n == 0:
            break

#%% simulador_2_deterministico
def simulador_2_deterministico(var_lambda, var_mi):
    n = 0
    random.seed(1)
    simultime = 0

    ARRIVAL = 1
    DEPARTURE = 2

    eventqueue = []
    heapq.heapify(eventqueue)

    def add_event(time, event_type):
        heapq.heappush(eventqueue, (time, event_type))

    def get_next_event():
        return heapq.heappop(eventqueue)

    add_event(random.expovariate(1), ARRIVAL)

    iteration = 1
    max_iterations = 100

    while eventqueue and iteration <= max_iterations:
        current_event_time, current_event_type = get_next_event()

        simultime = current_event_time

        if current_event_type == ARRIVAL:
            print(f'{simultime:08.4f} {"arrival":10s} {n}=>{n+1}')
            n += 1

            time_next_arrival = random.expovariate(var_lambda)

            if not eventqueue:
                time_next_service = random.expovariate(var_mi)

                if time_next_arrival < time_next_service:
                    add_event(simultime + time_next_service, DEPARTURE)
                    add_event(simultime + time_next_arrival, ARRIVAL)
                else:
                    add_event(simultime + time_next_arrival, ARRIVAL)
                    add_event(simultime + time_next_service, DEPARTURE)
            elif eventqueue[0][0] > simultime + time_next_arrival:
                add_event(simultime + time_next_arrival, ARRIVAL)
            else:
                add_event(simultime + time_next_arrival, ARRIVAL)

        else:
            print(f'{simultime:08.4f} {"departure":10s} {n}=>{n-1}')
            n -= 1

            if n > 0:
                time_next_service = random.expovariate(0.5)

                if eventqueue[0][0] < simultime + time_next_service:
                    add_event(simultime + time_next_service, DEPARTURE)
                else:
                    add_event(simultime + time_next_service, DEPARTURE)
                    heapq.heappush(eventqueue, (simultime + time_next_service, DEPARTURE))

        iteration += 1
        
        if n == 0:
            break



#%% execuçoes
# =============================================================================
# simulador_1(1, 2)
# simulador_1(2, 4)
# simulador_1(1, 4)
# 
# 
# simulador_2(1, 2)
# simulador_2(2, 4)
# simulador_2(1, 4)
# 
# simulador_2_deterministico(var_lambda, var_mi)
# 
# =============================================================================

