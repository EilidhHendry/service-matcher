from django.shortcuts import render

def search(request):
    query_string = request.GET.get('query')
    task_submit = request.POST.get('task')
    confirmation = ''
    price = ''
    service_provider = ''
    tasks = []
    if query_string:
        confirmation = 'So, you need ' + query_string + '?'
        tasks = ['install', 'replace']
    if task_submit:
        price = '99'
        service_provider = "Appliance Engineer"
    return render(request, 'service_search/search.html', {
        'query': query_string,
        'confirmation': confirmation,
        'tasks': tasks,
        'price': price,
        'service_provider': service_provider,
    })
