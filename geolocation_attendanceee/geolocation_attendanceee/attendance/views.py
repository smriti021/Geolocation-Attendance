from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm  

@login_required
def home(request):
    return render(request, 'attendance/home.html')

@login_required
def mark_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = Attendance(
                user=request.user,
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude']
            )
            attendance.save()
            return redirect('attendance_success')
    else:
        form = AttendanceForm()
    
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')

@login_required
def view_attendance(request):
    attendances = Attendance.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'attendance/view_attendance.html', {'attendances': attendances})
