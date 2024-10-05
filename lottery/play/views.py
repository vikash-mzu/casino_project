from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
import random
def play(request):
    context = {}
    if request.method == 'POST':
           answer=request.POST.get('ans')
           num =request.POST.get('num')
           if answer == "yes":
                 num = num
                 prizes = ["Car", "Bike", "LED TV", "Cash ₹ 1","a Toy"]
                 random_num = random.randint(0,4)
                 system_num = random_num + 1
        
                 if int(num) == system_num:
                  context['prize'] = prizes[random_num]  # Pass the prize to the context
                  context['message'] = "You won " + prizes[random_num]
                
                 else:
                      context['message'] = "Bad Luck!! Try next time!"
           else:
                      context['message'] = "You  Select No  play Option"   
       
    return render(request,'play.html',context)
   
    
        
        
    
    