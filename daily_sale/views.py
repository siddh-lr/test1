from django.shortcuts import render
from django.views.generic import TemplateView
from .models import daily_sale
from django.db.models import Sum
from django.db.models.functions import ExtractMonth , Cast
from django.db.models import DateField


# Creating views
class DailyChartView(TemplateView):
    template_name = 'daily_sale/daily_data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = daily_sale.objects.all().order_by("date")
        return context
    
    
class MonthlyChartView(TemplateView):
    template_name = 'daily_sale/monthly_data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = daily_sale.objects.filter().values(
                        'id',
                        'date',
                        'total_amount',
                    ).annotate(
                        month=Cast('date', DateField())
                    ).values('month').annotate(
                        total_revenue_amount=Sum('total_amount')
                    ).order_by("month")
        print("11")
        print(context["qs"])
        for i in context["qs"]:
            import datetime

            #provide month number
            month_num = str(i["month"])
            datetime_object = datetime.datetime.strptime(month_num, "%m")

            month_name = datetime_object.strftime("%b")
            print("Short name: ",month_name)
            print(i["month"])
            print(month_name)
        #     i["month"] = {"month_id": i["month"], "month_nm":month_name}
        #     # revenue = i['total_revenue_amount']
        #     # print(i['total_revenue_amount'])
        # # return revenue
        # print(context)
        return context
    
    
class CashOnlineChartView(TemplateView):
    template_name = 'daily_sale/cash_online.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = daily_sale.objects.all().order_by("date")
        return context
    
    
class MonthlyCashOnlineChartView(TemplateView):
    template_name = 'daily_sale/monthly_cash_online.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = daily_sale.objects.filter().values(
                        'id',
                        'date',
                        'cash',
                        'online',
                    ).annotate(
                        month=ExtractMonth('date')
                    ).values('month').annotate(
                        total_cash=Sum('cash'),total_online_payment=Sum('online')
                    ).order_by("month")
        print("11")
        print(context["qs"])
        return context