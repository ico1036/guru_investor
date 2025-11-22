#!/usr/bin/env python3
"""
Investment Guru Multi-Agent Discussion System

Main entry point for running the multi-agent investment guru discussion.
Usage: uv run run.py [topic]
"""

import sys
import asyncio
import argparse
from datetime import datetime
from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ToolUseBlock
from orchestrator import create_agent_options

async def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Run Investment Guru Discussion")
    parser.add_argument(
        "--topic", 
        default="AI 에이전트 시대의 picks and shovels 투자 기회에 대해 토론해줘.",
        help="Discussion topic"
    )
    parser.add_argument(
        "--gurus",
        default="warren_buffett,peter_lynch,cathie_wood,ray_dalio,benjamin_graham",
        help="Comma-separated list of investment gurus (e.g. 'warren_buffett,elon_musk')"
    )
    args = parser.parse_args()
    
    # Parse gurus
    guru_names = [name.strip() for name in args.gurus.split(",")]
    
    print(f"🤖 Starting Investment Guru Discussion Panel")
    print(f"topic: {args.topic}")
    print(f"Participants: {', '.join(guru_names)}")
    print("-" * 60)

    # Create options with all gurus registered
    options = create_agent_options(guru_names)
    
    # Collect discussion log
    discussion_log = []
    discussion_log.append(f"# Investment Guru Discussion: {args.topic}\n")
    discussion_log.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    discussion_log.append(f"**Participants:** {', '.join(guru_names)}\n\n")
    discussion_log.append("---\n\n")
    
    # Execute the Orchestrator Agent
    try:
        async with ClaudeSDKClient(options=options) as client:
            # Send the initial prompt to start the discussion
            await client.query(args.topic)
            
            # Stream the response
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(block.text, end="", flush=True)
                            discussion_log.append(block.text)
                        elif isinstance(block, ToolUseBlock):
                            # Real-time broadcasting of tool usage (Sub-agent calls)
                            if block.name == "Task":
                                subagent = block.input.get("subagent_type", "Unknown Agent")
                                log_msg = f"\n\n> 🎤 **[Social] Passing the microphone to:** `{subagent}`...\n\n"
                                print(log_msg.replace(">", "").replace("*", "").replace("`", "").strip())
                                discussion_log.append(log_msg)
                            elif block.name == "WebSearch":
                                query = block.input.get("query", "Unknown Query")
                                log_msg = f"\n\n> 🔍 **[System] Searching the web for:** `'{query}'`...\n\n"
                                print(log_msg.replace(">", "").replace("*", "").replace("`", "").strip())
                                discussion_log.append(log_msg)
                            else:
                                log_msg = f"\n\n> 🛠️ **[System] Using tool:** `{block.name}`\n\n"
                                print(log_msg.replace(">", "").replace("*", "").replace("`", "").strip())
                                discussion_log.append(log_msg)
        
        # Save to MD file
        filename = f"discussion_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("".join(discussion_log))
        
        print(f"\n\n💾 Discussion saved to: {filename}")
                            
    except Exception as e:
        print(f"\n\n❌ Error: {str(e)}")
        print("Ensure you are authenticated with 'anthropic auth login'.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⏹️  Discussion interrupted by user.")
        sys.exit(0)
