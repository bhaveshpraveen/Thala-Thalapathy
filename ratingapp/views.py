from django.shortcuts import render

from django.shortcuts import render

import rethinkdb as r

def rating_app(request):
    r.connect("localhost", 28015).repl()
    cursor = r.table('rating').run()
    print(cursor)
    person = list(cursor)
    context = {
        person[0]['name']: person[0]['votes'],
        person[1]['name']: person[1]['votes']
    }
    return render(request, 'base.html', context)