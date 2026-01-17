from django import forms
import markdown


class BlogCreateForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=127)
    reading_minute = forms.IntegerField(min_value=1, max_value=120)
    content_markdown = forms.CharField(min_length=1)
    tg_link = forms.URLField()
    is_published = forms.BooleanField(required=False)

    def clean_content_markdown(self):
        data = self.cleaned_data["content_markdown"]

        try:
            content_html = markdown.markdown(data)
            self.cleaned_data['content_html'] = content_html
            return data
        except:
            raise forms.ValidationError('markdown xato yozildi')


class BlogSearchForm(forms.Form):
    search = forms.CharField(min_length=5, max_length=20)
