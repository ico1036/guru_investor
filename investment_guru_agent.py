"""
Investment Guru Sub-Agent Implementation

Individual agent implementations for each investment guru with their unique
investment philosophy, analysis style, and decision-making process.
This module now adheres to the claude-agent-sdk standard by providing
module-level tools that delegate to the agent instances.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import json
from claude_agent_sdk import tool

@dataclass
class InvestmentRecommendation:
    """Represents a single investment recommendation"""
    company_name: str
    ticker: str
    sector: str
    investment_thesis: str
    competitive_advantage: str
    financial_analysis: str
    risk_factors: str
    target_price: Optional[str] = None
    time_horizon: str = "3-5년"

    def to_dict(self) -> Dict:
        return asdict(self)

class BaseInvestmentGuruAgent:
    """Base class for all investment guru agents"""
    
    def __init__(self, name: str, philosophy: str, expertise: str, risk_profile: str, style: str):
        self.name = name
        self.philosophy = philosophy
        self.expertise = expertise
        self.risk_profile = risk_profile
        self.analysis_style = style
    
    async def analyze_ai_picks_shovels(self) -> Dict:
        """Analyze AI agent era picks and shovels opportunities"""
        recommendations = await self._generate_recommendations()
        return {
            "guru": self.name,
            "philosophy": self.philosophy,
            "top_picks": [rec.to_dict() for rec in recommendations],
            "analysis_summary": await self._provide_analysis_summary(recommendations)
        }
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """Generate investment recommendations based on guru's style"""
        raise NotImplementedError("Each guru must implement their own recommendation logic")
    
    async def _provide_analysis_summary(self, recommendations: List[InvestmentRecommendation]) -> str:
        """Provide overall analysis summary"""
        return f"{self.name}의 관점에서 AI 에이전트 시대 투자 분석"
    
    async def respond_to_peer(self, peer_name: str, peer_analysis: Dict) -> Dict:
        """Respond to another guru's analysis"""
        return await self._formulate_response(peer_name, peer_analysis)
    
    async def _formulate_response(self, peer_name: str, peer_analysis: Dict) -> Dict:
        """Formulate response based on guru's personality"""
        return {
            "responding_guru": self.name,
            "target_guru": peer_name,
            "response": f"{self.name}의 {peer_name}에 대한 응답",
            "agreement_points": [],
            "disagreement_points": [],
            "additional_insights": ""
        }

class WarrenBuffettAgent(BaseInvestmentGuruAgent):
    """Warren Buffett investment approach agent"""
    
    def __init__(self):
        super().__init__(
            name="워렌 버핏",
            philosophy="가치투자, 장기보유, 경쟁우위가 있는 기업",
            expertise="소비재, 금융, 보험, 에너지",
            risk_profile="보수적, 안정성 중시",
            style="기본적 분석, 경영진 품질 중시, 단순하고 이해하기 쉬운 비즈니스 선호"
        )
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """버핏 스타일의 추천: 안정적이고 이해하기 쉬운 비즈니스"""
        return [
            InvestmentRecommendation(
                company_name="Microsoft Corporation",
                ticker="MSFT",
                sector="클라우드 컴퓨팅 플랫폼",
                investment_thesis="AI 에이전트의 필수 인프라인 클라우드 플랫폼을 독점적으로 제공. 안정적인 수익 모델과 강력한 경쟁 해자를 보유.",
                competitive_advantage="Azure 클라우드 생태계, Office 365 통합, OpenAI 파트너십을 통한 AI 시장 선점",
                financial_analysis="꾸준한 현금흐름, 높은 이익률, 배당 성장 기록. PER 25배 수준으로 합리적 밸류에이션",
                risk_factors="클라우드 경쟁 심화, 규제 리스크",
                time_horizon="10년 이상"
            ),
            InvestmentRecommendation(
                company_name="Berkshire Hathaway",
                ticker="BRK.B",
                sector="다각화 지주회사",
                investment_thesis="AI 혁명 과정에서도 변하지 않는 핵심 사업들(보험, 철도, 에너지)을 보유. AI 시대에도 필요한 기본 인프라 제공",
                competitive_advantage="다각화된 사업 포트폴리오, 강력한 현금 창출 능력, 우수한 자본 배분 능력",
                financial_analysis="저평가된 상태, 강력한 대차대조표, 지속적인 주주가치 창출",
                risk_factors="경영진 승계 리스크, 거시경제 변화",
                time_horizon="영구보유"
            )
        ]

class PeterLynchAgent(BaseInvestmentGuruAgent):
    """Peter Lynch investment approach agent"""
    
    def __init__(self):
        super().__init__(
            name="피터 린치",
            philosophy="성장투자, 개인이 알고 있는 분야 투자",
            expertise="소매, 소비재, 기술",
            risk_profile="중간, 성장 잠재력 중시",
            style="상식적 접근, PEG 비율 활용, 스토리가 있는 기업 선호"
        )
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """린치 스타일의 추천: 성장 잠재력이 큰 이해하기 쉬운 기업"""
        return [
            InvestmentRecommendation(
                company_name="Taiwan Semiconductor",
                ticker="TSM",
                sector="반도체 파운드리",
                investment_thesis="AI 에이전트가 필요로 하는 모든 칩을 만드는 '칩의 공장'. 간단하고 이해하기 쉬운 비즈니스 모델",
                competitive_advantage="세계 최고의 반도체 제조 기술, 고객사 종속성 높음, 진입장벽 극히 높음",
                financial_analysis="PEG 1.2 수준으로 합리적, 꾸준한 성장과 높은 마진 유지",
                risk_factors="지정학적 리스크, 자본집약적 사업",
                time_horizon="5-7년"
            ),
            InvestmentRecommendation(
                company_name="Salesforce",
                ticker="CRM",
                sector="CRM 및 클라우드 소프트웨어",
                investment_thesis="모든 기업이 AI 에이전트를 도입할 때 필요한 고객 데이터 플랫폼. 'AI 에이전트의 메모리' 역할",
                competitive_advantage="고객 데이터 플랫폼 독점, 높은 전환비용, AI 기능 통합 가속화",
                financial_analysis="성장률 대비 밸류에이션 매력적, 구독 모델로 예측 가능한 수익",
                risk_factors="경쟁 심화, 고객 이탈 위험",
                time_horizon="3-5년"
            )
        ]

class CathieWoodAgent(BaseInvestmentGuruAgent):
    """Cathie Wood investment approach agent"""
    
    def __init__(self):
        super().__init__(
            name="캐시 우드",
            philosophy="파괴적 혁신, 지수적 성장 기술",
            expertise="AI, 로보틱스, 바이오테크, 블록체인",
            risk_profile="공격적, 고위험 고수익",
            style="기술 트렌드 분석, 장기 성장 잠재력, 혁신 주기 파악"
        )
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """우드 스타일의 추천: 파괴적 혁신 기술 기업"""
        return [
            InvestmentRecommendation(
                company_name="NVIDIA Corporation",
                ticker="NVDA",
                sector="AI 컴퓨팅 하드웨어",
                investment_thesis="AI 에이전트 혁명의 절대적 인프라. 모든 AI 모델 훈련과 추론에 필수적인 GPU 독점 공급",
                competitive_advantage="CUDA 소프트웨어 생태계, AI 칩 설계 노하우, 네트워크 효과",
                financial_analysis="매출 폭증, 마진 확대, AI 시장 성장과 함께 지수적 성장 가능",
                risk_factors="밸류에이션 부담, 경쟁 칩 등장 가능성",
                time_horizon="10년"
            ),
            InvestmentRecommendation(
                company_name="Palantir Technologies",
                ticker="PLTR",
                sector="데이터 분석 플랫폼",
                investment_thesis="AI 에이전트가 의사결정하기 위해 필요한 데이터 통합 및 분석 플랫폼. 정부와 기업의 AI 도입 필수 도구",
                competitive_advantage="복잡한 데이터 통합 기술, 높은 고객 의존도, 정부 계약 안정성",
                financial_analysis="매출 성장 가속화, 수익성 개선 추세, AI 붐과 함께 재평가 가능",
                risk_factors="정부 의존도, 경쟁 심화",
                time_horizon="5-10년"
            )
        ]

class RayDalioAgent(BaseInvestmentGuruAgent):
    """Ray Dalio investment approach agent"""
    
    def __init__(self):
        super().__init__(
            name="레이 달리오",
            philosophy="분산투자, 거시경제 기반 투자",
            expertise="글로벌 매크로, 채권, 원자재",
            risk_profile="중간, 리스크 패리티",
            style="거시경제 분석, 시스템적 접근, 원칙 기반 투자"
        )
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """달리오 스타일의 추천: 거시경제적 관점의 인프라 투자"""
        return [
            InvestmentRecommendation(
                company_name="Amazon Web Services (Amazon)",
                ticker="AMZN",
                sector="클라우드 인프라",
                investment_thesis="AI 에이전트 시대의 핵심 인프라. 글로벌 클라우드 1위로 모든 AI 워크로드의 기반",
                competitive_advantage="글로벌 인프라 규모, 다양한 AI 서비스 포트폴리오, 생태계 네트워크 효과",
                financial_analysis="AWS 부문 고마진 성장, 전체 그룹 밸류 재평가 여지",
                risk_factors="클라우드 경쟁, 규제 리스크, 거시경제 둔화",
                time_horizon="7-10년"
            ),
            InvestmentRecommendation(
                company_name="Alphabet Inc.",
                ticker="GOOGL",
                sector="인터넷 플랫폼 및 AI",
                investment_thesis="AI 에이전트가 정보를 얻는 주요 통로. 검색과 광고 플랫폼을 통해 AI 경제의 수혜자",
                competitive_advantage="검색 독점, 데이터 네트워크 효과, AI 연구 역량",
                financial_analysis="현재 밸류에이션 매력적, AI 투자 대비 저평가",
                risk_factors="광고 시장 변화, AI 경쟁, 규제 압력",
                time_horizon="5-8년"
            )
        ]

class BenjaminGrahamAgent(BaseInvestmentGuruAgent):
    """Benjamin Graham investment approach agent"""
    
    def __init__(self):
        super().__init__(
            name="벤자민 그레이엄",
            philosophy="절대적 가치투자, 안전마진 확보",
            expertise="다양한 섹터, 저평가 자산 발굴",
            risk_profile="매우 보수적, 손실 최소화 우선",
            style="정량적 분석, 재무제표 중심, 시장 감정과 반대 방향"
        )
    
    async def _generate_recommendations(self) -> List[InvestmentRecommendation]:
        """그레이엄 스타일의 추천: 저평가된 안전한 인프라 기업"""
        return [
            InvestmentRecommendation(
                company_name="Intel Corporation",
                ticker="INTC",
                sector="반도체",
                investment_thesis="AI 붐에 뒤처졌지만 여전히 필수적인 CPU와 데이터센터 인프라 제공. 현재 과도하게 저평가",
                competitive_advantage="x86 아키텍처 독점, 파운드리 사업 확장, 정부 지원",
                financial_analysis="PBR 1.5배, 배당수익률 5% 이상, 자산가치 대비 저평가",
                risk_factors="기술 경쟁력 격차, 시장점유율 하락",
                time_horizon="3-5년"
            ),
            InvestmentRecommendation(
                company_name="International Business Machines",
                ticker="IBM",
                sector="엔터프라이즈 IT 서비스",
                investment_thesis="기업들이 AI를 도입할 때 필요한 컨설팅과 시스템 통합 서비스. 안정적 배당과 저평가",
                competitive_advantage="기업 고객 관계, AI 컨설팅 역량, 하이브리드 클라우드",
                financial_analysis="낮은 PER, 높은 배당수익률, 안정적 현금흐름",
                risk_factors="레거시 사업 의존, 성장 둔화",
                time_horizon="3-5년"
            )
        ]

class InvestmentGuruFactory:
    """Factory class to create investment guru agents"""
    
    GURU_MAPPING = {
        "워렌 버핏": WarrenBuffettAgent,
        "피터 린치": PeterLynchAgent,
        "캐시 우드": CathieWoodAgent,
        "레이 달리오": RayDalioAgent,
        "벤자민 그레이엄": BenjaminGrahamAgent
    }
    
    @classmethod
    def create_guru_agent(cls, guru_name: str) -> BaseInvestmentGuruAgent:
        """Create a guru agent by name"""
        agent_class = cls.GURU_MAPPING.get(guru_name)
        if agent_class:
            return agent_class()
        else:
            # Create a generic agent for unknown gurus
            return BaseInvestmentGuruAgent(
                name=guru_name,
                philosophy="균형잡힌 투자",
                expertise="다양한 섹터",
                risk_profile="중간",
                style="기본적 분석"
            )
    
    @classmethod
    def get_available_gurus(cls) -> List[str]:
        """Get list of available guru names"""
        return list(cls.GURU_MAPPING.keys())

# --- Claude Agent SDK Tool Logic Extraction for Testing ---

async def _analyze_market_logic(args: Dict[str, Any]) -> Dict[str, Any]:
    """Inner logic for analyze_market tool"""
    guru_name = args["guru_name"]
    agent = InvestmentGuruFactory.create_guru_agent(guru_name)
    result = await agent.analyze_ai_picks_shovels()
    
    return {
        "content": [
            {
                "type": "text",
                "text": json.dumps(result, ensure_ascii=False, indent=2)
            }
        ]
    }

async def _respond_to_peer_logic(args: Dict[str, Any]) -> Dict[str, Any]:
    """Inner logic for respond_to_peer tool"""
    guru_name = args["guru_name"]
    peer_name = args["peer_name"]
    peer_analysis = args["peer_analysis"]
    
    agent = InvestmentGuruFactory.create_guru_agent(guru_name)
    result = await agent.respond_to_peer(peer_name, peer_analysis)
    
    return {
        "content": [
            {
                "type": "text",
                "text": json.dumps(result, ensure_ascii=False, indent=2)
            }
        ]
    }

# --- Claude Agent SDK Tool Definitions ---

@tool("analyze_market", "Generate investment recommendations based on a specific guru's style", {"guru_name": str})
async def analyze_market(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Tool to generate investment recommendations using a specific guru's philosophy.
    """
    return await _analyze_market_logic(args)

@tool("respond_to_peer", "Respond to another guru's analysis", 
      {"guru_name": str, "peer_name": str, "peer_analysis": dict})
async def respond_to_peer(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Tool to formulate a response to another guru's analysis.
    """
    return await _respond_to_peer_logic(args)
