## JadenCase 문자열 만들기

##### Python

```python
def solution(s):
    answer = ''
    sign=1
    for i in s:
        if sign==1:
            try:
                int(i)
                answer+=str(i)
                sign=0
            except:
                answer+=(i.upper())
                sign=0
        else:
            answer+=(i.lower())
            sign=0
        if i==' ':
            sign=1
    return answer
```
