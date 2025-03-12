from prometheus_api_client import PrometheusConnect
import csv
import datetime

import os
from dotenv import load_dotenv

load_dotenv()

prometheus_url = os.getenv("PROMETHEUS_URL")
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
data_file_path_name = f"data/prometheus_data_{current_time}.csv"

prom = PrometheusConnect(url=prometheus_url, disable_ssl=True)

usage = []
column_name = [
                "timestamp",
                "cpu_usage",
                "gpu_usage",
                "memory_usage",
                "pod_name",
                "instance", 
                "node_name",
                "namespace",
                "kubernetes_io_arch",
                "kubernetes_io_os"
              ]

for i in range(10):
    jupyter_pod_name = f"test-{i+1}-0"

    # CPU
    cpu_query = f'rate(container_cpu_usage_seconds_total{{pod=\"{jupyter_pod_name}\", namespace=\"kubeflow-user-example-com\"}}[5m])'
    total_cpu_query = 'count(node_cpu_seconds_total)-count(node_cpu_seconds_total{mode="idle"})'

    cpu_usage_data = prom.custom_query(query=cpu_query)
    total_cpu = prom.custom_query(query=total_cpu_query)

    # Memory
    memory_query = f'rate(container_memory_usage_bytes{{pod=\"{jupyter_pod_name}\", namespace=\"kubeflow-user-example-com\"}}[5m])'
    total_memory_query = 'node_memory_MemTotal_bytes'

    memory_usage_data = prom.custom_query(query=memory_query)
    total_memory = prom.custom_query(query=total_memory_query)
    
    # GPU
    gpu_query = ""

    try :       
        usage.append([
            datetime.datetime.fromtimestamp(cpu_usage_data[0]['value'][0]).strftime("%Y%m%d%H%M%S"), # Timestamp
            (float(cpu_usage_data[0]['value'][1]) / float(total_cpu[0]['value'][1])) * 100, # CPU Usage ( Pod cpu usage / total cpu usage * 100 )
            (float(memory_usage_data[0]['value'][1]) / (float(test[0]['value'][1]) * 1024 * 1024 * 1024)) * 100, # Memory Usage ( Pod mem usage / total mem usage * 100 )
            # TODO: GPU Usage
            "",
            cpu_usage_data[0]['metric']['pod'], # Pod Name
            cpu_usage_data[0]['metric']['instance'], # Node Name
            cpu_usage_data[0]['metric']['namespace'], # Namespace
            cpu_usage_data[0]['metric']['kubernetes_io_arch'], # K8S I/O architecture
            cpu_usage_data[0]['metric']['kubernetes_io_os'], # K8S I/O OS
        ])
    except :
        pass