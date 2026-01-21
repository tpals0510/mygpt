#!/usr/bin/env python3
"""Naver blog draft generator for beginners.

Prompts for desired format, tone, and main keyword, then prints a structured
post draft tailored to common Naver blog ranking guidance.
"""

from datetime import datetime


def prompt(label: str) -> str:
    value = input(f"{label}: ").strip()
    return value


def build_outline(keyword: str) -> list[str]:
    return [
        f"{keyword} 개요",
        f"{keyword} 핵심 포인트 3가지",
        f"{keyword} 실제 적용 방법",
        f"{keyword} 자주 하는 실수",
        f"{keyword} 요약 및 다음 행동",
    ]


def build_article(keyword: str, tone: str, format_style: str) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    outline = build_outline(keyword)

    sections = [
        f"# {keyword} 완전초보를 위한 가이드 ({today})",
        "",
        f"**톤**: {tone}",
        f"**형태/양식**: {format_style}",
        "",
        f"{keyword}에 관심을 가진 분이라면, 오늘 글에서 핵심만 빠르게 정리해 드릴게요.",
        "",
        "## 목차",
        *[f"- {item}" for item in outline],
        "",
        f"## {outline[0]}",
        f"{keyword}는 초보자가 시작할 때 길을 잃기 쉬운 주제예요. ",
        "핵심만 잡고 가면 시행착오를 크게 줄일 수 있습니다.",
        "",
        f"## {outline[1]}",
        "1) 검색 의도에 맞는 제목 구성\n"
        "2) 본문에서 키워드를 자연스럽게 반복\n"
        "3) 경험 기반 문장과 구체적인 예시 포함",
        "",
        f"## {outline[2]}",
        "- 문제 제기 → 해결 과정 → 결과 순으로 전개\n"
        "- 소제목마다 핵심 요약 한 줄 추가\n"
        "- 동일 주제라도 나만의 경험/팁을 넣어 차별화",
        "",
        f"## {outline[3]}",
        "- 키워드 과다 삽입으로 읽기 불편해지는 경우\n"
        "- 짧은 문단만 반복해 신뢰도 떨어지는 경우\n"
        "- 제목과 내용이 어긋나 이탈률이 높아지는 경우",
        "",
        f"## {outline[4]}",
        f"오늘은 {keyword}의 기본 흐름을 정리했습니다. ",
        "다음 글에서는 실제 예시와 템플릿을 더 구체적으로 소개해 드릴게요.",
        "",
        "---",
        "### 체크리스트",
        "- 제목에 핵심 키워드 포함\n"
        "- 첫 문단에 글의 목적 요약\n"
        "- 본문에 경험/수치/예시 포함\n"
        "- 마무리 문장에 다음 행동 제안",
    ]

    return "\n".join(sections)


def main() -> None:
    print("네이버 블로그 원고 생성기\n")
    keyword = prompt("메인 키워드")
    tone = prompt("원하는 느낌/톤 (예: 친근, 전문가, 담백)")
    format_style = prompt("형태/양식 (예: 체크리스트 포함, Q&A, 후기형)")

    if not keyword:
        print("키워드를 입력해야 합니다.")
        return

    article = build_article(keyword, tone or "친근", format_style or "체크리스트 포함")
    print("\n===== 생성된 원고 =====\n")
    print(article)


if __name__ == "__main__":
    main()
