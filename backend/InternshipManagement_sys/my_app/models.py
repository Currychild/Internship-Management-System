from django.db import models

# Create your models here.
# Academy Model (for the 'academy' table)

class Academy(models.Model):
    a_id = models.IntegerField(primary_key=True, verbose_name='院系Id')
    a_name = models.CharField(max_length=20, verbose_name='院系名称')
    a_profile = models.CharField(max_length=255, verbose_name='院系简介')
    a_dean = models.CharField(max_length=20, verbose_name='院长')
    a_establishdate = models.DateField(verbose_name='成立日期')
    a_conceldate = models.DateField(null=True, blank=True, verbose_name='撤销日期')
    a_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    a_modifier_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='academy_modifier')

    class Meta:
        db_table = 'academy'
        verbose_name = '学院'
        verbose_name_plural = '学院'


class Major(models.Model):
    m_id = models.IntegerField(primary_key=True, verbose_name='专业ID')
    a_id = models.ForeignKey(Academy, on_delete=models.CASCADE, verbose_name='所属院系id')
    m_name = models.CharField(max_length=20, verbose_name='专业名称')
    m_profile = models.CharField(max_length=255, verbose_name='专业简介')
    m_trainingplan = models.BinaryField(verbose_name='培养计划pdf')
    m_establishdate = models.DateField(verbose_name='成立日期')
    m_conceldate = models.DateField(null=True, blank=True, verbose_name='撤销日期')
    m_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    m_modifier_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='major_modifier')
    class Meta:
        db_table = 'major'
        verbose_name = '专业'
        verbose_name_plural = '专业'


class Teacher(models.Model):
    t_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='老师ID',primary_key=True)
    c_id = models.IntegerField(verbose_name='管理班级ID')
    t_type = models.IntegerField(verbose_name='是否班主任', choices=[(0, '不是班主任'), (1, '是班主任')])

    class Meta:
        db_table = 'teacher'
        verbose_name = '校内导师'
        verbose_name_plural = '校内导师'


class Class(models.Model):
    c_id = models.IntegerField(primary_key=True, verbose_name='班级id')
    m_id = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name='专业ID')
    t_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='班主任Id')
    act_id = models.IntegerField(null=True, blank=True, verbose_name='活动ID')
    c_name = models.CharField(max_length=20, verbose_name='班级名称')
    c_profile = models.CharField(max_length=255, verbose_name='班级简介')
    c_enrollmentyear = models.IntegerField(verbose_name='入学年份')
    c_degree = models.CharField(max_length=20, verbose_name='学历层次')
    c_studentnumber = models.IntegerField(verbose_name='学生人数')
    c_lastmodifytime = models.DateTimeField(verbose_name='最后修改时间')
    c_modifier_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='class_modifier')

    class Meta:
        db_table = 'class'
        verbose_name = '班级'
        verbose_name_plural = '班级'


class Student(models.Model):
    s_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='学生ID', primary_key=True)
    c_id = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='班级ID')
    s_grade = models.CharField(max_length=20, verbose_name='学生年级')
    s_state = models.BinaryField(verbose_name='实习状态，0为否，1为是')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = '学生'


class Announcement(models.Model):
    an_id = models.IntegerField(primary_key=True, verbose_name='公告id')
    an_publisher_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='announcement_publisher')
    an_title = models.CharField(max_length=200, verbose_name='公告标题')
    an_content = models.TextField(verbose_name='公告内容')
    an_topddl = models.DateField(verbose_name='置顶截止时间')
    an_validityddl = models.DateField(verbose_name='有效期截止日期')
    an_releasetime = models.DateTimeField(verbose_name='发布时间')
    an_viewcount = models.IntegerField(verbose_name='浏览量')

    class Meta:
        db_table = 'announcement'
        verbose_name = '公告'
        verbose_name_plural = '公告'


class Company(models.Model):
    co_id = models.IntegerField(primary_key=True, verbose_name='企业ID')
    co_name = models.CharField(max_length=20, verbose_name='企业名称')
    co_address = models.CharField(max_length=45, verbose_name='企业地址')
    co_contacts = models.CharField(max_length=45, verbose_name='联系人')
    co_scale = models.IntegerField(verbose_name='企业规模')

    class Meta:
        db_table = 'company'
        verbose_name = '企业'
        verbose_name_plural = '企业'


class CompanyTeacher(models.Model):
    cot_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='企业导师ID', primary_key=True)
    co_id = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='企业ID')
    act_id = models.IntegerField(null=True, blank=True, verbose_name='管理的实习活动id')
    cot_title = models.CharField(max_length=45, verbose_name='职称/头衔')

    class Meta:
        db_table = 'company_teacher'
        verbose_name = '企业导师'
        verbose_name_plural = '企业导师'


class IpActivity(models.Model):
    act_id = models.IntegerField(primary_key=True, verbose_name='实习活动id')
    co_id = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='企业id')
    act_name = models.CharField(max_length=255, verbose_name='实习活动名称')
    act_description = models.CharField(max_length=255, verbose_name='实习活动描述')
    act_begindate = models.DateField(verbose_name='实习开始日期')
    act_enddate = models.DateField(verbose_name='实习结束日期')

    class Meta:
        db_table = 'ip_activity'
        verbose_name = '实习活动'
        verbose_name_plural = '实习活动'


class IpApplication(models.Model):
    appl_id = models.IntegerField(primary_key=True, verbose_name='实习申请表id')
    s_id = models.IntegerField(verbose_name='学生id')
    j_id = models.IntegerField(verbose_name='实习岗位id')
    appl_resume = models.BinaryField(verbose_name='简历pdf')
    appl_choice = models.IntegerField(verbose_name='志愿编号')
    appl_status = models.IntegerField(verbose_name='申请表状态')

    class Meta:
        db_table = 'ip_application'
        verbose_name = '实习申请'
        verbose_name_plural = '实习申请'


class IpJob(models.Model):
    j_id = models.IntegerField(primary_key=True, verbose_name='岗位ID')
    act_id = models.ForeignKey(IpActivity, on_delete=models.CASCADE, verbose_name='实习活动ID')
    co_id = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='公司ID')
    j_name = models.CharField(max_length=20, verbose_name='岗位名称')
    j_description = models.CharField(max_length=255, verbose_name='岗位描述')
    j_salary = models.FloatField(verbose_name='实习工资')
    j_type = models.CharField(max_length=45, verbose_name='岗位类型')
    j_begindate = models.DateField(verbose_name='开始时间')
    j_enddate = models.DateField(verbose_name='结束时间')
    j_count = models.IntegerField(verbose_name='人数限制')

    class Meta:
        db_table = 'ip_job'
        verbose_name = '实习岗位'
        verbose_name_plural = '实习岗位'


class IpSummary(models.Model):
    sm_id = models.IntegerField(primary_key=True, verbose_name='实习总结id')
    s_id = models.IntegerField(verbose_name='学生ID')
    t_id = models.IntegerField(verbose_name='校内导师id')
    cot_id = models.IntegerField(verbose_name='企业导师id')
    sm_submissiontime = models.DateTimeField(verbose_name='提交时间')
    sm_content = models.BinaryField(verbose_name='实习总结pdf')
    sm_t_score = models.IntegerField(null=True, blank=True, verbose_name='校内导师给分')
    sm_ct_score = models.IntegerField(null=True, blank=True, verbose_name='企业导师给分')
    t_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='校内导师评语')
    cot_comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='企业导师评语')
    sm_status = models.IntegerField(verbose_name='状态')

    class Meta:
        db_table = 'ip_summary'
        verbose_name = '实习总结'
        verbose_name_plural = '实习总结'


class IpWeekly(models.Model):
    w_id = models.IntegerField(primary_key=True, verbose_name='实习周报id')
    s_id = models.IntegerField(verbose_name='学生ID')
    t_id = models.IntegerField(verbose_name='校内导师id')
    cot_id = models.IntegerField(verbose_name='企业导师id')
    w_content = models.BinaryField(verbose_name='周报pdf')
    w_time = models.CharField(max_length=45, verbose_name='实习周次')
    w_submissiontime = models.DateTimeField(verbose_name='周报提交时间')
    w_status = models.IntegerField(default=0, verbose_name='周报状态')
    w_t_score = models.IntegerField(null=True, blank=True, verbose_name='校内导师评分')
    w_ct_score = models.IntegerField(null=True, blank=True, verbose_name='企业导师评分')

    class Meta:
        db_table = 'ip_weekly'
        verbose_name = '实习周报'
        verbose_name_plural = '实习周报'


class User(models.Model):
    u_id = models.IntegerField(primary_key=True, verbose_name='用户ID')
    u_name = models.CharField(max_length=20, verbose_name='用户名（姓名）')
    u_password = models.CharField(max_length=20, default='123456', verbose_name='密码')
    u_type = models.IntegerField(verbose_name='用户类型', choices=[(0, '管理员'), (1, '学生'), (2, '班主任'), (3, '企业导师')])
    u_tel = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    u_photo = models.BinaryField(null=True, blank=True, verbose_name='照片')
    u_status = models.IntegerField(default=0, verbose_name='激活状态，0为未激活，1为已激活')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户'