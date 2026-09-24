
# Register your models here.
from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from .models import Document, Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'created_by', 'is_official', 'updated_at')
    list_filter = ('status', 'category', 'is_official')
    search_fields = ('name', 'description')
    fields = (
        'name', 'description', 'category', 'structure',
        'created_by', 'status', 'reviewed_by', 'review_note', 'is_official',
        'created_at', 'updated_at',
    )
    # Statut verrouillé au formulaire : on passe uniquement par les actions ci-dessous
    readonly_fields = ('created_by', 'status', 'reviewed_by', 'created_at', 'updated_at')
    actions = ['approve_templates', 'reject_templates', 'archive_templates']

    @admin.action(description='Approuver et publier')
    def approve_templates(self, request, queryset):
        count = 0
        for template in queryset:
            try:
                template.approve(request.user)
            except ValidationError:
                pass  # statut incompatible -> ignoré silencieusement
            else:
                count += 1
        messages.success(request, f"{count} modèle(s) publié(s).")

    @admin.action(description='Rejeter (remplir review_note avant)')
    def reject_templates(self, request, queryset):
        count = 0
        for template in queryset:
            try:
                template.reject(request.user, template.review_note)
            except ValidationError:
                pass
            else:
                count += 1
        messages.success(request, f"{count} modèle(s) rejeté(s).")

    @admin.action(description='Archiver')
    def archive_templates(self, request, queryset):
        count = 0
        for template in queryset:
            try:
                template.archive(request.user)
            except ValidationError:
                pass
            else:
                count += 1
        messages.success(request, f"{count} modèle(s) archivé(s).")


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'template', 'updated_at')
    list_filter = ('owner',)
    search_fields = ('title',)
    readonly_fields = ('owner', 'created_at', 'updated_at')
