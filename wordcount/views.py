from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']    #원문글전체를 문자열로 변수에 저장
    space=text.count(' ')
    
    words=text.split()
    spacepluswords=len(words)+space
    dic=dict()
    dic2=dict()
    for i in words:
        a=dic.setdefault(i,0)
        if a == 0:
            dic[i]+=1
        else:
            dic[i]=a+1
    
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dic':dic, 'spacepluswords': spacepluswords})