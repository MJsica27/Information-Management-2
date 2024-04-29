from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import TourPackage, Review
from .forms import ReviewForm

def homepage(request):
    tour_packages = TourPackage.objects.all()
    return render(request, 'homepage.html', {'tour_packages': tour_packages})

def tour_detail(request, pk):
    tour_package = get_object_or_404(TourPackage, pk=pk)
    return render(request, 'tour_detail.html', {'tour_package': tour_package})

def review_submission(request, pk):
    tour_package = get_object_or_404(TourPackage, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour_package = tour_package
            
            # Custom validation to ensure rating is between 1 and 5
            rating = form.cleaned_data.get('rating')
            if rating < 1 or rating > 5:
                form.add_error('rating', 'Rating must be between 1 and 5.')
                return render(request, 'review_submission.html', {'form': form})
            
            review.save()
            return redirect('tour_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'review_submission.html', {'form': form})