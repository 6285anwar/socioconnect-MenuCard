from django.shortcuts import render

def handler404(request, exception, template_name="pages-error-404.html"):
    response = render('/not-found')
    response.status_code = 404
    return render(request, response)

def handler500(request, *args, **argv):
    return render(request, 'pages-error-500.html', status=500)
    
def handler403(request, *args, **argv):
    return render(request, 'pages-error-403.html', status=403)