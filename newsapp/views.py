from django.shortcuts import render
import requests
def main(request):
    r=requests.get('http://api.mediastack.com/v1/news?access_key=d89f60bbef1de51ad6e0732f10558681')
    res=r.json()
    data=res['data']
    title=[]
    description=[]
    image=[]
    url=[]
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news= zip(title,description,image,url)
    context={
        "news":news
    }
    return render(request,'newsapp/index.html',context)