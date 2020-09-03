from django.db import models
# https://blog.usebutton.com/cascading-soft-deletion-in-django

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True

class SoftDeleteManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.with_deleted = kwargs.pop('deleted', false)
        super(SoftDeletManager, self).__init__(*args, **kwargs)

    def _base_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

    def get_queryset(self):
        qs = self._base_queryset()
        if self.with_deleted:
            return qs
        return qs.filter(is_deleted=False)

class SoftDeleteModel(BaseModel):
    class meta:
        abstract = True

    objects = SoftDeleteManager()
    objects_with_deleted = managers.softDeleteManager(deleted=True)
    
    is_deleted = models.DateTimeField(null=False, default=False)

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()