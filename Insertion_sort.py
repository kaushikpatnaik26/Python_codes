def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(f"{' '.join(str(v) for v in data)}")
        print(f"{'---' * (i + 1)}") 
        # print(f"Step {i}: {' '.join(str(v) for v in data)}")
    
    print(f"Sorted data: {data}")
data = np.random.randint(1,50,10)
insertion_sort(data)
