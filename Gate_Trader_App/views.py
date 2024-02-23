from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def otp(request):
    return render(request, "otp.html")


def index(request):
    return render(request, "index.html")


def news(request):
    return render(request, "news.html")


def broker(request):
    return render(request, "broker.html")


def subscriptions(request):
    return render(request, "subscriptions.html")


def edit(request):
    return render(request, "edit.html")


def profile(request):
    return render(request, "profile.html")


def order(request):
    return render(request, "order.html")


def pl(request):
    return render(request, "p&l.html")


def trade_graph(request):
    return render(request, "trade_graph.html")


def planalysis(request):
    return render(request, "p&l_analysis.html")


def market(request):
    return render(request, "market.html")


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')
