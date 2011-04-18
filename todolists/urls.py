from django.conf.urls.defaults import patterns
from django.contrib.auth.decorators import permission_required

from .views import DeleteTodolist

urlpatterns = patterns('todolists.views',
    (r'^$',                       'todolist_list'),
    (r'^(\d+)/$',                 'view'),
    (r'^add/$',                   'add'),
    (r'^edit/(?P<list_id>\d+)/$', 'edit'),
    (r'^flag/(\d+)/(\d+)/$',      'flag'),
    (r'^delete/(?P<pk>\d+)/$',
        permission_required('main.delete_todolist')(DeleteTodolist.as_view())),
)

# vim: set ts=4 sw=4 et: