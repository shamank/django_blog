from django.shortcuts import render

# Create your views here.


from elasticsearch_dsl import Q
from app.documents import PostDocument

def search_posts(request):
    query = request.GET.get('q')
    q = Q('multi_match', query=query, fields=['title', 'description', 'content'], fuzziness='auto')
    search = PostDocument.search().query(q)
    # response = search.execute()
    result = search.to_queryset()
    return render(request, template_name='app/search.html', context={'result': result})