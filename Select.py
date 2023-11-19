import random
import sys

# 선택정렬
def Selection(a):
    n = len(a)
    for i in range(n-1): # for문은 0부터 시작하기 때문에 -1 값 해주기
        least = i  # 현재까지의 최솟값을 저장하고 있는 인덱스
        for j in range(i+1, n):  # 최솟값을 탐색하기 위한 루프
            if a[j] < a[least]:  # j번째 수가 현재까지의 최솟값보다 작다면?
                least = j  # 최솟값을 j로 변경
        a[i], a[least] = a[least], a[i]  # 현재 위치(i)와 최솟값의 위치를 교환
    return a
# 삽입정렬
def Insertion(a):
    n = len(a)
    for i in range(1,n): # 첫 번째 원소는 정렬된 상태로 간주하고, 두 번째 원소부터 시작하여 리스트를 끝까지 순회
        key = a[i] # 현재 정렬하고자 하는 원소를 key에 저장
        j = i-1 # j는 key의 바로 앞에 있는 원소의 인덱스
        while j >= 0 and a[j] > key: # key가 정렬된 부분의 원소(a[j])보다 크거나 같을 때까지 또는 j가 0이 될 때까지 반복
            a[j+1] = a[j] # a[j]가 key보다 크므로, a[j]를 오른쪽으로 한 칸 이동
            j -= 1 # j를 왼쪽으로 한 칸 이동
        a[j+1] = key # key를 정렬된 올바른 위치에 삽입
    return a

# 버블정렬
def Bubble(a):
    n = len(a)
    for i in range(n-1, 0, -1): # 리스트의 마지막 인덱스부터 첫 번째 인덱스까지 역순으로 순회
        for j in range(i): # 리스트의 첫 번째 원소부터 i번째 원소까지 순회
            if a[j] > a[j+1]: # 만약 현재 원소가 다음 원소보다 크다면,
                a[j], a[j+1] = a[j+1], a[j] # 두 원소의 위치를 바꾸기
    return a

# 퀵정렬
def Quick(a, left, right):
    if left < right: # 왼쪽 인덱스가 오른쪽 인덱스보다 작은 경우에만 정렬을 수행
        i = left + 1 # i는 pivot보다 큰 값을 찾기 위한 인덱스, pivot의 오른쪽 인덱스로 초기화
        j = right # j는 pivot보다 작은 값을 찾기 위한 인덱스, 리스트의 오른쪽 끝 인덱스로 초기화
        pivot = a[left] # 피봇을 리스트의 왼쪽 첫 번째 원소로 설정
        while i <= j: # i와 j가 교차할 때까지 반복
            while i <= right and a[i] <= pivot:  # i가 오른쪽 끝을 넘지 않고, i번째 원소가 pivot보다 작거나 같다면?
                i += 1 # i를 오른쪽으로 이동
            while j >= left and a[j] > pivot: # j가 왼쪽 끝을 넘지 않고, j번째 원소가 pivot보다 크다면?
                j -= 1 # j를 왼쪽으로 이동
            if i < j: # i가 j보다 작다면?
                a[i], a[j] = a[j], a[i] # i번째 원소와 j번째 원소의 위치를 바꾸기
        a[left], a[j] = a[j], a[left] # 피봇과 j번째 원소의 위치를 바꿉니다.
        Quick(a, left, j-1) # 피봇의 왼쪽 부분을 재귀함수로 퀵 정렬
        Quick(a, j+1, right) # 피봇의 오른쪽 부분을 재귀함수로 퀵 정렬

# 합병정렬
sorted = []  # 정렬된 결과를 저장할 리스트를 선언
def Merge(a, left, mid, right):
    i = left  # 왼쪽 부분 배열의 시작 인덱스를 i로 지정
    j = mid + 1  # 오른쪽 부분 배열의 시작 인덱스를 j로 지정
    # 왼쪽 부분 배열과 오른쪽 부분 배열을 비교하면서 작은 순서대로 sorted_list에 추가
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            sorted[k]
            i += 1
            k += 1
        else:
            sorted[k] = a[j] 
            k+=1
            j += 1
    # 남은 요소들을 sorted_list에 추가
    if i > mid:
        sorted[k: k+right-j+1] = a[j: right+1]
    else:
        sorted[k: k+mid-i+1] = sorted[left: right+1]
    # sorted_list로 원래 배열의 left부터 right까지의 요소를 대체

def MergeSort(a, left, right):
    global sorted # 정렬된 리스트
    if left < right:
        mid = (left + right) // 2 # 분할 기준 정하기
        MergeSort(a, left, mid)  # 왼쪽 부분 분할
        MergeSort(a, mid+1, right)  # 오른쪽 부분 분할
        Merge(a, left, mid, right)  # 분할된된 두 부분 배열을 합병
        return a
# 힙정렬 1
def heap1push(heap, n):
    heap.append(n)  # 힙에 새로운 요소를 추가
    i = len(heap) - 1  # 추가된 요소의 인덱스를 i로 지정
    while i != 1 and n > heap[i//2]:  # 부모 노드와 비교하여 힙 속성을 만족시키도록 요소를 이동
        heap[i] = heap[i//2]
        i //= 2
    heap[i] = n

def heap1pop(heap):
    size = len(heap) - 1
    if size == 0:
        return None  # 힙이 비어있을 경우 None을 반환
    root = heap[1]  # 최대값인 루트 노드를 저장
    last = heap[size]  # 힙의 마지막 요소를 저장
    p = 1 # 부모 인덱스 포인터
    i = 2 # 자식 인덱스 포인터
    while i <= size:
        if i < size and heap[i] < heap[i+1]:  # 자식 노드 중 더 큰 값을 선택
            i += 1
        if last >= heap[i]:  # 마지막 요소가 자식 노드보다 크거나 같으면 반복을 종료
            break
        heap[p] = heap[i]  # 자식 노드를 부모 노드로 이동
        p = i # 부모 포인터를 자식 포인터로 이동
        i *= 2 # 자식 포인터를 아래로 이동
    heap[p] = last  # 마지막 요소를 삽입
    heap.pop()  # 마지막 요소를 제거
    return root

def heap1Sort(data):
    heap = [0]  # 힙을 초기화
    for e in data:
        heap1push(heap, e)  # 데이터를 힙에 추가
    sorted_data = []
    for i in range(1, len(data) + 1):
        data[-i] = heap1pop(heap)
    return data

# 힙정렬 2
def heapify(arr, n, i): # n = arr의 길이, i = 루트노드 인덱스
    largest = i  # 현재 노드를 가장 큰 값으로 설정
    l = 2 * i  # 왼쪽 자식 노드의 인덱스를 계산
    r = 2 * i+1  # 오른쪽 자식 노드의 인덱스를 계산
    # 루트(i)와 두 자식 중 가장 큰 요소 인덱스 구하기
    if l <= n and arr[i] < arr[l]:  # 왼쪽 자식 노드가 존재하고 현재 노드보다 크다면?
        largest = l  # largest 변수를 업데이트
    if r <= n and arr[largest] < arr[r]:  # 오른쪽 자식 노드가 존재하고 largest 변수보다 크다면?
        largest = r  # largest 변수를 업데이트
    if largest != i:  # largest가 i와 다르다면?
        arr[i], arr[largest] = arr[largest], arr[i]  # 현재 노드와 largest 값을 교환
        heapify(arr, n, largest)  # 재귀적으로 heapify 함수를 호출하여 하위 트리에 대해 heapify 작업 하기


def heap2Sort(arr):
    n = len(arr) - 1  # 배열의 크기를 저장

    # 힙을 구성 (최대 힙)
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)

    # 힙 정렬 수행
    for i in range(n - 1, 0, -1):
        arr[i + 1], arr[1] = arr[1], arr[i + 1]  # 가장 큰 값을 배열의 맨 뒤로 이동
        heapify(arr, i, 1)  # 힙 속성을 유지하며 재귀적으로 heapify 작업을 수행
    return arr

def Sort_main():
    while True:
        a = random.sample(range(101), 25) # 리스트 생성
        print("정렬 프로그램 중 하나를 선택하세요.")
        print("----------------------------------")
        print("1. 선택정렬 (Selection Sort)")
        print("2. 삽입정렬 (Insertion Sort)")
        print("3. 버블정렬 (Bubble Sort)")
        print("4. 퀵정렬 (Quick Sort)")
        print("5. 합병정렬 (Merge Sort)")
        print("6. 힙정렬 (Heap Sort)")
        print("8. 종료(quit)")
        Select = input("정렬 번호 선택 : ")
        print("")
        if Select == "1":
            print("정렬 전 :", a)
            print("정렬 후 :", Selection(a))
        elif Select == "2":
            print("정렬 전 :", a)
            print("정렬 후 :", Insertion(a))
        elif Select == "3":
            print("정렬 전 :", a)
            print("정렬 후 :", Bubble(a))
        elif Select == "4":
            print("정렬 전 :", a)
            Quick(a, 0, len(a) - 1)
            print("정렬 후 :", a)
        elif Select == "5":
            print("정렬 전 :", a)
            MergeSort(a, 0, len(a) - 1)
            print("정렬 후 :", a)
        elif Select == "6":
            print("힙 정렬 1")
            print("정렬 전 :", a)
            print("힙 정렬 1")
            print("정렬 후 :", heap1Sort(a))
            print("힙 정렬 2")
            print("정렬 후 :", heap2Sort(a))
        elif Select == "7":
            print('종료')
            sys.exit()
        else:
            print('번호를 잘못 입력하셨습니다')

if __name__ == "__main__":
    Sort_main()
