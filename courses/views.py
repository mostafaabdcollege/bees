from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Exercise
from .forms import CourseForm, ExerciseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from accounts.models import Profile
# عرض الدورات
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# إضافة تمرين
@login_required
def add_exercise(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if hasattr(request.user, 'profile') and request.user.profile.user_type in [1, 2]:
        if request.method == 'POST':
            form = ExerciseForm(request.POST)
            if form.is_valid():
                exercise = form.save(commit=False)
                exercise.course = course
                exercise.save()
                messages.success(request, "Exercise added successfully!")
                return redirect('course_detail', course_id=course.id)
        else:
            form = ExerciseForm()
        return render(request, 'courses/add_exercise.html', {'form': form, 'course': course})
    messages.error(request, "You are not authorized to create exercises.")
    return redirect('course_list')

# عرض تفاصيل الدورة بما في ذلك التمارين
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    exercises = Exercise.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {'course': course, 'exercises': exercises})

# التقديم للتمرين
@login_required
def submit_answer(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    course = exercise.course
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == exercise.correct_answer:
            messages.success(request, "Correct!")
        else:
            messages.error(request, "Wrong answer. Try again!")
        return redirect(reverse('course_detail', kwargs={'course_id': course.id}))

# إضافة دورة
@login_required
def add_course(request):
    if hasattr(request.user, 'profile') and request.user.profile.user_type in [1, 2]:
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = form.save(commit=False)
                course.teacher = request.user
                course.save()
                messages.success(request, "Course added successfully!")
                return redirect('course_list')
        else:
            form = CourseForm()
        return render(request, 'courses/add_course.html', {'form': form})
    messages.error(request, "You are not authorized to add courses.")
    return redirect('course_list')

# تعديل دورة
@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.teacher != request.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this course.")
        return redirect('course_list')

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form})

# حذف دورة
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user)
    if hasattr(request.user, 'profile') and request.user.profile.user_type in [1, 2]:
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('course_list')
    messages.error(request, "You are not authorized to delete this course.")
    return redirect('course_list')

# عرض لوحة القيادة
@login_required
def tableau_de_bord(request):
    if hasattr(request.user, 'profile') and request.user.profile.user_type in [1, 2]:
        courses = Course.objects.prefetch_related('exercises').all()
        return render(request, 'courses/tableau_de_bord.html', {'courses': courses})
    return redirect('home')
#dashboard
@login_required
def dashboard(request):
    # جلب الدورات والتمارين
    courses = Course.objects.all()
    exercises = Exercise.objects.all()

    # إظهار آخر 5 دورات
    latest_courses = courses[:5]

    # حساب عدد المستخدمين حسب النوع
    total_students = Profile.objects.filter(user_type=1).count()  # الطلاب
    total_teachers = Profile.objects.filter(user_type=2).count()  # المدرسون
    total_admins = Profile.objects.filter(user_type=3).count()  # الإداريون

    # تمرير البيانات إلى القالب
    return render(request, 'courses/dashboard.html', {
        'courses': courses,
        'exercises': exercises,
        'latest_courses': latest_courses,
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_admins': total_admins,
    })
