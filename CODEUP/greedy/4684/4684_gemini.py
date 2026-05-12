'''
제시해주신 코드는 문제의 핵심인 '역순으로 추적하기'에 대한 접근은 좋았으나, 조건 분기가 너무 복잡하고 자물쇠의 특성(원형 구조)을 처리하는 로직에서 막힌 것으로 보입니다.

이 문제는 3회의 동작(밀기 → 뒤집기 → 밀기)을 역순으로 되돌려 **1, 2, ..., N** 상태를 만드는 조합을 찾는 것이 핵심입니다. 아래에 피드백과 함께 효율적인 접근법을 정리해 드릴게요.

---

### 1. 코드 피드백 (수정할 점)

* **하드코딩된 로직의 위험성:** `lock[i] + 1 != lock[i+1]` 방식으로 연속성을 체크하면, 숫자가 뒤집혀서 역순(`5, 4, 3`)으로 배치된 경우를 잡아내기 어렵습니다.
* **원형 밀기(Shift) 처리:** `c = n - (again + 1)` 같은 계산식보다는 리스트 슬라이싱이나 `collections.deque`의 `rotate` 기능을 사용하는 것이 훨씬 직관적이고 실수를 줄일 수 있습니다.
* **완전 탐색의 부재:** 첫 번째 '밀기'의 경우의 수는 $1$부터 $N-1$까지로 많지 않습니다. 이를 고정하고 뒤집기 구간을 찾는 식으로 브루트 포스(Brute Force)를 섞으면 훨씬 간단해집니다.

---

### 2. 문제 해결을 위한 전략 (역순 추적)

잠긴 상태를 $S_3$라고 할 때, 우리가 해야 할 일은 다음과 같습니다:

1. **3단계 역행:** $S_3$를 오른쪽으로 $k_2$칸 밀어 $S_2$를 만듭니다. ($1 \le k_2 < N$)
2. **2단계 역행:** $S_2$에서 뒤집힌 구간 $(P, Q)$를 찾아 다시 뒤집어 $S_1$을 만듭니다.
3. **1단계 역행:** $S_1$을 오른쪽으로 $k_1$칸 밀어 `[1, 2, ..., N]`이 되는지 확인합니다.

---

### 3. 추천 소스코드 (Python)

```python
import sys

def solve():
    n = int(sys.stdin.readline())
    target = list(map(int, sys.stdin.readline().split()))
    origin = list(range(1, n + 1))

    # 1. 마지막에 밀었던 k2를 결정 (역으로 오른쪽으로 k2만큼 민다)
    for k2 in range(1, n):
        # 오른쪽으로 k2만큼 밀기 (파이썬 슬라이싱 활용)
        s2 = target[n-k2:] + target[:n-k2]
        
        # 2. 뒤집힌 구간 (P, Q) 찾기
        # 원래 순서(1~N)와 다른 부분의 시작과 끝을 찾음
        diff = [i for i in range(n) if s2[i] != origin[i]]
        
        if not diff: continue # 이미 정렬된 경우 (문제 조건상 드묾)
        
        p_idx, q_idx = diff[0], diff[-1]
        
        # 해당 구간을 뒤집어서 s1 만들기
        sub = s2[p_idx:q_idx+1]
        s1 = s2[:p_idx] + sub[::-1] + s2[q_idx+1:]
        
        # 3. 처음에 밀었던 k1 찾기
        # s1이 origin의 회전된 형태인지 확인
        # s1에서 1의 위치를 찾으면 k1을 유추할 수 있음
        try:
            one_idx = s1.index(1)
            # s1을 오른쪽으로 n-one_idx만큼 밀면 [1, 2, ...]이 되는지 확인
            k1 = (n - one_idx) % n
            check = s1[one_idx:] + s1[:one_idx]
            
            if check == origin and k1 != 0:
                print(k1)
                print(f"{p_idx + 1} {q_idx + 1}")
                print(k2)
                return
        except ValueError:
            continue

solve()

```

---

### 4. 핵심 포인트 요약

* **리스트 슬라이싱:** `arr[n-k:] + arr[:n-k]`는 리스트를 오른쪽으로 $k$번 미는 동작을 한 줄로 해결해 줍니다.
* **뒤집기 구간 식별:** 뒤집힌 구간은 반드시 `target[i] != i+1`인 지점들 사이에 존재합니다. 이 지점들의 최소/최대 인덱스를 $P, Q$ 후보로 잡으면 됩니다.
* **첫 번째 밀기($k_1$) 역산:** 뒤집기를 복구한 리스트에서 숫자 `1`이 어디에 있는지만 알면, 처음에 왼쪽으로 몇 칸 밀었는지 바로 계산할 수 있습니다.

작성하셨던 코드에서 `if` 문을 통한 케이스 분류에 너무 집중하기보다, **하나의 값을 고정(k2)하고 나머지가 성립하는지 확인**하는 방식으로 접근하면 로직이 훨씬 깔끔해질 거예요! 다시 한번 도전해 보세요. 건승을 빕니다! :)
'''

import os
import sys


input_path = os.path.join(os.path.dirname(__file__), "4684.txt")

if os.path.exists(input_path):
    print("connected")
    sys.stdin = open(input_path, "r", encoding="utf-8")


import sys

def solve():
    n = int(sys.stdin.readline())
    target = list(map(int, sys.stdin.readline().split()))
    origin = list(range(1, n + 1))

    # 1. 마지막에 밀었던 k2를 결정 (역으로 오른쪽으로 k2만큼 민다)
    for k2 in range(1, n):
        # 오른쪽으로 k2만큼 밀기 (파이썬 슬라이싱 활용)
        s2 = target[n-k2:] + target[:n-k2]
        
        # 2. 뒤집힌 구간 (P, Q) 찾기
        # 원래 순서(1~N)와 다른 부분의 시작과 끝을 찾음
        diff = [i for i in range(n) if s2[i] != origin[i]]
        
        if not diff: continue # 이미 정렬된 경우 (문제 조건상 드묾)
        
        p_idx, q_idx = diff[0], diff[-1]
        
        # 해당 구간을 뒤집어서 s1 만들기
        sub = s2[p_idx:q_idx+1]
        s1 = s2[:p_idx] + sub[::-1] + s2[q_idx+1:]
        
        # 3. 처음에 밀었던 k1 찾기
        # s1이 origin의 회전된 형태인지 확인
        # s1에서 1의 위치를 찾으면 k1을 유추할 수 있음
        try:
            one_idx = s1.index(1)
            # s1을 오른쪽으로 n-one_idx만큼 밀면 [1, 2, ...]이 되는지 확인
            k1 = (n - one_idx) % n
            check = s1[one_idx:] + s1[:one_idx]
            
            if check == origin and k1 != 0:
                print(k1)
                print(f"{p_idx + 1} {q_idx + 1}")
                print(k2)
                return
        except ValueError:
            continue

solve()