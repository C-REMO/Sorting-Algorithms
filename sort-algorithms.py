#!/usr/bin/python3
import time, random

#unsorted_list = ['c','a','a','b','a','t','d','a','f','e','a']
#unsorted_list = [1,3,7,4,9,2,5,6,0,8,0,1,2,4]
#unsorted_list = [1,3,7,4]
unsorted_list = [random.randint(0,9999) for i in range(7000)]
#unsorted_list = [random.randint(0,9) for i in range(7000)]

#Bubble sort ascending
def BubbleSortAsc(lst):
    swapped = True
    sortedvalue=0
    while swapped:
        swapped = False
        sortedvalue+=1
        for i in range(0,len(lst)-sortedvalue):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1], swapped = lst[i+1], lst[i], True

#Bubble sort descending
def BubbleSortDsc(lst):
    swapped = True
    sortedvalue=0
    while swapped:
        swapped = False
        sortedvalue+=1
        for i in range (0,len(lst)-sortedvalue):
            if lst[i]<lst[i+1]:
                lst[i], lst[i+1], swapped = lst[i+1], lst[i], True

#Selection sort ascending
def SelectionSortAsc(lst):
    swapped = True
    counter=0
    while swapped:
        swapped = False
        min=lst[counter]
        for i in range (counter,len(lst)):
            if min>=lst[i]:
                min=lst[i]
                index=i
                swapped = True
        lst[counter], lst[index] = lst[index], lst[counter]
        counter+=1
        if counter==len(lst): break

#Selection sort descending
def SelectionSortDsc(lst):
    swapped = True
    counter=0
    while swapped:
        swapped = False
        min=lst[counter]
        for i in range (counter,len(lst)):
            if min<=lst[i]:
                min=lst[i]
                index=i
                swapped = True
        lst[counter], lst[index] = lst[index], lst[counter]
        counter+=1
        if counter==len(lst): break

#Insertion sort ascending
def InsertionSortAsc(lst):
    counter=0
    while counter<len(lst)-1:
        for i in range(counter+1,0,-1):
            if lst[i]<lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
            else: break
        counter+=1

#Insertion sort descending
def InsertionSortDsc(lst):
    counter=0
    while counter<len(lst)-1:
        for i in range(counter+1,0,-1):
            if lst[i]>lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
            else: break
        counter+=1

#Shell sort ascending
def ShellSortAsc(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(0, len(lst)-gap):
            if lst[i]>lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                for j in range(i-gap,-1,-gap):
                    if lst[j]>lst[j+gap]:
                        lst[j], lst[j+gap] = lst[j+gap], lst[j]
        gap//=2

#Shell sort descending
def ShellSortDsc(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(0, len(lst)-gap):
            if lst[i]<lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                for j in range(i-gap,-1,-gap):
                    if lst[j]<lst[j+gap]:
                        lst[j], lst[j+gap] = lst[j+gap], lst[j]
        gap//=2

#Merge sort ascending
def MergeSortAsc(lst):
    half = len(lst)//2
    left_half, right_half = lst[:half], lst[half:]
    if len(left_half) > 1: left_half = MergeSortAsc(left_half)
    if len(right_half)> 1: right_half= MergeSortAsc(right_half)
    sorted_list = []
    while left_half and right_half:
        if left_half[0] <= right_half[0]:
            sorted_list.append(left_half.pop(0))
        else:
            sorted_list.append(right_half.pop(0))
    return sorted_list + (left_half or right_half)

#Merge sort descending
def MergeSortDsc(lst):
    half = len(lst)//2
    left_half, right_half = lst[:half], lst[half:]
    if len(left_half) > 1: left_half = MergeSortDsc(left_half)
    if len(right_half)> 1: right_half= MergeSortDsc(right_half)
    sorted_list = []
    while left_half and right_half:
        if left_half[0] >= right_half[0]:
            sorted_list.append(left_half.pop(0))
        else:
            sorted_list.append(right_half.pop(0))
    return sorted_list + (left_half or right_half)

#Quick sort ascending
def QuickSortAsc(lst,pivot,high):
    index=pivot+1
    if index>high: return
    border=pivot
    while index<=high:
        if lst[index]<=lst[pivot]:
            border+=1
            lst[index], lst[border] = lst[border], lst[index]
        index+=1
    if lst[pivot]>lst[border]:
        lst[pivot], lst[border] = lst[border], lst[pivot]
    QuickSortAsc(lst,pivot,border-1)
    QuickSortAsc(lst,border+1,index-1)
    return (lst)

#Quick sort descending
def QuickSortDsc(lst,pivot,high):
    index=pivot+1
    if index>high: return
    border=pivot
    while index<=high:
        if lst[index]>=lst[pivot]:
            border+=1
            lst[index], lst[border] = lst[border], lst[index]
        index+=1
    if lst[pivot]<lst[border]:
        lst[pivot], lst[border] = lst[border], lst[pivot]
    QuickSortDsc(lst,pivot,border-1)
    QuickSortDsc(lst,border+1,index-1)
    return (lst)

if __name__ == '__main__':
    t1=time.clock()
    BubbleSortAsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t1)+' seconds for BubbleSortAsc.')

    t2=time.clock()
    BubbleSortDsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t2)+' seconds for BubbleSortDsc.')

    t3=time.clock()
    SelectionSortAsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t3)+' seconds for SelectionSortAsc.')

    t4=time.clock()
    SelectionSortDsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t4)+' seconds for SelectionSortDsc.')

    t5=time.clock()
    InsertionSortAsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t5)+' seconds for InsertionSortAsc.')

    t6=time.clock()
    InsertionSortDsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t6)+' seconds for InsertionSortDsc.')

    t7=time.clock()
    ShellSortAsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t7)+' seconds for ShellSortAsc.')

    t8=time.clock()
    ShellSortDsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t8)+' seconds for ShellSortDsc.')

    t9=time.clock()
    MergeSortAsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t9)+' seconds for MergeSortAsc.')

    t10=time.clock()
    MergeSortDsc(unsorted_list[:])
    print('%.4f' % (time.clock()-t10)+' seconds for MergeSortDsc.')

    t11=time.clock()
    QuickSortAsc(unsorted_list[:],0,len(unsorted_list)-1)
    print('%.4f' % (time.clock()-t11)+' seconds for QuickSortAsc.')

    t12=time.clock()
    QuickSortDsc(unsorted_list[:],0,len(unsorted_list)-1)
    print('%.4f' % (time.clock()-t12)+' seconds for QuickSortDsc.')
