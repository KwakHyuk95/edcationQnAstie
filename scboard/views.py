from django.shortcuts import render, get_object_or_404, redirect
from .models import Scquestion, Scanswer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
# Create your views here.

# 주석달기
# 언제 누가 뭘 위해서 작성하는지
# 메인 페이지 작성
# 질문 목록 출력
#21.09.17 곽혁 작성
def index(request):
    # Question.objects.order_by('-create_date')
    # Question 모델에서 객체를 참조하는데 / -가 붙어있으면 해당 객체를 기준으로 역순정렬
    # 역순으로 정렬해올것 (객체는 create_date)

    # 페이징처리 추가 21.09.24 곽혁

    # 페이징 처리 관련 템플릿 태그 속성. (템플릿단 페이징 처리 속성)
    # .count : 전체 게시물 개수
    # .per_page : 페이지당 보여줄 게시물 개수
    # .page_range : 페이지 범위
    # number : 현재 페이지 번호
    # previous_page_number : 이전 페이지 번호
    # previous_page_number : 다음 페이지 번호
    # has_previous : 이전 페이지 유무
    # has_next : 다음 페이지 유무
    # start_index :  현재 페이지 시작 인덱스
    # end_index :  현재 페이지 끝 인덱스

    # 페이지의 입력 파라미터 추가.

    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')
    # 조회
    # question_list = Scquestion.objects.order_by('-create_date')
    if so == "recommend":
        # annotate = 기존의 모델에 임시로 속성을 부여하는 장고의 함수
        # voter(추천수)를 카운트 받아 저장후 정렬조건에 사용.
        question_list = Scquestion.objects.annotate(num_voter=Count('voter')).order_by('-num_voter','-create_date')
    elif so =='popular':
        question_list = Scquestion.objects.annotate(num_answer=Count('scanswer')).order_by('-num_answer','-create_date')
    else:
        question_list = Scquestion.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # __icontains : 컬럼의 조회조건 부여
            Q(content__icontains=kw) |
            Q(author__first_name__icontains=kw) |
            Q(scanswer__author__first_name__icontains=kw)
        ).distinct()

    # 페이징 처리 기능 구현
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩
    page_obj = paginator.get_page(page)
    context ={'question_list': page_obj}
    # 템플릿단에 던짐 / 변수에 담지않고 던져도 상관 X
    return render(request, 'scboard/question_list.html', context) # render는 조회성


def detail(request, question_id):
    # 글의 제목과 내용 출력
    question = Scquestion.objects.get(id=question_id)
    return render(request, 'scboard/question_detail.html', {'question': question})

def mainpg(request):
    return render(request, 'main.html')

def question_modify(request, question_id):
    question = get_object_or_404(Scquestion, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('scboard:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('scboard:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'scboard/question_form.html', {'form': form})

def question_delete(request, question_id):
    question = get_object_or_404(Scquestion, pk=question_id)
    # 질문을 한 사람과 글을 작성한 사람이 같은지를 확인.
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('scboard:detail', question_id=question.id)
    question.delete()
    return redirect('scboard:index')

# @LOGIN_REQUIRED : 해당 함수가 로그인이 되어있는지를 확인하는 데코레이터
#                   만약 로그인 되어있지 않다면 해당 url을 호출
@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # request.user : 현재 로그인한 계정의
                                           #                User모델 객체.
            question.create_date = timezone.now()
            question.save()
            return redirect('scboard:index')
    else:
        form = QuestionForm()
    return render(request, 'scboard/question_form.html', {'form': form})

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Scquestion, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect('scboard:detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'scboard/question_detail.html', {'question': question, 'form': form})



@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Scanswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('scboard:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('scboard:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'scboard/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Scanswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('scboard:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Scquestion, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('scboard:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Scanswer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('scboard:detail', question_id=answer.question.id)