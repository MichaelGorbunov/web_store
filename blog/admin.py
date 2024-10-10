from django.contrib import admin
from django.contrib import admin
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Job  # Import your Job model
# Register your models here.
from .models import Post
from apscheduler.triggers.cron import CronTrigger
from .models import CronJob
from .apps import scheduler

admin.site.register(Post)



# scheduler = BackgroundScheduler()
# scheduler.start()

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'name','interval')

    actions = ['stop_job','start_job']

    def stop_job(self, request, queryset):
        for job in queryset:
            try:
                scheduler.remove_job(job.job_id)  # Remove the job using its ID
                self.message_user(request, f"Job {job.job_id} stopped successfully.")
            except Exception as e:
                self.message_user(request, f"Failed to stop job {job.job_id}: {str(e)}", level='error')

    stop_job.short_description = "Stop selected jobs"

    # actions = []

    def start_job(self, request, queryset):
        for job in queryset:
            try:
                # Define the job function
                def job_function():
                    print(f"Job {job.name} is running...")

                # Schedule the job
                scheduler.add_job(job_function, 'interval', seconds=job.interval, id=job.job_id)
                # scheduler.start()

                self.message_user(request, f"Job {job.job_id} started successfully.")
            except Exception as e:
                self.message_user(request, f"Failed to start job {job.job_id}: {str(e)}", level='error')

    start_job.short_description = "Start selected jobs"


class CronJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'name', 'minute', 'hour', 'day', 'month', 'day_of_week')

    actions = ['start_job', 'stop_job']

    def start_job(self, request, queryset):
        for job in queryset:
            try:
                # Define the job function
                def job_function():
                    print(f"Job {job.name} is running...")

                # Schedule the job using CronTrigger
                trigger = CronTrigger(
                    minute=job.minute,
                    hour=job.hour,
                    day=job.day,
                    month=job.month,
                    day_of_week=job.day_of_week
                )
                scheduler.add_job(job_function, trigger, id=job.job_id)
                self.message_user(request, f"Job {job.job_id} started successfully.")
            except Exception as e:
                self.message_user(request, f"Failed to start job {job.job_id}: {str(e)}", level='error')

    start_job.short_description = "Start selected cron jobs"

    def stop_job(self, request, queryset):
        for job in queryset:
            try:
                scheduler.remove_job(job.job_id)
                self.message_user(request, f"Job {job.job_id} stopped successfully.")
            except Exception as e:
                self.message_user(request, f"Failed to stop job {job.job_id}: {str(e)}", level='error')

    stop_job.short_description = "Stop selected cron jobs"





admin.site.register(Job, JobAdmin)
admin.site.register(CronJob, CronJobAdmin)