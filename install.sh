#!/bin/bash
# Claude Marketing Suite — Installer
# Installs aim-* skills, agents, scripts and templates into Claude Code

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║     Claude Marketing Suite — Installer       ║${NC}"
echo -e "${CYAN}║     10 Skills · 5 Agents · 4 Scripts         ║${NC}"
echo -e "${CYAN}║                                              ║${NC}"
echo -e "${CYAN}║     Лаборатория ИИ-Маркетинга                ║${NC}"
echo -e "${CYAN}║     t.me/moremarketingisaid                   ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════╝${NC}"
echo ""

# Detect script directory
if [ -n "$BASH_SOURCE" ] && [ "$BASH_SOURCE" != "bash" ] && [ -f "$BASH_SOURCE" ]; then
    SCRIPT_DIR="$(cd "$(dirname "$BASH_SOURCE")" && pwd)"
else
    # Running via curl | bash — need to clone
    echo -e "${YELLOW}Running remote install — cloning repository...${NC}"
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/Fillikam/claude-marketing-suite.git "$TEMP_DIR/claude-marketing-suite" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to clone repository.${NC}"
        exit 1
    fi
    SCRIPT_DIR="$TEMP_DIR/claude-marketing-suite"
fi

# Target directories
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo -e "${BLUE}Source:${NC}  $SCRIPT_DIR"
echo -e "${BLUE}Target:${NC} $SKILLS_DIR"
echo ""

# Check if Claude Code is available
if command -v claude &>/dev/null; then
    echo -e "${GREEN}✓ Claude Code detected${NC}"
else
    echo -e "${YELLOW}⚠ Claude Code not found in PATH${NC}"
    if [ -t 0 ]; then
        read -p "  Continue anyway? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Installation cancelled."
            exit 0
        fi
    else
        echo "  Continuing (non-interactive mode)..."
    fi
fi

# Create directories
echo -e "\n${BLUE}Creating directories...${NC}"
mkdir -p "$SKILLS_DIR"
mkdir -p "$AGENTS_DIR"

# Install main orchestrator
echo -e "${BLUE}Installing main orchestrator...${NC}"
mkdir -p "$SKILLS_DIR/aim"
cp "$SCRIPT_DIR/aim/SKILL.md" "$SKILLS_DIR/aim/SKILL.md"
echo -e "  ${GREEN}✓${NC} aim/SKILL.md (orchestrator)"

# Install sub-skills
echo -e "\n${BLUE}Installing skills...${NC}"
SKILL_DIRS=(
    "00-aim-report"
    "01-aim-audit"
    "02-aim-landing"
    "03-aim-competitors"
    "04-aim-brand"
    "05-aim-audience"
    "06-aim-emails"
    "07-aim-social"
    "08-aim-ads"
    "09-aim-headlines"
)

SKILL_COUNT=0
for skill_dir in "${SKILL_DIRS[@]}"; do
    skill_name="${skill_dir#*-}"  # Remove number prefix (e.g., "00-")
    skill_name="${skill_name#*-}" # Keep aim-* part... actually extract properly
    # Get the aim-* name from directory
    aim_name=$(echo "$skill_dir" | sed 's/^[0-9]*-//')
    if [ -f "$SCRIPT_DIR/skills/$skill_dir/SKILL.md" ]; then
        mkdir -p "$SKILLS_DIR/$aim_name"
        cp "$SCRIPT_DIR/skills/$skill_dir/SKILL.md" "$SKILLS_DIR/$aim_name/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $aim_name"
        SKILL_COUNT=$((SKILL_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $aim_name (not found, skipping)"
    fi
done

# Install agents
echo -e "\n${BLUE}Installing agents...${NC}"
AGENTS=(
    "aim-content"
    "aim-conversion"
    "aim-competitive"
    "aim-technical"
    "aim-strategy"
)

AGENT_COUNT=0
for agent in "${AGENTS[@]}"; do
    if [ -f "$SCRIPT_DIR/agents/$agent.md" ]; then
        cp "$SCRIPT_DIR/agents/$agent.md" "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} $agent"
        AGENT_COUNT=$((AGENT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $agent (not found, skipping)"
    fi
done

# Install scripts
echo -e "\n${BLUE}Installing scripts...${NC}"
SCRIPTS_TARGET="$SKILLS_DIR/aim/scripts"
mkdir -p "$SCRIPTS_TARGET"

SCRIPT_FILES=(
    "analyze_page.py"
    "competitor_scanner.py"
    "social_calendar.py"
    "generate_pdf_report.py"
)

SCRIPT_COUNT=0
for script in "${SCRIPT_FILES[@]}"; do
    if [ -f "$SCRIPT_DIR/scripts/$script" ]; then
        cp "$SCRIPT_DIR/scripts/$script" "$SCRIPTS_TARGET/$script"
        chmod +x "$SCRIPTS_TARGET/$script"
        echo -e "  ${GREEN}✓${NC} $script"
        SCRIPT_COUNT=$((SCRIPT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $script (not found, skipping)"
    fi
done

# Install templates
echo -e "\n${BLUE}Installing templates...${NC}"
TEMPLATES_TARGET="$SKILLS_DIR/aim/templates"
mkdir -p "$TEMPLATES_TARGET"

TEMPLATE_COUNT=0
if [ -d "$SCRIPT_DIR/templates" ]; then
    for template in "$SCRIPT_DIR/templates"/*.md; do
        if [ -f "$template" ]; then
            cp "$template" "$TEMPLATES_TARGET/$(basename "$template")"
            echo -e "  ${GREEN}✓${NC} $(basename "$template")"
            TEMPLATE_COUNT=$((TEMPLATE_COUNT + 1))
        fi
    done
fi

# Check Python dependencies
echo -e "\n${BLUE}Checking Python dependencies...${NC}"
if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null)
    echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION detected"
    if python3 -c "import reportlab" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} reportlab installed (PDF reports ready)"
    else
        echo -e "  ${YELLOW}⚠${NC} reportlab not installed (needed for PDF reports)"
        echo -e "    Install with: ${CYAN}pip install reportlab${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠${NC} Python 3 not found — scripts won't work"
    echo -e "    Install Python: ${CYAN}https://python.org${NC}"
fi

# Cleanup temp directory if used
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

# Summary
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║           Installation Complete!              ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Skills installed:    ${GREEN}$SKILL_COUNT${NC}"
echo -e "  Agents installed:    ${GREEN}$AGENT_COUNT${NC}"
echo -e "  Scripts installed:   ${GREEN}$SCRIPT_COUNT${NC}"
echo -e "  Templates installed: ${GREEN}$TEMPLATE_COUNT${NC}"
echo ""
echo -e "${CYAN}Available Commands:${NC}"
echo "  /aim audit <url>          Full marketing audit (5 parallel agents)"
echo "  /aim landing <url>        Landing page CRO analysis"
echo "  /aim competitors <url>    Competitive intelligence"
echo "  /aim brand <url>          Brand voice analysis"
echo "  /aim audience <url>       Audience research & segmentation"
echo "  /aim emails <topic/url>   Email sequences"
echo "  /aim social <topic/url>   Social media content calendar"
echo "  /aim ads <url>            Ad campaigns"
echo "  /aim headlines <product>  100 direct response headlines"
echo "  /aim report <url>         Full marketing report"
echo ""
echo -e "  Telegram: ${CYAN}https://t.me/moremarketingisaid${NC}"
echo -e "  ${YELLOW}Start a new Claude Code session to use the skills.${NC}"
echo ""
