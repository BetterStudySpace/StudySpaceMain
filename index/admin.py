from django.contrib import admin
from .models import Post
from .models import Library
from .models import Floor

admin.site.register(Post)
admin.site.register(Library)
admin.site.register(Floor)