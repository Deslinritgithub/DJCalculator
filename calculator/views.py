from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# create your views here

@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
      def post(self,request):
          request_body=request.body
          form_data=request.body
          n1=form_data.get('num1')
          n2=form_data.get('num2')
          result=n1+n2
          print(request_body)
          data={
              "sum":result
          }
          return JsonResponse(data)
      
      
@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        data=request.body
        form_data=request.body(data)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        differnece=n1-n2
        result={
            "differene":differnece
        }
        return JsonResponse(result)

        