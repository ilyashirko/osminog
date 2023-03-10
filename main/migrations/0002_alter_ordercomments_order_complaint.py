# Generated by Django 4.1.7 on 2023-02-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercomments',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='main.order', verbose_name='комментарий'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.TextField(blank=True, verbose_name='Текст жалобы')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ на жалобу')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Жалоба подана')),
                ('closed_at', models.DateTimeField(db_index=True, verbose_name='Жалоба закрыта')),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='main.order', verbose_name='жалоба')),
                ('admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='main.owner', verbose_name='админ')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='complaints', to='main.manager', verbose_name='менеджер')),
            ],
        ),
    ]
