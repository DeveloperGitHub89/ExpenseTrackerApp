from django.shortcuts import render,redirect
from .models import User,Expense,Income
# Create your views here.

def openDashboard(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        expenses=user.expense_set.all()
        incomes=user.income_set.all()
        totalExpense=0
        totalIncome=0
        for expense in expenses:
            totalExpense+=expense.amount
        for income in incomes:
            totalIncome+=income.amount
        netBalance=totalIncome-totalExpense
        return render(request,"Dashboard.html",{"net_balance":netBalance,"user":user,"total_expenses":totalExpense,"total_incomes":totalIncome})

    else:
        return redirect('/')
    
def recordExpense(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        exp=Expense()
        exp.amount=request.POST['amount']
        exp.date=request.POST['date']
        exp.time=request.POST['time']
        exp.category=request.POST['category']
        exp.remarks=request.POST['remark']
        exp.user=user
        exp.save()
        return redirect('/dashboard')

    else:
        return redirect('/')

def recordIncome(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        exp=Income()
        exp.amount=request.POST['amount']
        exp.date=request.POST['date']
        exp.time=request.POST['time']
        exp.category=request.POST['category']
        exp.remarks=request.POST['remark']
        exp.user=user
        exp.save()
        return redirect('/dashboard')

    else:
        return redirect('/')
    
def fetchAllExpenses(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        expenses=user.expense_set.all()
        return render(request,"ExpensesList.html",{"expenses":expenses}) 

    else:
        return redirect('/')

def fetchAllIncomes(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        incomes=user.income_set.all()
        return render(request,"IncomeList.html",{"incomes":incomes}) 

    else:
        return redirect('/')

    
def openLoginForm(request):
    if 'userid' in request.session:
        return redirect('/dashboard')
    return render(request,"Login.html")

def performLogin(request):
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.filter(email=email,password=password)
    if user:
        list=user.values()
        request.session['userid']=list[0]['id']
        return redirect('/dashboard')
    else:
        return render(request,"Login.html",{"error":"Invalid email or password"})

def logout(request):
    del request.session['userid']
    return redirect('/')

def openExpenseForm(request):
    if 'userid' in request.session:
        return render(request,"ExpenseForm.html")
    else:
        return redirect('/')
    

def openIncomeForm(request):
    return render(request,"IncomeForm.html")

def openUserForm(request):
    return render(request,"UserForm.html")

def registerUser(request):
    user=User()
    user.name=request.POST['name']
    user.email=request.POST['email']
    user.phone=request.POST['phone']
    user.password=request.POST['password']
    user.save()
    return redirect('/')