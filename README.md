# django_with_data_table.js
django-datatable
================

Overview
--------

django-datatable is a simple Django app to organize data in tabular
form based on `datatable <http://datatables.net>`__ and
`bootstrap <http://getbootstrap.com/>`__.

It is worth mentioning that the design of this project makes reference
to `django-table2 <https://github.com/bradleyayers/django-tables2>`__
and is mainly for the purpose of learning. I really appreciate anyone
making a pull-request to improve it.

Requirements
------------

-  Python 2.x,3.X

-  jQuery 1.6+

-  Django 1.10+

-  Bootstrap 3.0

Quick start
-----------

-  Setup Django-datatable application in Python environment:

   ::

       $ pip install django-datatable
::

    Urls:

        # urls.py
        from django.conf.urls import url, include
        from django.contrib import admin

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^your_app', include('home_app.urls')),
        ]

    your_app/Urls:

        # urls.py
        from django.conf.urls import url
        from .import views

        urlpatterns = [
            url(r'1/', views.OrderListJson.as_view(), name='order_list_json'), #that url return json data
            url(r'2/', views.OrderList1.as_view(), name='order_list_json2'), # that url return data_table_views.js
        ]


-  add you model into your_app/models.py here my model name "Internalorder":

   ::
  
       # example/your_app/models.py
       class Internalorder(models.Model):
          order_id = models.AutoField(primary_key=True)
          ordertime = models.TextField(blank=True, null=True)
          last_updated = models.TextField(blank=True, null=True)
          ordertype = models.TextField(blank=True, null=True)

          class Meta:
            managed = False
            db_table = 'internalorder'


-  Add "your_django_app_name" to your INSTALLED\_APPS setting like this:

   ::

       INSTALLED_APPS = (
           ...,
           'your_django_app_name',
       )

And pass a table instance to the view.

::

        # example/your_app/views.py
        from django.shortcuts import render #render templates
        from django.http import HttpResponse #return response
        from django_datatables_view.base_datatable_view import BaseDatatableView #for data view 
        from django.views.generic import TemplateView # for template
        from .models import Internalorder   #import your models

        class OrderListJson(BaseDatatableView):
          model = Internalorder
          #define that columns name into list that you want display in template and available in your models example: your_app/models.py
          columns = ['order_id','etc']
          #same as here 
          order_columns = ['order_id','etc']


          max_display_length = 50
          
          #that function return Json list of dict data
          def render_column(self, row, column):
            return super(OrderListJson, self).render_column(row, column)
        
        class OrderList1(TemplateView):
          template_name  = "folder_name/order_list_json.html" #return templates 

-  Finally, implement the template:
add html into your templates file folder
----------
your_app/templates/folder_name/base.html
::
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
      <head>
          <title>Welcome in Internalorder Table</title>
          <script src="//code.jquery.com/jquery-1.12.4.js"></script>
          {% block extra_head %}{% endblock %}
      </head>
      <body>
         <div>
          <h2><p>Welcome To Internalorder Table</p></h2>
         </div>
          {% block content %}{% endblock %}
      </body>
  </html>

add html into your templates file folder
----------
your_app/templates/folder_name/order_list_json.html
::
{% extends "base.html" %}

{% block extra_head %}
    {% load static %}
    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css">
    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/fixedheader/3.1.3/css/fixedHeader.dataTables.min.css">
    <script type="text/javascript" charset="utf8" src="//cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" charset="utf8" src="cdn.datatables.net/fixedheader/3.1.3/js/dataTables.fixedHeader.min.js"></script>
    <script src='{% static "home_app/internalorder_datatables.js" %}' type="text/javascript"></script>
    <script type="text/javascript">
        var USERS_LIST_JSON_URL = '{% url "order_list_json" %}';
    </script>
   
{% endblock %}

{% block content %}
    <table class="display compact", id="table", cellspacing="0" width="100%">
       <thead>
            <tr>
                <th>order_id</th>   # type here your columns name accordingly your models columns 
                <th>ordertime</th>  # type here your columns name accordingly your models columns 
                <th>last_updated</th> # type here your columns name accordingly your models columns   
                <th>ordertype</th>  # type here your columns name accordingly your models columns 
                <th>ticker</th>   # type here your columns name accordingly your models columns 
                <th>quantity</th>
                <th>test</th>
                <th>test2</th>
            </tr>
        </thead>
    </table>
{% endblock %}


add javascript into your static file folder
----------
your_app/static/folder_name/internalorder_datatables.js
::
$(document).ready(function() {
    var dt_table = $('table').DataTable({
        fixedHeader: true,
        order: [[ 0, "desc" ]],
        lengthMenu: [[20 ,50,100,200], [20,50,100,200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0,1,2,3,4,5]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: USERS_LIST_JSON_URL,
        
        
    });    

# that block refrese your data every 5 sec
    // setInterval( function () {
    //     dt_table.ajax.reload();
    // }, 5000 );
    
    
});
````````

Built-in Ajax
`````````````

For large amounts of data, loading them on front-end entirely is
impossible. So, django-table provides a simle option 'ajax' to load data
from the server-side asynchronously.

Note that once toggling ``ajax``, the ``model`` option is necessary.
Django-table will do paging/searching/sorting based on
``ModelClass.objects.all()``.

