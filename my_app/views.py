import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models




SO_URL = 'https://stackoverflow.com/search/?q={}'
def home1(request):
    return render(request, 'home.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = SO_URL.format(quote_plus(search))
    print(final_url)
    page = requests.get(final_url).text
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    results = soup.find("div", {"class": "grid--cell fl1 fs-body3 mr12"}).text
    results = results.strip().split(' ')[0]

    question = soup.findAll("div", {"class": "question-summary search-result"})
    total_pages = soup.findAll("a", {"class": "s-pagination--item js-pagination-item"})

    print('Found:', str(len(question)), 'questions')
    print('Found: ', total_pages[-2].text, 'pages')
    f = []
    rel_ques = []
    for x in range(0, int(len(question) / 2)):
        rel_ques.append(soup.find("div", {"class": "question-summary search-result", "data-position": str(x + 1)}))

    for rel_question in rel_ques:
        p = rel_question.find("a", {"class": "question-hyperlink"}).text
        q = rel_question.find("div", {"class": "excerpt"}).text.strip()
        f.append((p,q))


    stuff_for_frontend = {
            'search': search,
            'f': f,
        }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
