# Generated to restore the LiteratureReview table in the database schema.

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_add_group_guide'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LiteratureReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_1', models.FileField(upload_to='literature_review_documents/')),
                ('file_2', models.FileField(upload_to='literature_review_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('guide_approved', models.BooleanField(default=False)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='literature_review', to='core.group')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_literature_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
