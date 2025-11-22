"""
Orchestrator Agent

This agent coordinates the multi-agent discussion by managing the sub-agents (Gurus).
It uses the AgentDefinition architecture from claude-agent-sdk.
"""

import asyncio
from typing import List, Dict
from claude_agent_sdk import ClaudeAgentOptions, AgentDefinition
import investment_gurus

def get_system_prompt(guru_names: List[str]) -> str:
    """
    Returns the Orchestrator's system prompt dynamically based on the participants.
    """
    
    # Create bullet list of gurus for the prompt
    guru_list_str = "\n".join([f"- `{name}`" for name in guru_names])
    
    return f"""
You are the Orchestrator Agent for an Investment Guru Discussion Panel.
Your goal is to facilitate a deep, insightful discussion on investment topics among legendary investors.

# Your Responsibilities
1. **Introduce the Topic**: Clearly state the investment theme.
2. **Coordinate the Discussion**: Use the `Task` tool to call upon specific Gurus to share their views.
   - Call one Guru at a time.
   - After a Guru speaks, you can ask another Guru to respond or critique.
3. **Synthesize Views**: Summarize the key points of agreement and disagreement.
4. **Drive to Conclusion**: Formulate a consensus or a diversified portfolio recommendation based on the discussion.

# Your Sub-Agents (The Gurus)
You have access to the following specialized agents via the `Task` tool:
{guru_list_str}

# How to Use the Task Tool
To ask a Guru for their opinion:
`Task(subagent_type="guru_name", prompt="Please analyze [topic] based on your investment philosophy.")`

# Discussion Flow Rules
- Start by asking relevant Gurus for their initial analysis.
- Then facilitate a cross-examination phase.
- Finally, present a summary of the findings.

Always maintain a professional, moderating tone.
"""

def get_allowed_tools() -> List[str]:
    """Returns the tools allowed for the Orchestrator."""
    return ["Bash", "Read", "Write", "WebSearch", "Task"]

def create_agent_options(guru_names: List[str]) -> ClaudeAgentOptions:
    """
    Creates the ClaudeAgentOptions with the specified gurus registered as sub-agents.
    Accepts ANY guru name and dynamically creates an agent definition for them.
    """
    
    agents_map: Dict[str, AgentDefinition] = {}
    
    for name in guru_names:
        # Normalize name
        clean_name = name.strip()
        
        # Create definition for EVERY guru provided, whether predefined or dynamic
        agents_map[clean_name] = AgentDefinition(
            description=f"Investment Guru: {clean_name.replace('_', ' ').title()}",
            prompt=investment_gurus.get_guru_prompt(clean_name),
            tools=investment_gurus.get_guru_tools(clean_name)
        )
            
    return ClaudeAgentOptions(
        system_prompt=get_system_prompt(guru_names),
        allowed_tools=get_allowed_tools(),
        permission_mode='acceptEdits',
        agents=agents_map
    )
