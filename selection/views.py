from django.shortcuts import render
from .forms import UserInputForm
from .models import College, CollegeInfo
from django.shortcuts import get_object_or_404


def home(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            city = form.cleaned_data['city']
            course = form.cleaned_data['course']
            colleges = College.objects.filter(
                level=level, city=city, courses_offered=course
            )
            print(colleges)
            return render(request, 'college_list.html', {'colleges': colleges})
    else:
        form = UserInputForm()
        return render(request, 'home.html', {'form': form})


def college(request, college):
    print(college)
    college_info = get_object_or_404(CollegeInfo, college__name=college)
    return render(request, 'college_detail.html', {'object': college_info})
