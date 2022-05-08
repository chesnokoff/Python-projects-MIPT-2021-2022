from django.shortcuts import render


def create(request):
    return render(request, 'clicker/create.html')


def clicking(request):
    cost1 = request.POST['cost1']
    cost2 = request.POST['cost2']
    cost3 = request.POST['cost3']
    power1 = request.POST['power1']
    power2 = request.POST['power2']
    power3 = request.POST['power3']

    if cost1.isdigit() and cost2.isdigit() and cost3.isdigit() and power1.isdigit() \
            and power2.isdigit() and power3.isdigit():
        cost1 = int(cost1)
        cost2 = int(cost2)
        cost3 = int(cost3)
        power1 = int(power1)
        power2 = int(power2)
        power3 = int(power3)
    else:
        cost1 = 1
        cost2 = 25
        cost3 = 100
        power1 = 1
        power2 = 5
        power3 = 20
    dct = {"cost1": cost1,
           "cost2": cost2,
           "cost3": cost3,
           "power1": power1,
           "power2": power2,
           "power3": power3,}
    return render(request, 'clicker/clicker.html', dct)
