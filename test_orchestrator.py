import pytest
from orchestrator import get_system_prompt, get_allowed_tools, create_agent_options
from claude_agent_sdk import ClaudeAgentOptions, AgentDefinition

def test_orchestrator_system_prompt():
    """Test orchestrator system prompt"""
    prompt = get_system_prompt()
    assert isinstance(prompt, str)
    assert "Orchestrator" in prompt
    assert "Task" in prompt  # Must mention Task tool usage

def test_orchestrator_allowed_tools():
    """Test orchestrator allowed tools"""
    tools = get_allowed_tools()
    assert isinstance(tools, list)
    assert "Task" in tools  # Critical for sub-agent orchestration
    assert "WebSearch" in tools

def test_create_agent_options():
    """Test creation of ClaudeAgentOptions with sub-agents"""
    guru_names = ["warren_buffett", "cathie_wood"]
    options = create_agent_options(guru_names)
    
    assert isinstance(options, ClaudeAgentOptions)
    assert options.permission_mode == 'acceptEdits'
    
    # Check if sub-agents are registered correctly
    assert options.agents is not None
    assert "warren_buffett" in options.agents
    assert "cathie_wood" in options.agents
    
    # Check AgentDefinition properties
    buffett_def = options.agents["warren_buffett"]
    assert isinstance(buffett_def, AgentDefinition)
    assert buffett_def.description is not None
    assert buffett_def.prompt is not None
    assert buffett_def.tools is not None
