import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    n=input("Enter a value for n >= 0: ")
    while n < 0:
        n=input("Nice try, go again!: ")
    global gamma
    gamma = input("Enter a value for G where 0<G<1: ")
    while gamma >= 1 or gamma <= 0:
        gamma = input("Nice try ;) Go again: ")

    # pretty printing
    print "\nFor n = {0}, G = {1}.\n".format( n, gamma)

    fit_exercise = q(n,'fit','exercise')
    fit_relax = q(n,'fit','relax')
    print "fit:\tExercise: {0}\tRelax: {1}\tpi: {2}".format( fit_exercise, fit_relax, "exercise" if fit_exercise >= fit_relax else "relax" )

    unfit_exercise = q(n,'unfit','exercise')
    unfit_relax = q(n,'unfit','relax')
    print "unfit:\tExercise: {0}\tRelax: {1}\tpi: {2}\n".format( unfit_exercise, unfit_relax, "exercise" if unfit_exercise >= unfit_relax else "relax")


def v (n,s):
    return max( q(n,s,'exercise'), q(n,s,'relax') )


def q (n,s,a):
    if n == 0:
        return q0(s,a)
    return  q0(s,a) + ((gamma)*(p(s,a,'fit') * v(n-1,'fit') + p(s,a,'unfit') * v(n-1,'unfit')))


def q0 (s,a):
    p_fit = p(s,a,'fit')
    p_unfit = p(s,a,'unfit')
    r_fit = r(s,a,'fit')
    r_unfit = r(s,a,'unfit')
    return (p_fit * r_fit) + (p_unfit * r_unfit)


def p (r,half,c):
    # both matrices are now in row major order in p_arr
    # one half of the array (index from 0 to 3) is the exercise matrix
    # and the other half (index 4 to 7) is the relax matrix
    p_arr = [0.99, 0.01, 0.2, 0.8, 0.7, 0.3, 0.0, 1.0]
    row_size = 2
    row = 0
    column = 0
    if r == 'unfit':
        row = 1
    if c == 'unfit':
        column = 1

    index = (row_size*row) + column

    # move to corresponding value in second half of matrix if searching for 'relax'
    if half == 'relax':
        index += 4

    return p_arr[index]


def r (r,half,c):
    # same concept as p_arr above
    r_arr = [8.0, 8.0, 0.0, 0.0, 10.0, 10.0, 5.0, 5.0]
    row_size = 2
    row = 0
    column = 0
    if r == 'unfit':
        row = 1
    if c == 'unfit':
        column = 1

    index = (row_size*row) + column

    if half == 'relax':
        index += 4

    return r_arr[index]

# just nice having the main function at the top
if __name__== "__main__":
  main()
