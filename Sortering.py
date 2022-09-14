
array = [3,5,6,6,3,5,7,9,0,0,2,4,3,9,53,1]
"[1,3,4,6,7]"


def selectionSort(temparray):
    array = temparray.copy()
    antall = len(array)
    outputArray = []

    while len(outputArray) is not antall:
        tempLow = array[0]
        
        for ele in array:
            if ele < tempLow:
                tempLow = ele
        array.remove(tempLow)
        outputArray.append(tempLow)
    return outputArray

print(selectionSort(array))
print(array, "a")

def bubbleSort(temparray):
    array = temparray.copy()
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] =  array[j+1], array[j]

    return array
print(bubbleSort(array),"edvcd", array)


def insertionSort(temparray):
    print(temparray, "N")
    array = temparray.copy()
    i = 0
    while True:
        #print(i)

        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            #print(array, i)
            if i> 0:    
                i -= 2

            #print(array, i
        elif (i == len(array)-2) and  (array[i] <= array[i+1]):
            return array
        i += 1
        
print(insertionSort(array), "inn")