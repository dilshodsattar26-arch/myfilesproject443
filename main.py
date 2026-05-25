import math
import os

class dbManagerEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [46, 36, 26, 10, 91, 1]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = dbManagerEngine(node_id=178)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")