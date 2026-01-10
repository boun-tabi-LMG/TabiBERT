# Quick Security Guide

## ✅ Your Repository is Clean!

No API keys or secrets were found in your git history.

---

## 🔒 Keep It Secure - Quick Checklist

### Before Committing Code

- [ ] Check for hardcoded credentials
- [ ] Ensure `.env` files are in `.gitignore`
- [ ] Review diff before pushing: `git diff`
- [ ] Use environment variables for all secrets

### Example: Safe Credential Management

❌ **DON'T DO THIS:**
```python
# Bad - Hardcoded API key
api_key = "sk-1234567890abcdef"
openai_client = OpenAI(api_key=api_key)
```

✅ **DO THIS:**
```python
# Good - Use environment variables
import os
api_key = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=api_key)
```

### Environment File Example

Create `.env` (add to `.gitignore`):
```bash
# .env - NEVER commit this file
OPENAI_API_KEY=sk-your-actual-key-here
HUGGINGFACE_TOKEN=hf_your-token-here
WANDB_API_KEY=your-wandb-key-here
```

Create `.env.example` (safe to commit):
```bash
# .env.example - Safe template for team
OPENAI_API_KEY=your_openai_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here
WANDB_API_KEY=your_wandb_key_here
```

---

## 🛠️ Quick Security Tools

### 1. Install gitleaks (Recommended)

```bash
# macOS
brew install gitleaks

# Linux
wget https://github.com/gitleaks/gitleaks/releases/download/v8.18.0/gitleaks_8.18.0_linux_x64.tar.gz
tar xvzf gitleaks_8.18.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/

# Scan your repo
gitleaks detect --source . --verbose
```

### 2. Pre-commit Hook (Optional)

Create `.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Check for common secret patterns before commit

if git diff --cached | grep -iE "(api[_-]?key|password|secret[_-]?key)" > /dev/null; then
    echo "⚠️  WARNING: Possible secret detected in commit!"
    echo "Please review your changes before committing."
    exit 1
fi
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### 3. Quick Manual Check

Before pushing, run:
```bash
# Check what you're about to commit
git diff HEAD

# Search for potential secrets in staged files
git diff --cached | grep -iE "(api[_-]?key|password|secret)"
```

---

## 🚨 If You Accidentally Commit a Secret

### Option 1: If Not Yet Pushed
```bash
# Remove from last commit
git reset HEAD~1
# Edit the file to remove secret
# Recommit without the secret
git add .
git commit -m "Your message"
```

### Option 2: If Already Pushed (More Complex)
1. **Immediately rotate the compromised credential** (get a new key)
2. Contact your team lead
3. Consider using `git filter-repo` or BFG Repo-Cleaner
4. Force push carefully (coordinate with team)

**Important**: Once pushed to GitHub, consider the secret compromised even if deleted!

---

## 📚 Resources

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

## ✨ Current Status

**Last Security Scan**: 2026-01-10  
**Status**: ✅ Clean - No secrets detected  
**Next Scan**: Recommended every 3-6 months

See `SECURITY_SCAN_REPORT.md` for detailed findings.
