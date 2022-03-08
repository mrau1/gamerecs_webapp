from django.shortcuts import render
from django.http import HttpResponse

# create view ==> add to urls.py here, then in parent class.
def input_view(request){
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/input.html", {"form": form})
}
def home(request):
    return render(request, 'home.html') #, context=context)

    #return HttpResponse('HOME PAGE \n Welcome to our capstone website')
