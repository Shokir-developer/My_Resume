from django.shortcuts import render, redirect
from django.views import View

from my_portfolio.forms import SendForm
from my_portfolio.models import MySkills, MyPortfolio, Blogs


class Home(View):
    def get(self, request):
        skills = MySkills.objects.all()

        portfolio = MyPortfolio.objects.all()

        form = SendForm()
        if request.method == 'POST':
            form = SendForm(request.POST)
            if form.is_valid():
                form.save()

        context = {'skills': skills, 'portfolio': portfolio, 'form':form}
        return render(request, 'my_portfolio/index.html', context)


class BlogListView(View):
    def get(self, request):
        blogs = Blogs.objects.all()
        return render(request, 'my_portfolio/blog_list.html', {'blogs': blogs})


class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blogs.objects.get(slug=slug)
        return render(request, 'my_portfolio/blog_detail.html', {'blog': blog})