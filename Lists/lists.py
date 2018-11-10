
lista = []
def action(act) :
    global lista
    act = act.split()
    if act[0] == 'insert':
        lista.insert(int(act[1]),int(act[2]))
    elif act[0] == 'print':
        print(lista)
    elif act[0] == 'remove':
        lista.remove(int(act[1]))
    elif act[0] == 'sort':
        lista.sort()
    elif act[0] == 'pop':
        lista.pop()
    elif act[0] == 'append' :
        lista.append(int(act[1]))
    elif act[0] == 'reverse' :
        lista.reverse()


if __name__ == '__main__':
    N = int(input("how many Actions: "))
    Actions = []
    for i in range(N) :
        Actions.append(input("What to do? "))
    for act in Actions:
        action(act)
