from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .services import get_launches
from .models import Launch


class LaunchesPage(ListView):
    def get(self, request):
        launches = get_launches(request)

        for i in launches:
            launch_data = Launch(
                name = i['mission_name'],
                launch_year = i['launch_year'],
                launch_date = i['launch_date_utc'],
                succeeded = i['launch_success'],
                upcoming = i['upcoming'],
                description = i['details'],
                rocket = i['rocket']['rocket_name'],
                launch_site = i['launch_site']['site_name_long'],
                slug = i['flight_number'],
                image_url = i['links']['mission_patch'],
                image_alt_url = i['links']['mission_patch_small'],
                article_url = i['links']['article_link'],
                wikipedia_url = i['links']['wikipedia'],
                video = i['links']['video_link']
            )
            if not Launch.objects.filter(slug=i['flight_number']).exists():
                launch_data.save()
        all_launches = Launch.objects.all().order_by('-id')
            
        paginator = Paginator(all_launches, 24) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'launches.html', {'launches':page_obj})

def home(request):
    launches = Launch.objects.all().order_by('-id')[0:8]
    return render(request, 'home.html', {'launches':launches})


def launch_detail(request, id):
    launch = Launch.objects.get(id = id)
    print(launch)
    return render (
        request,
        'launch_details.html',
        {'launch': launch}
    )

def search_launches(request):
    if request.method == "POST":
        search = request.POST['search']
        launches = Launch.objects.filter(Q(name__contains=search) | Q(launch_date__year=search))

        all_launches = launches.order_by('-id')
            
        paginator = Paginator(all_launches, 24) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'search.html', {'search': search,
        'launches':page_obj})
    else:
        return render(request, 'search.html')



