from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def 결과(request):
    team = int(request.GET['team'])

    if team == 2:
        result ="이 팀이 2팀이네ㅎㅎ"
    else:
        result ="저희가 많이 보죠"

    return render(request, "결과.html", {'result' : result})