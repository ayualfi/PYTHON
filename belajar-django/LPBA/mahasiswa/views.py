from django.shortcuts import render

# Create your views here.
def beranda(request):
  return render(request, 'mahasiswa/beranda.html')
def about(request):
  return render(request, 'mahasiswa/about.html')
def news(request):
  return render(request, 'mahasiswa/news.html')
def contact(request):
  return render(request, 'mahasiswa/contact.html')
def achievement(request):
  return render(request, 'mahasiswa/achievement.html')
def education(request):
  return render(request, 'mahasiswa/education.html')
def family(request):
  
  return render(request, 'mahasiswa/family.html')
def product(request):
  return render(request, 'mahasiswa/product.html')
def skill(request):
  return render(request, 'mahasiswa/skill.html')
def others(request):
  return render(request, 'mahasiswa/others.html')

