from django.contrib import admin
from .models import Applicant, ApplicationStatus, Interviewer, InterviewScore
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from datetime import datetime

from unfold.admin import ModelAdmin, TabularInline


class CreatedYearFilter(admin.SimpleListFilter):
    title = "申请年份"
    parameter_name = "created_year"

    def lookups(self, request, model_admin):
        return (
            ("2025", "2025年"),
            ("2026", "2026年"),
            ("2027", "2027年"),
        )

    def queryset(self, request, queryset):
        year = self.value()
        if year:
            return queryset.filter(created_at__year=int(year))
        return queryset

# to make the user and group use Unfold's UserAdmin and GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class ListInterviewScoreInline(TabularInline):
    model = InterviewScore
    fk_name = "application"
    fields = ["interviewer", "score", "comment"]
    readonly_fields = ["interviewer", "score", "comment"]
    can_delete = False
    show_change_link = True
    extra = 0
    verbose_name = "查看面试评分"
    verbose_name_plural = "查看面试评分"
    
    def has_add_permission(self, request, obj):
        return False

class AddInterviewScoreInline(TabularInline):
    model = InterviewScore
    fk_name = "application"
    extra = 0
    fields = ["interviewer", "score", "comment"]
    can_delete = False
    max_num = 1
    
    verbose_name = "添加面试评分"
    verbose_name_plural = "添加面试评分"
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.none()

# Register your models here.
class ApplicantAdmin(ModelAdmin):
    search_fields = ('name', 'school', 'major', 'phone', 'email')
    list_display = ('name', 'email', 'phone', 'wechat', 'school', 'major', 'grade', 'sex', 'region', 'first_choice', 'second_choice', 'third_choice', 'has_experience', 'experience_detail', 'self_intro', 'disposable_time', 'id', 'src', 'created_at')
    list_filter = ('grade', 'first_choice', 'second_choice', 'third_choice', 'sex', 'has_experience', 'src', CreatedYearFilter)
    fields = ['name', 'email', 'phone', 'wechat', 'school', 'major', 'grade', 'sex', 'region', ('first_choice', 'second_choice', 'third_choice'), ('has_experience', 'experience_detail'), 'self_intro', 'disposable_time', 'src', ('created_at', 'modified_at')]
    readonly_fields = ['created_at', 'modified_at']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        query = Q()
        depts = ("FAL", "IT", "LIA",
                 "PR", "HR", "CM", "TUT")
        
        for g in request.user.groups.all():
            print(g.name)
            if g.name in depts:
                query.add(Q(first_choice=g.name), Q.OR)
                query.add(Q(second_choice=g.name), Q.OR)
            elif g.name == "ALL":
                return qs
        if len(query) == 0:
            return qs.none()
        return qs.filter(query)
    
class ApplicationStatusAdmin(ModelAdmin):
    search_fields = ('applicant', )
    list_display = ('applicant','status', 'interview_time', 'writiing_task_score', 'avgInterviewScore', 'totalScore', 'handle_by',)
    list_filter = ('handle_by', 'status')
    readonly_fields = ["writing_task_file", "writing_task_video_link"]
    list_per_page = 30
    fields = ["applicant", ("status", "handle_by"), "writing_task_ddl",
              ("writing_task_file", "writing_task_video_link"),
              "interview_time", ("interviewer", "interview_uploaded_to_feishu"),
              ("writiing_task_score", "writing_task_comment"),
              "remark"]
    raw_id_fields = ('applicant', )
    autocomplete_fields = ('interviewer', )
    actions = ['send_writing_task_email','check_writing_task_expired', 'send_interview_email', 'send_decision_email', ]
    
    inlines = [
        ListInterviewScoreInline,
        AddInterviewScoreInline,
    ]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        query = Q()
        depts = ("FAL", "IT", "LIA",
                 "PR", "HR", "CM", "TUT")
        
        for g in request.user.groups.all():
            print(g.name)
            if g.name in depts:
                query.add(Q(handle_by=g.name), Q.OR)
            elif g.name == "ALL":
                return qs        
        if len(query) == 0:
            return qs.none()
        return qs.filter(query)
    
    
    def get_readonly_fields(self, request, obj=None):
        fields = super(ApplicationStatusAdmin, self).get_readonly_fields(request)
        fields_to_add = ["handle_by", "applicant"]
        if obj:
            for f in fields_to_add:
                if f in fields:
                    continue
                fields.append(f)
        else:
            for f in fields_to_add:
                if f in fields:
                    fields.remove(f)
        return fields
    
    def get_actions(self, request):
        actions = super(ApplicationStatusAdmin, self).get_actions(request)
        if not request.user.has_perm('backend.send_decision_email'):
            del actions["send_decision_email"]
        return actions
    
    def send_writing_task_email(self, request, queryset):
        all_success = True
        self.message_user(request, "处理中...", level=messages.INFO)
        for application in queryset:
           all_success = all_success and application.send_writing_task_email()
        if all_success:
            self.message_user(request, "全部笔试邮件发送成功")
        else:
            self.message_user(request, "某些笔试邮件发送失败", level=messages.WARNING)
    send_writing_task_email.short_description = "向选择的申请发送笔试邮件"
    
    def check_writing_task_expired(self, request, queryset):
        queryset.filter(status="WRTIING_TASK_EMAIL_SENT")\
            .filter(writing_task_ddl__lt=timezone.now())\
            .update(status="WRTIING_TASK_EXPIRED")
        self.message_user(request, "已检查过期", level=messages.INFO)
    check_writing_task_expired.short_description = "对选择的申请检查笔试过期"
            
    
    def send_interview_email(self, request, queryset):
        all_success = True
        self.message_user(request, "处理中...", level=messages.INFO)

        for application in queryset:
            all_success = all_success and application.send_interview_email()
        if all_success:
            self.message_user(request, "全部面试邮件发送成功")
        else:
            self.message_user(request, "某些面试邮件发送失败", level=messages.WARNING)
    send_interview_email.short_description = "向选择的申请发送面试邮件"
    
    def send_decision_email(self, request, queryset):
        all_success = True
        self.message_user(request, "处理中...", level=messages.INFO)

        for application in queryset:
            all_success = all_success and application.send_decision_email()
        if all_success:
            self.message_user(request, "全部录取邮件发送成功")
        else:
            self.message_user(request, "某些录取邮件发送失败", level=messages.WARNING)
    send_decision_email.short_description = "向选择的申请发送录取/拒绝邮件"
    
    
class InterviewerAdmin(ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'department', "meeting_link")
    

class InterviewScoreAdmin(ModelAdmin):
    search_fields = ('application', 'interviewer')
    list_display = ('application', 'interviewer', 'score', 'comment')
    list_filter = ('interviewer', )
    fields = ['application', 'interviewer', 'score', 'comment']
    readonly_fields = ['application', 'interviewer']
    list_per_page = 30

admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
admin.site.register(Interviewer, InterviewerAdmin)
admin.site.register(InterviewScore, InterviewScoreAdmin)

admin.site.disable_action('delete_selected')
