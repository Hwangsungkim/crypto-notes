# data_handler.py

def get_dummy_notes(category):
    if category == "기초 용어":
        return [
            {"title": "비트코인(Bitcoin)이란?", "content": "최초의 블록체인 기반 암호화폐입니다.\n* **특징**: 탈중앙화, 2100만 개 한정 발행"},
            {"title": "이더리움(Ethereum)", "content": "스마트 컨트랙트를(Smart Contract) 지원하는 2세대 블록체인입니다."}
        ]
    elif category == "블록체인 구조":
        return [
            {"title": "합의 알고리즘(PoW vs PoS)", "content": "네트워크 참여자들이 장부의 상태에 합의하는 방식입니다.\n* **PoW (작업증명)**: 컴퓨팅 연산력 제공 (예: 비트코인)\n* **PoS (지분증명)**: 지분(코인) 예치 (예: 이더리움)"}
        ]
    
    return []
import random

# (기존 get_dummy_notes 함수는 이 위에 그대로 둡니다)

def get_quiz_question():
    # 테스트 통과를 위한 최소한의 가짜 퀴즈 데이터를 반환합니다.
    # 나중에 객관식을 위해 'options(보기)'도 미리 넣어둡니다.
    return {
        "question": "최초의 블록체인 기반 암호화폐는 무엇인가요?",
        "answer": "비트코인",
        "options": ["이더리움", "리플", "비트코인", "솔라나"]
    }
