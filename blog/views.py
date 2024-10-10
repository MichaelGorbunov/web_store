from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from apscheduler.events import EVENT_JOB_ADDED, EVENT_JOB_REMOVED, EVENT_JOB_EXECUTED
from datetime import datetime


class PostCreateView(CreateView):
    """создание поста"""
    model = Post
    fields = ['title', 'body', 'preview']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts_list')


class PostListView(ListView):
    """список постов"""
    model = Post

    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # queryset = super().get_queryset().filter(published=True)
        # return queryset.order_by("-id")
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """детальное описание поста"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # def get_object(self):
    #     # Переопределение метода get_object
    #     obj = super().get_object()
    #     obj.views_count = obj.views_count + 1
    #     obj.save()
    #     return obj

    def get_object(self, queryset=None):
        # Переопределение метода get_object
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    """обновление поста"""
    model = Post
    fields = ["title", "body", "published", "preview", "views_count"]
    template_name = 'blog/post_form.html'

    # success_url = reverse_lazy('blog:posts_list')
    # def get_success_url(self):
    #     pk = self.kwargs["pk"]
    #     return reverse_lazy("blog:post_detail", kwargs={"pk": pk})
    def get_success_url(self):
        return reverse_lazy("blog:post_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    """удаление поста"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')


class PostList2View(ListView):
    """список постов"""
    model = Post
    paginate_by = 3

    template_name = 'blog/posts_list2.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # queryset = super().get_queryset().filter(published=True)
        # return queryset.order_by("-id")
        return Post.objects.filter(published=True)






def job_listener(event):
    if event.exception:
        print(f'Job {event.job_id} failed.')
    else:
        print(f'Job {event.job_id} **.')
        print(f'Job {event} **.')


# def clean_jobstore(scheduler):
#     # Удаляем все задачи из jobstore
#     # scheduler.remove_all()
#     scheduler.remove_all_jobs()
#
#     print("Jobstore cleaned.")


# 'cron' Mode cycle, week 1 To the week 5 , every day 9:30:10 Execute ,id For work ID As a mark
# ('scheduler',"interval", seconds=1) # Use interval Mode loop, every 1 Second execution 1 Times
# print(scheduler.get_job('task_time'))
# @register_job(scheduler, "interval", seconds=25, id='task_time')
# def test_job():
#     # t_now = datetime.now()
#     print("task1")
#
# def test_job2():
#     # t_now = datetime.now()
#     print("task2")
#
# def scheduled_job(param1, param2):
#     print(f"Scheduled job executed with parameters: {param1}, {param2}")

# def start_scheduler():
#     #  Instantiate scheduler
#     scheduler = BackgroundScheduler()
#     #  Scheduler uses DjangoJobStore()
#     scheduler.add_jobstore(DjangoJobStore(), "default")
#
#     # Добавляем слушателя
#     scheduler.add_listener(job_listener, EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_EXECUTED)
#
#     clean_jobstore(scheduler)

    # Пример задачи
    # scheduler.add_job(my_job, 'interval', seconds=10, id='my_job_id')
    # scheduler.add_job(
    #     scheduled_job,
    #     "interval",
    #     seconds=5,
    #     id='scheduled_job1',
    #     jobstore="default",
    #     args=['Hello', 'World'],
    #     replace_existing=True)
    #
    # scheduler.start()
    # print("Scheduler started.")


# start_scheduler()

# scheduler.add_listener(job_listener, EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_EXECUTED)
#




# scheduler.add_job(
#     test_job2,
#     "interval",
#     seconds=13,
#     id='task2_time',
#     jobstore="default",
#     replace_existing=True)

# scheduler.add_job(test_job2, 'cron', hour=13, minute='*', second='*/5' ,jitter=3,id='task2_time',jobstore="default",replace_existing=True)


#  Scheduler starts
# scheduler.start()
# print("Scheduler started.")
# scheduler.print_jobs()
# m=input("clean?")
# if m in("Y","1","Да","Yes","yes"):
#     clean_jobstore(scheduler)

# # clean_jobstore(scheduler)
# scheduler = BackgroundScheduler()
# # scheduler.add_jobstore(DjangoJobStore(), "default")
# scheduler.add_listener(job_listener, EVENT_JOB_ADDED | EVENT_JOB_REMOVED | EVENT_JOB_EXECUTED)
# scheduler.start()