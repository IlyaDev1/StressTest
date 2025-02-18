import multiprocessing
import time

import requests
from timer import wrapper
from datetime import datetime, timedelta


@wrapper
def requester() -> None:
    requests.get('http://localhost:8080/api/v1/task')


def client(result_dict, process_id) -> None:
    end_time = datetime.now() + timedelta(seconds=20)
    counter = 0
    total_time = timedelta()
    while datetime.now() < end_time:
        total_time += requester()
        counter += 1
    result_dict[process_id] = (counter, total_time)


def main():
    processes = []
    manager = multiprocessing.Manager()
    result_dict = manager.dict()
    for i in range(10):
        process = multiprocessing.Process(target=client, args=(result_dict, i))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_requests = sum(data[0] for data in result_dict.values())
    total_execution_time = sum((data[1] for data in result_dict.values()), timedelta())

    print(f"Общее количество запросов: {total_requests}")
    print(f"Суммарное время выполнения: {total_execution_time}")


if __name__ == '__main__':
    main()
