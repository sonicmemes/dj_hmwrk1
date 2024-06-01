from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes = [form for form in self.forms if form.cleaned_data.get('is_main', False)]
        if len(main_scopes) < 1:
            raise ValidationError('Укажите основной раздел.')
        if len(main_scopes) > 1:
            raise ValidationError('Основным может быть только один раздел.')
        return super().clean()
    # def save(self, commit=True):
    #     main_scopes = [form for form in self.forms if form.cleaned_data.get('is_main', False)]
    #     if len(main_scopes) > 1:
    #         raise ValidationError('Основным может быть только один раздел.')
    #     return super().save(commit)


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1  # Количество дополнительных полей, которые будут отображаться


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
