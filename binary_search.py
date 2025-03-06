#BINARY.PY
import numpy as np
def binary_search(data,key):
        low = 0
        high = len(data)-1
        mid = (low + high +1)//2
        location = -1
        while low <= high and location == -1:
            if key == data[mid]:
                location = mid
            elif key < data[mid]:
                high = mid -1
            else: 
                low = mid + 1
            mid = (low + high + 1)//2
        return location 
        
def main():
        data = np.random.randint(11,101,10)
        data.sort()
        print(f"Unsorted Data : {data}")
        key = int(input("Enter a key u want to locate (-1 to quit): "))
        while key != -1:
            loc = binary_search(data,key)
            if loc != -1:
                print(f"Key {key} is located at pos {loc +1}")
            else:
                print(f"Key {key} is not in the list")
            key = int(input("Enter a key u want to locate (-1 to quit): "))
if __name__ == "__main__":
    main()
            
                            


        
        
