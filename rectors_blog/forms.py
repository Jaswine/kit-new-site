from django.forms import ModelForm, ValidationError
from .models import RectorsBlogQuestionAnswerModel
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings

""" Блог Ректора Вопрос - Ответ """
class RectorsBlogQuestionAnswerForm(ModelForm):
    recaptcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY
    )
    class Meta:
        model = RectorsBlogQuestionAnswerModel
        fields = ['firstName', 'lastName', 'email', 'question']
