import pytest
from investment_gurus import get_guru_prompt, get_guru_tools, AVAILABLE_GURUS

def test_available_gurus():
    """Test that we have the expected list of gurus"""
    expected_gurus = [
        "warren_buffett",
        "peter_lynch", 
        "cathie_wood",
        "ray_dalio",
        "benjamin_graham"
    ]
    for guru in expected_gurus:
        assert guru in AVAILABLE_GURUS

def test_guru_prompts():
    """Test that each guru has a valid system prompt"""
    for guru in AVAILABLE_GURUS:
        prompt = get_guru_prompt(guru)
        assert isinstance(prompt, str)
        assert len(prompt) > 100
        # Check if prompt contains guru specific keywords
        if guru == "warren_buffett":
            assert "워렌 버핏" in prompt or "Warren Buffett" in prompt
        elif guru == "cathie_wood":
            assert "캐시 우드" in prompt or "Cathie Wood" in prompt

def test_guru_tools():
    """Test that each guru has allowed tools"""
    for guru in AVAILABLE_GURUS:
        tools = get_guru_tools(guru)
        assert isinstance(tools, list)
        # Basic tools that every guru should have
        assert "WebSearch" in tools

