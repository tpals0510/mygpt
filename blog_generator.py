import openai
import re

# OpenAI API 키 설정
openai.api_key = 'your-api-key'

def generate_blog_content(prompt, max_tokens=2000):
    response = openai.Completion.create(
        engine="code-davinci-002",  # Codex 엔진
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def clean_text(text):
    """ 블로그 글에서 불필요한 부분(예: 금지 단어) 제거 및 정리 """
    forbidden_keywords = [
        '최저가', '할인', '가격', '정가', '특가', '품절임박', '타임세일', '재입고', '조기마감', '예약링크', '후기 이벤트',
        '무료체험', '정품', '공식', '1위', '무료', '휴대폰', '가장', '만족', '추천', '특별', '성형', '비용', '할인'
    ]

    # 금지 단어를 제거합니다.
    for keyword in forbidden_keywords:
        text = text.replace(keyword, "")

    # 금지 표현 (이어서, (1/2) 등) 제거
    text = re.sub(r'\(.*\)', '', text)

    # "예시 문구" 패턴을 제거
    text = text.replace("예시 문구", "")

    return text

def create_blog_post(main_keyword, sub_keywords, proposal_details=None, tone="감성적이고 친근한 톤", max_tokens=2000):
    """주어진 규칙에 맞는 블로그 글을 생성하는 함수"""

    # 프로포즈 세부사항 처리
    proposal_section = ""
    if proposal_details:
        proposal_section = f"""
        여기에는 특별한 프로포즈 패키지가 포함되어 있습니다. 예를 들어, 헬륨풍선과 함께 두 분의 사진을 액자에 담아 세팅하고,
        로즈 톤의 조화 플라워 테이블과 감성적인 프로포즈 가랜드가 포인트를 이룹니다. 또한, 프로포즈 장식이 인물 중심으로 완벽하게 연출되어,
        그날의 순간을 더욱 특별하게 만듭니다. 스탠바이미 시스템을 통해 동영상을 상영하거나, 소중한 추억을 담은 사진을 공간에 배치하여
        감성적인 분위기를 만들어줍니다.
        """

    # 블로그 글의 prompt (AI에 전달할 입력)
    prompt = f"""
    블로그 글을 작성해주세요. 아래의 규칙을 따르세요:

    - 메인 키워드: {main_keyword}
    - 서브 키워드: {', '.join(sub_keywords)}
    - 스타일: 20대 후반 여성 사장님이 쓴 감성적이고 친근한 톤
    - 글의 톤: 친근하고 감성적인 대화체, 리얼한 경험 위주
    - 문체: 자연스럽고 공손한 존댓말
    - 금지 단어 사용 금지: 상업적인 단어(가격, 할인, 무료 등)
    - 블로그 글 길이: 2000자
    - 소제목 사용 금지
    - 글의 끝에 "내가 적지 말라고 알려줬던 단어들은 절대 적지 않는다." 문구 포함

    글의 흐름에 맞춰 작성해주세요. 아래는 블로그 글을 위한 작성 예시입니다.

    {proposal_section}  # 프로포즈 관련 내용 포함
    """

    # 블로그 글 생성
    blog_content = generate_blog_content(prompt, max_tokens)

    # 텍스트 정리
    cleaned_blog_content = clean_text(blog_content)

    return cleaned_blog_content

# 예시: 블로그 생성하기
main_keyword = "썸데이 파티룸"
sub_keywords = ["해운대", "오션뷰", "프라이빗", "파티룸", "사진", "드레스", "음식", "스탠바이미"]
proposal_details = True  # 프로포즈 관련 세부사항을 포함

blog_post = create_blog_post(main_keyword, sub_keywords, proposal_details)
print(blog_post)
