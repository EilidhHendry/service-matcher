from django.shortcuts import render
import pre_process
import services_tree

def search(request):
    query_string = request.GET.get('query')
    task_submit = request.POST.get('task')
    confirmation = ''
    price = ''
    service_provider = ''
    tasks = []
    if query_string:
        n_grams = pre_process.get_query_grams(query_string)
        path, choices = services_tree.search_services_tree(n_grams)
        confirmation = 'So, you want ' + ' '.join(path) + '?'
    if task_submit:
        choices = services_tree.services_tree[task_submit]
    try:
        len(choices)
        tasks = choices
    except:
        price = str(choices)
    return render(request, 'service_search/search.html', {
        'query': query_string,
        'confirmation': confirmation,
        'tasks': tasks,
        'price': price,
    })
