from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    
    path('enterform', views.enterform, name="enterform"),
    path('getform', views.getform, name="getform"),
    path('enteradmin', views.enteradmin, name='enteradmin'),
    path('getadmin', views.getadmin, name='getadmin'),
    path('enterowner', views.enterowner, name='enterowner'),
    path('getowner', views.getowner, name='getowner'),
    path('enteruser', views.enteruser, name='enteruser'),
    path('getuser', views.getuser, name='getuser'),
    path('enterplot', views.enterplot, name='enterplot'),
    path('getplot', views.getplot, name='getplot'),
    path('entertrans', views.entertrans, name='entertrans'),
    path('gettrans', views.gettrans, name='gettrans'),
    path('entertenure', views.entertenure, name='entertenure'),
    path('gettenure', views.gettenure, name='gettenure'),
    path('entervalue', views.entervalue, name='entervalue'),
    path('getvalue', views.getvalue, name='getvalue'),
    path('enterinfra', views.enterinfra, name='enterinfra'),
    path('getinfra', views.getinfra, name='getinfra'),
    path('deluser/<int:user_id>', views.deluser, name='deluser'),
    path('updateuser/<int:user_id>', views.updateuser, name='updateuser'),
    path('updateuser/updated/<int:user_id>', views.updated, name='updated'),
    path('delowner/<int:owner_id>', views.delowner, name='delowner'),
    path('updateowner/<int:owner_id>', views.updateowner, name='updateowner'),
    path('updateowner/updatedowner/<int:owner_id>', views.updatedowner, name='updatedowner'),
    path('delinfra/<int:infrastructure_id>', views.delinfra, name='delinfra'),
    path('updateinfra/<int:infrastructure_id>', views.updateinfra, name='updateinfra'),
    path('updateinfra/updatedinfra/<int:infrastructure_id>', views.updatedinfra, name='updatedinfra'),
    path('deltenure/<int:tenure_id>', views.deltenure, name='deltenure'),
    path('updatetenure/<int:tenure_id>', views.updatetenure, name='updatetenure'),
    path('updatetenure/updatedtenure/<int:tenure_id>', views.updatedtenure, name='updatedtenure'),
    path('deltrans/<int:transaction_id>', views.deltrans, name='deltrans'),
    path('updatetrans/<int:transaction_id>', views.updatetrans, name='updatetrans'),
    path('updatetrans/updatedtrans/<int:transaction_id>', views.updatedtrans, name='updatedtrans'),
    path('delplot/<int:plot_id>', views.delplot, name='delplot'),
    path('updateplot/<int:plot_id>', views.updateplot, name='updateplot'),
    path('updateplot/updatedplot/<int:plot_id>', views.updatedplot, name='updatedplot'),
    path('delvalue/<int:valuation_id>', views.delvalue, name='delvalue'),
    path('updatevalue/<int:valuation_id>', views.updatevalue, name='updatevalue'),
    path('updatevalue/updatedvalue/<int:valuation_id>', views.updatedvalue, name='updatedvalue'),
    path('owner/<int:owner_id>/', views.ownerid, name='ownerid'),
    path('admin/<int:admin_id>/', views.adminid, name='adminid'),
    path('user/<int:user_id>/', views.userid, name='userid'),
    path('tenure/<int:tenure_id>/', views.tenureid, name='tenureid'),
    path('plot/<int:plot_id>/', views.plotid, name='plotid'),
    path('value/<int:valuation_id>/', views.valueid, name='valueid'),
    path('trans/<int:transaction_id>/', views.transid, name='transid'),
    path('infra/<int:infrastructure_id>/', views.infraid, name='infraid'),
    path('filterplot/', views.filterplot, name='filterplot'),
    path('ownerdob/<int:age>/', views.ownerdob, name='ownerdob'),
    path('filtervalue/', views.filtervalue, name='filtervalue'),
    path('filtertrans/', views.filtertrans, name='filtertrans'),
    path('filtertenure/', views.filtertenure, name='filtertenure'),
    path('filterinfra', views.filterinfra, name='filterinfra'),
    path('', views.index, name='index'),
]