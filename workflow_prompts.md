**Prompt 1 — Discussion (Claude)**

```
I have a coding problem I need to solve: given a stream of integers, 
find the most frequent element at any point in time.

Don't give me the solution. Instead, help me think through it like 
a senior engineer would. Ask me questions to guide my thinking. 
What data structure should I use and why? What are the tradeoffs? 
Push back if my reasoning is wrong.
```

---

**Prompt 2 — Plan (Claude, after discussion)**

```
Based on our discussion, give me a concrete step-by-step implementation 
plan for solving this problem. Break it down into small coding steps. 
Don't write the code — just tell me exactly what to build and in what order.
```

---

**Prompt 3 — Review (Gemini or Qwen, after implementing)**

```
I solved this problem: given a stream of integers, find the most frequent 
element at any point in time. Here is my Python solution: [paste code here]

Review it and tell me:
1. Does it actually solve the problem correctly?
2. What is the time and space complexity?
3. What edge cases did I miss?
4. How would you improve it?

Be direct and technical.
```

