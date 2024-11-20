from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from .forms import ProfileUpdateForm, UserUpdateForm, UserPostasCreateForm, PostasReviewForm, \
    UserAdvertisementCreateForm, AdvertisementReviewForm
from .models import Postai, Profile, Advertisements, Cpu, Gpu, Ram


# Create your views here.

def index(request):
    num_posts = (Postai.objects.filter(~Q(status__icontains='p'))
                 .filter(~Q(status__icontains='d')).count())
    num_users = User.objects.count()
    num_ads = Advertisements.objects.count()

    context = {"num_posts": num_posts,
               "num_users": num_users,
               "num_ads": num_ads}

    return render(request, "index.html", context=context)


class PostaiListView(generic.ListView):
    model = Postai
    context_object_name = "postai_list"
    template_name = "forum.html"


def get_postai(reqest):
    postai_s = (Postai.objects
                .filter(Q(category__icontains='s'))
                .filter(~Q(status__icontains='p'))
                .filter(~Q(status__icontains='d'))
                .order_by('-create_data')[:3])
    postai_a = (Postai.objects
                .filter(Q(category__icontains='a'))
                .filter(~Q(status__icontains='p'))
                .filter(~Q(status__icontains='d'))
                .order_by('-create_data')[:3])
    postai_p = (Postai.objects
                .filter(Q(category__icontains='p'))
                .filter(~Q(status__icontains='p'))
                .filter(~Q(status__icontains='d'))
                .order_by('-create_data')[:3])
    postai_k = (Postai.objects
                .filter(Q(category__icontains='k'))
                .filter(~Q(status__icontains='p'))
                .filter(~Q(status__icontains='d'))
                .order_by('-create_data')[:3])
    postai_r = (Postai.objects
                .filter(Q(category__icontains='r'))
                .filter(~Q(status__icontains='p'))
                .filter(~Q(status__icontains='d'))
                .order_by('-create_data')[:3])
    context = {
        'postai_s': postai_s,
        'postai_a': postai_a,
        'postai_p': postai_p,
        'postai_k': postai_k,
        'postai_r': postai_r
    }
    return render(reqest, 'forum.html', context=context)


class UserPostaiListView(LoginRequiredMixin, generic.ListView):
    model = Postai
    template_name = 'my_posts.html'
    context_object_name = 'postai'

    def get_queryset(self):
        return (Postai.objects
                .filter(creator=self.request.user)
                .filter(~Q(status='d'))
                .order_by('category'))


def get_postai_by_cat(reqest, cat):
    postai = (Postai.objects
              .filter(Q(category__icontains=cat))
              .filter(~Q(status__icontains='p'))
              .filter(~Q(status__icontains='d'))
              .order_by('-create_data'))
    context = {
        'postai': postai
    }
    return render(reqest, 'threads.html', context=context)


# def get_one_post(request, post_id):
#     post_one = get_object_or_404(Postai, pk=post_id)
#     return render(request, 'thread.html', {'post': post_one})

class ThreadDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Postai
    context_object_name = 'post'
    template_name = 'thread.html'
    form_class = PostasReviewForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.postas = self.object
        form.instance.reviewer = self.request.user

        form.save()
        return super().form_valid(form)

    # nurodom kur patenkam PO posto
    def get_success_url(self):
        return reverse('thread-one', kwargs={'pk': self.object.id})


@login_required
def profilis(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.info(request, "Profilis atnaujintas")
        else:
            messages.warning(request, "Profilis neatnaujintas")
        return redirect('profilis-url')

    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)
    more_info = Profile.objects.filter(Q(user=request.user))
    context = {
        'p_form': p_form,
        'u_form': u_form,
        'user_info': more_info
    }

    return render(request, 'profilis.html', context=context)


class PostasByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Postai
    form_class = UserPostasCreateForm
    template_name = 'new_post.html'
    success_url = '/home/forum/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.status = 'a'
        return super().form_valid(form)


class PostasByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Postai
    form_class = UserPostasCreateForm
    # fields = ('due_back',) alternatyyva  form_class
    template_name = 'new_post.html'
    success_url = '/home/forum/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.status = 'a'
        return super().form_valid(form)

    def test_func(self):  # UserPassesTestMixin dalis, patys nustatom sąlygą ar leidžiam updeitinti
        posto_object = self.get_object()
        return posto_object.creator == self.request.user


@login_required
def postas(request):
    if request.method == 'POST':
        form = UserPostasCreateForm()
        if form.is_valid():
            form.save()
            messages.info(request, "Postas atnaujintas")
        else:
            messages.warning(request, "Postas nesukurtas dėl klaidų formoje")
        return redirect('forum-main')


@csrf_protect
def register_user(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':
        # paimam duomenis iš formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.warning(request, 'Slaptažodžiai nesutampa!')

        if User.objects.filter(username=username).exists():
            messages.warning(request, f'Toks vartotojo vardas {username} jau yra!')

        if not email:
            messages.warning(request, "Email neįvestas!")

        if User.objects.filter(email=email).exists():
            messages.warning(request, f"Email {email} jau užregistruotas!")

        if messages.get_messages(request):
            return redirect('register-url')

        User.objects.create_user(username=username, email=email, password=password)
        messages.info(request, f"Vartotojas {username} sukurtas!")
        return redirect('login')


def get_advertisements(request):
    ads = Advertisements.objects.all()
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    paged_ads = paginator.get_page(page_number)
    context = {
        'advertisements': paged_ads
    }

    return render(request, 'advertisements.html', context=context)


def get_advertisements_pc(request):
    ads = (Advertisements.objects
           .filter(cpu_kiekis__gt=0)
           .filter(gpu_kiekis__gt=0)
           .filter(ram_kiekis__gt=0))
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    paged_ads = paginator.get_page(page_number)
    context = {
        'advertisements': paged_ads
    }

    return render(request, 'advertisements.html', context=context)


def get_advertisements_cpu(request):
    ads = (Advertisements.objects
           .filter(cpu_kiekis__gt=0)
           .filter(gpu_kiekis=0)
           .filter(ram_kiekis=0))
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    paged_ads = paginator.get_page(page_number)
    context = {
        'advertisements': paged_ads
    }

    return render(request, 'advertisements.html', context=context)


def get_advertisements_gpu(request):
    ads = (Advertisements.objects
           .filter(cpu_kiekis=0)
           .filter(gpu_kiekis__gt=0)
           .filter(ram_kiekis=0))
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    paged_ads = paginator.get_page(page_number)
    context = {
        'advertisements': paged_ads
    }

    return render(request, 'advertisements.html', context=context)


def get_advertisements_ram(request):
    ads = (Advertisements.objects
           .filter(cpu_kiekis=0)
           .filter(gpu_kiekis=0)
           .filter(ram_kiekis__gt=0))
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    paged_ads = paginator.get_page(page_number)
    context = {
        'advertisements': paged_ads
    }

    return render(request, 'advertisements.html', context=context)


class AdvertisementByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Advertisements
    form_class = UserAdvertisementCreateForm
    template_name = 'new-advertisement.html'
    success_url = '/home/advertisements/'

    def form_valid(self, form):
        form.instance.useris = self.request.user
        form.instance.status = 'a'
        return super().form_valid(form)


class AdvertisementDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Advertisements
    context_object_name = 'ad'
    template_name = 'advertisement.html'
    form_class = AdvertisementReviewForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.advert = self.object
        form.instance.reviewer = self.request.user

        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ad-one', kwargs={'pk': self.object.id})


def get_all_setup_parts(request):
    cpus = Cpu.objects.order_by('model')
    gpus = Gpu.objects.order_by('model')
    rams = Ram.objects.order_by('size')

    context = {"cpus": cpus,
               "gpus": gpus,
               "rams": rams}

    return render(request, "bootleneck_calc.html", context=context)
