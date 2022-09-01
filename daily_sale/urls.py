from django.urls import include, path
from . import views
from daily_sale.views import DailyChartView , MonthlyChartView , CashOnlineChartView , MonthlyCashOnlineChartView

"""
urlpatterns contains Authentication module relvent URLs (APIs)
This urls are access by Admin permision and normal user can also access
"""
urlpatterns = [
    path('daily-report/', DailyChartView.as_view(), name='Daily sales'),
    path('monthly-report/', MonthlyChartView.as_view(), name='Monthly Sales'),
    path('cash-online-report/', CashOnlineChartView.as_view(), name='Daily Cash/Online Sales'),
    path('monthly-cash-online-report/', MonthlyCashOnlineChartView.as_view(), name='Monthly Cash/Online Sales'),
]
