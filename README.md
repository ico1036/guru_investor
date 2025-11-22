# Investment Guru Multi-Agent Discussion System

AI 에이전트 시대의 "picks and shovels" 투자 기회를 분석하는 다중 에이전트 토론 시스템입니다. 5명의 전설적인 투자 거장들이 각자의 독특한 투자 철학을 바탕으로 토론을 펼치며, 최고의 투자 기회를 발굴합니다.

## 🎯 주요 기능

- **동적 서브에이전트 생성**: 입력된 투자거장 이름을 바탕으로 각각의 고유한 투자 철학과 스타일을 가진 AI 에이전트 자동 생성
- **구조화된 토론 진행**: 5단계의 체계적인 토론 프로세스 (오프닝 → 개별분석 → 교차토론 → 컨센서스 → 최종권고)
- **투자거장별 특화 분석**: 각 거장의 실제 투자 스타일과 철학을 반영한 맞춤형 분석
- **AI 인프라 전문 분석**: "picks and shovels" 개념에 맞는 AI 에이전트 시대 핵심 인프라 기업 발굴

## 🏛️ 지원하는 투자 거장들

| 투자 거장 | 투자 철학 | 전문 분야 | 위험 성향 |
|-----------|-----------|-----------|-----------|
| **워렌 버핏** | 가치투자, 장기보유 | 소비재, 금융, 에너지 | 보수적 |
| **피터 린치** | 성장투자, 친숙한 기업 | 소매, 소비재, 기술 | 중간 |
| **캐시 우드** | 파괴적 혁신 | AI, 로보틱스, 바이오테크 | 공격적 |
| **레이 달리오** | 분산투자, 거시경제 | 글로벌 매크로, 채권 | 중간 |
| **벤자민 그레이엄** | 절대적 가치투자 | 저평가 자산 발굴 | 매우 보수적 |

## 🚀 빠른 시작

### 전제 조건

- Python 3.9 이상
- uv 패키지 매니저 (권장) 또는 pip

### 설치

```bash
# 저장소 클론
git clone <repository-url>
cd agent_investment_guru

# uv를 사용한 설치 (권장)
uv sync

# 또는 pip를 사용한 설치
pip install -r requirements.txt
```

### 사용법

```bash
# 기본 사용법 - 5명의 투자거장 토론
uv run run.py "워렌 버핏,피터 린치,캐시 우드,레이 달리오,벤자민 그레이엄"

# 3명만으로 간단한 토론
uv run run.py "워렌 버핏,피터 린치,캐시 우드"

# 상세한 JSON 결과 출력
uv run run.py "워렌 버핏,캐시 우드" --output-format json

# 자세한 로깅과 함께 실행
uv run run.py "워렌 버핏,피터 린치" --verbose
```

## 🏗️ 아키텍처

### 시스템 구조

```
┌─────────────────────────────────────────────────────────────┐
│                    run.py (Main Entry)                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│              InvestmentGuruSystem                           │
│  ┌─────────────────────────┬─────────────────────────────┐ │
│  │  InvestmentOrchestrator │   DiscussionCoordinator     │ │
│  │  Agent                  │                             │ │
│  └─────────────────────────┴─────────────────────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                InvestmentGuruFactory                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Warren   │ │ Peter    │ │ Cathie   │ │   Ray    │  ...  │
│  │ Buffett  │ │ Lynch    │ │ Wood     │ │ Dalio    │       │
│  │ Agent    │ │ Agent    │ │ Agent    │ │ Agent    │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└─────────────────────────────────────────────────────────────┘
```

### 주요 컴포넌트

1. **InvestmentOrchestratorAgent** (`orchestrator.py`)
   - 전체 시스템을 조율하는 메인 오케스트레이터
   - 동적으로 서브에이전트 생성 및 관리

2. **DiscussionCoordinator** (`discussion_coordinator.py`)
   - 5단계 토론 프로세스 진행 관리
   - 각 페이즈별 결과 수집 및 분석

3. **BaseInvestmentGuruAgent** 및 구체적 구현체들 (`investment_guru_agent.py`)
   - 각 투자거장의 고유한 투자 철학과 스타일 구현
   - `WarrenBuffettAgent`, `PeterLynchAgent`, `CathieWoodAgent` 등

4. **InvestmentGuruFactory**
   - 투자거장 이름을 바탕으로 적절한 에이전트 인스턴스 생성
   - 확장 가능한 팩토리 패턴 구현

## 📊 토론 프로세스

### 5단계 구조화된 토론

1. **🎤 오프닝 (5분)**
   - 각 투자거장의 투자 철학 소개
   - AI 에이전트 시대에 대한 관점 제시

2. **📈 개별 분석 발표 (15분)**
   - 각 거장이 독립적으로 TOP 2 추천종목 발표
   - 상세한 투자 논리와 리스크 분석

3. **🔄 교차 토론 (20분)**
   - 다른 거장들의 선택에 대한 질문과 반박
   - 서로 다른 관점의 활발한 의견 교환

4. **🤝 컨센서스 빌딩 (10분)**
   - 공통점과 차이점 정리
   - 투자자에게 유용한 통합 인사이트 도출

5. **🎯 최종 권고 (10분)**
   - 종합적인 투자 권고사항
   - 구체적인 실행 방안 제시

### 출력 형태

```json
{
  "topic": "AI 에이전트 시대의 picks and shovels 섹터와 대표적인 상장사는 무엇일까? 탑2개를 뽑아라",
  "participants": ["워렌 버핏", "피터 린치", "캐시 우드"],
  "final_recommendations": [
    {
      "rank": 1,
      "company": "NVIDIA Corporation (NVDA)",
      "category": "AI Hardware Infrastructure",
      "supporting_gurus": ["캐시 우드"],
      "investment_thesis": "AI 에이전트 컴퓨팅의 핵심 인프라",
      "target_allocation": "15-20%"
    }
  ],
  "execution_summary": {
    "key_insights": [...],
    "action_items": [...],
    "risk_monitors": [...]
  }
}
```

## 🔧 확장 가능성

### 새로운 투자거장 추가

```python
class NewGuruAgent(BaseInvestmentGuruAgent):
    def __init__(self):
        super().__init__(
            name="새로운 거장",
            philosophy="투자 철학",
            expertise="전문 분야",
            risk_profile="위험 성향",
            style="분석 스타일"
        )
    
    async def _generate_recommendations(self):
        # 거장만의 고유한 추천 로직 구현
        return [...]

# Factory에 등록
InvestmentGuruFactory.GURU_MAPPING["새로운 거장"] = NewGuruAgent
```

### 새로운 토론 주제 추가

`DiscussionCoordinator` 클래스를 상속받아 새로운 토론 주제에 맞는 페이즈와 분석 로직을 구현할 수 있습니다.

## 📝 결과 파일

실행 후 다음 파일들이 생성됩니다:

- `discussion_results_YYYYMMDD_HHMMSS.json`: 전체 토론 결과
- 각 단계별 상세 분석 결과
- 최종 추천 종목 및 포트폴리오 구성 제안

## 🤝 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🚨 면책 조항

이 시스템은 교육 및 연구 목적으로 제작되었습니다. 실제 투자 결정에 사용하기 전에 반드시 전문가와 상담하시기 바랍니다. 투자에는 항상 위험이 따르며, 과거 성과가 미래 결과를 보장하지 않습니다.