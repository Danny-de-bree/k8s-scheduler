import time
import random
import json
import yaml

from kubernetes import client, config, watch

class scheduler_setup:
     
     def get_k8s_client(self):
         if config.load_incluster_config():
             return client.CoreV1Api()
         else:
             config.load_kube_config()
         v1 = client.CoreV1Api()
         return v1

     def nodes(self):
        node_labels = self.get_node_labels()
        ready_nodes = []
        for node in v1.list_node().items:
            node_name = node.metadata.name
        for status in node.status.conditions:
            if status.status == "True" and status.type == "Ready":
                if node_name in node_labels:
                    labels = node_labels[node_name]
                else:
                    print("Node %s is ready but has no labels" % node_name)
                ready_nodes.append((node_name, labels))
            return ready_nodes

##will add logic for taints and allocatable resources later

class filter_nodes:
    
     def get_node_list(self, label_name, label_value):
        node_labels = self.get_node_labels()
        matching_nodes = []
        for node_name, labels in node_labels.items():
            if label_name in labels and labels[label_name] == label_value:
                matching_nodes.append(node_name)
            return matching_nodes
        
class scheduler:

##use the matching_nodes list to select a node for the pod to be scheduled on and return the node name

     def schedule(self, matching_nodes):
            for matching_node in matching_nodes:
                
                print("Scheduling pod on node %s" % matching_node)
                return matching_node