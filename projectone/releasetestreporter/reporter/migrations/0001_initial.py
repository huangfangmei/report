# Generated by Django 4.1.5 on 2023-02-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfomation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('function_bug', models.IntegerField(max_length=50, verbose_name='功能问题个数')),
                ('need_bug', models.IntegerField(max_length=50, verbose_name='新增需求个数')),
                ('data_bug', models.IntegerField(max_length=50, verbose_name='数据问题个数')),
                ('environment_bug', models.IntegerField(max_length=50, verbose_name='环境问题个数')),
                ('performance_bug', models.IntegerField(max_length=50, verbose_name='数据问题个数')),
                ('ui_bug', models.IntegerField(max_length=50, verbose_name='数据问题个数')),
                ('compatibility_bug', models.IntegerField(max_length=50, verbose_name='数据问题个数')),
                ('high_bug', models.IntegerField(max_length=50, verbose_name='致命问题个数')),
                ('serious_bug', models.IntegerField(max_length=50, verbose_name='严重问题个数')),
                ('general_bug', models.IntegerField(max_length=50, verbose_name='中等问题个数')),
                ('minor_bug', models.IntegerField(max_length=50, verbose_name='轻微问题个数')),
                ('legacy_bug', models.IntegerField(max_length=50, verbose_name='遗留问题个数')),
                ('impact', models.CharField(max_length=50, verbose_name='遗留问题影响')),
                ('solutions', models.CharField(max_length=50, verbose_name='解决措施')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, verbose_name='姓名')),
                ('passwd', models.CharField(max_length=25, verbose_name='密码')),
                ('position', models.CharField(max_length=50, verbose_name='职位')),
                ('permission', models.IntegerField(max_length=10, verbose_name='权限类型')),
                ('ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.IntegerField(max_length=10, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reporter_name', models.CharField(max_length=100, verbose_name='报告名称')),
                ('needs_address', models.CharField(max_length=500, verbose_name='需求地址')),
                ('dev_address', models.CharField(max_length=500, verbose_name='技术地址')),
                ('test_address', models.CharField(max_length=500, verbose_name='测试用例地址')),
                ('test_num', models.IntegerField(max_length=500, verbose_name='测试用例条数')),
                ('test_pass_num', models.IntegerField(max_length=500, verbose_name='测试用例通过条数')),
                ('test_no_pass_num', models.IntegerField(max_length=500, verbose_name='测试用例不通过条数')),
                ('bug_id', models.IntegerField(max_length=500, verbose_name='bug信息id')),
                ('api_automation', models.IntegerField(max_length=30, verbose_name='接口自动化执行通过率')),
                ('ui_automation', models.IntegerField(max_length=30, verbose_name='UI自动化执行通过率')),
                ('data_configuration', models.IntegerField(max_length=30, verbose_name='数据库配置情况')),
                ('url_configuration', models.IntegerField(max_length=30, verbose_name='url配置情况')),
                ('task_configuration', models.IntegerField(max_length=30, verbose_name='定时任务配置情况')),
                ('versions', models.CharField(max_length=30, verbose_name='版本')),
                ('release_be', models.CharField(max_length=30, verbose_name='后端发版人')),
                ('release_fe', models.CharField(max_length=30, verbose_name='前端发版人')),
                ('release_qa', models.CharField(max_length=30, verbose_name='测试发版人')),
                ('release_pm', models.CharField(max_length=30, verbose_name='pm发版人')),
                ('release_maintenance', models.CharField(max_length=30, verbose_name='运维发版人')),
                ('ctime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('status', models.IntegerField(max_length=30, verbose_name='发布状态：0未发布，1已发布')),
                ('is_delete', models.IntegerField(max_length=10, verbose_name='是否删除')),
            ],
        ),
    ]
