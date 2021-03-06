from django import forms
from enboard.models import Enquestion, Enanswer

# 폼
# 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기위해 사용하는 클래스
# 필수 파라미터의 값이 누락되지 않았는지 형식은 적절한지를 검증할 목적으로 사용
# HTML의 자동생성, 연결된 모뎋을 이용해서 데이터를 저장할 수 도 있음.

# 메타클래스
# 클래스안의 클래스
# 메타클래스의 사용이유: 클래스를 동적으로 사용하고 싶을때
#                    클래스를 원하는 방향으로 쉽게 컨트롤하고 싶을때.(커스텀 메타클래스)
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Enquestion # 사용할 모델의 연결
        fields = ['subject', 'content'] # QuestionForm 클래스에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }
# 21.09.26 곽혁 질문폼 작성
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Enanswer # 사용할 모델의 연결
        fields = ['content'] # AnswerForm 클래스에서 사용할 Answer 모델의 속성

        labels = {
            'content': '답변',
        }