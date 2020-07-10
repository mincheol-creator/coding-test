## 더 맵게

##### Python

```python
def solution(citations):
    up=0
    down=0
    arr=[]
    for i in range(len(citations)):
        for j in citations:
            if (i+1)<=j:
                up+=1
            else:
                down+=1
        if (i+1)<=up and (i+1)>=down:
            arr.append(i+1)
        up=0
        down=0
    return max(arr) if arr!=[] else 0
```
