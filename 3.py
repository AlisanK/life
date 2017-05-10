
f=open('lenta.txt','r')
l=f.readline()
r=str(bin(int(input())))
r=r[2:]
r=list(r)
r.reverse()
while len(r)<8:
    r.append(0)
N=len(l)

def cell_calculate(left, current, right):
    return r[int(right)+int(current)*2+int(left)*4]

def calculate_field(field):
    new_field = [0]*N
    for i in range(-1,N-1):
        new_field[i] = cell_calculate(field[i-1], field[i], field[i+1])
    field[:] = new_field

def generate_field(l):
    field = list(l)
    return field

def print_field(field):
    for cell in field:
        print('★' if int(cell) else ' ' , end = '')
    print()

def modelling(l):
    """ цикл моделирования клеточного автомата """
    field = generate_field(l)
    print_field(field)
    for t in range(10):
        calculate_field(field)
        print_field(field)

if __name__ == '__main__':
    modelling(l)