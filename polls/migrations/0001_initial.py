# Generated by Django 2.0 on 2017-12-20 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('MATH', 'Математика'), ('ENGLISH', 'Английский')], help_text='Subject polls prepared for', max_length=100)),
                ('grade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')], help_text='Grade polls prepared for')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Question text', max_length=100)),
                ('answer', models.CharField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, 'Затрудняюсь ответить')], help_text='Learner answer', max_length=100, null=True)),
                ('quiz', models.ForeignKey(help_text='Poll question belongs to', on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
    ]
