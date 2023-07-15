
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c_even = 0
    c_odd = 0
    m_even = -float('inf')
    m_odd = -float('inf')
    for i in range(n):
        x = a[i]
        if i % 2 == 0:

            m_even = max(m_even, x)

            if x > 0:
                c_even += x
        else:

            m_odd = max(m_odd, x)

            if x > 0:
                c_odd += x
    print(max(c_even if m_even >= 0 else m_even, c_odd if m_odd >= 0 else m_odd))