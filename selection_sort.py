import numpy as np

def selection_sort(data):
    for i in range(len(data) - 1):        
        minpos = i
        for j in range(i + 1, len(data)):
            if data[j] < data[minpos]:
                minpos = j
        print(f"{' '.join(str(v) for v in data)}")
        print(f"{'---' * (i + 1)}") 
        
        data[i], data[minpos] = data[minpos], data[i]

    print(f"Sorted data: {data}")

data = np.random.randint(1, 50, 15)
selection_sort(data)
