# Generated by Django 4.1 on 2023-07-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_student_phonenumber_alter_student_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='a@a.com', max_length=254),
        ),
    ]
