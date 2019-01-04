from django.core.paginator import Paginator
 
def getPages(request, objectlist):
    """get the paginator"""
    currentPage = request.GET.get('page', 1)
    
    paginator = Paginator(objectlist, 4)
    objectlist = paginator.page(currentPage)
 
    return paginator, objectlist