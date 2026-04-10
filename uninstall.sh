#!/bin/bash
# Claude Marketing Suite — Uninstaller
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "${YELLOW}Uninstalling Claude Marketing Suite...${NC}"
echo ""

SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

# Remove orchestrator
if [ -d "$SKILLS_DIR/aim" ]; then
    rm -rf "$SKILLS_DIR/aim"
    echo -e "  ${GREEN}✓${NC} Removed: aim (orchestrator + scripts + templates)"
fi

# Remove skills
SKILLS=("aim-report" "aim-audit" "aim-landing" "aim-competitors" "aim-brand" "aim-audience" "aim-emails" "aim-social" "aim-ads" "aim-headlines")
for skill in "${SKILLS[@]}"; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        rm -rf "$SKILLS_DIR/$skill"
        echo -e "  ${GREEN}✓${NC} Removed skill: $skill"
    fi
done

# Remove agents
AGENTS=("aim-content" "aim-conversion" "aim-competitive" "aim-technical" "aim-strategy")
for agent in "${AGENTS[@]}"; do
    if [ -f "$AGENTS_DIR/$agent.md" ]; then
        rm "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} Removed agent: $agent"
    fi
done

echo ""
echo -e "${GREEN}Claude Marketing Suite uninstalled.${NC}"
echo ""
