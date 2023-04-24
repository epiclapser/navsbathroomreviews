from django.shortcuts import render
from django.views import generic
from .models import Review

class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status = 0)
    template_name = 'index.html'

class ReviewDetail(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
# Create your views here.
