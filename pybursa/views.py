from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def student_list(request):
    return render(request, 'student_list.html')
    
def quadratic_results(request):
    
    def checkreq(abc):
        oshibka = ''
        if not abc == '':
            good = abc
            for i in abc:
                if not i in '-0123456789':
                    oshibka = 'коэффициент не целое число'
        else:
            good = abc
            oshibka = 'коэффициент не определен'
        return good, oshibka
    
    error = False
    a, errora = checkreq(request.GET['a'])    
    if a == '0':
        errora = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        
    b, errorb = checkreq(request.GET['b'])
    c, errorc = checkreq(request.GET['c'])
    errord = ''
    discr = ''
    d = 0
    x1 = 0
    x2 = 0 
    
    if not errora == '' or not errorb == '' or not errorc == '':
        error = True
    
    if not error:
        d = int(b)**2 - 4*int(a)*int(c)
        discr = 'Дискриминант: %d' % d
        
        if d >= 0:
            x1 = round((-int(b) + (d**0.5)) / 2*int(a), 1)
            x2 = round((-int(b) - (d**0.5)) / 2*int(a), 1)
    
        if d < 0:
            errord = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            errord = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x1
        elif d > 0:
            errord = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
            
    return render(request, 'quadratic/results.html', context = {
                                                                'errora': errora,
                                                                'errorb': errorb,
                                                                'errorc': errorc,
                                                                'errord': errord,
                                                                'discr': discr,
                                                                'a': a,
                                                                'b': b,
                                                                'c': c, })
