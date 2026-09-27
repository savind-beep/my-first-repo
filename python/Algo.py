import queue

L = []


def Push(value=None):
    if value is not None:
        L.append(value)
    return L


def push(value=None):
    if value is not None:
        L.append(value)
    return L


def pop():
    if not L:
        return None
    return L.pop()


def peek():
    if not L:
        return None
    return L[-1]


Push(15)
print(L)
push(25)
print(L)
push(35)
print(L)
print(pop())
print(L)
push(45)
print(L)
push(55)
print(L)
print(peek())
print(pop())
push(65)
print(L)

