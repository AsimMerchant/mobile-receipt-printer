# MCP (Model Context Protocol) Server Setup Guide

## Overview
This guide walks you through setting up MCP servers in VS Code. MCP allows you to extend AI capabilities with specialized tools and services.

## Prerequisites

### 1. Install Node.js
```powershell
# Install Node.js using Windows Package Manager
winget install OpenJS.NodeJS
```

### 2. Set PowerShell Execution Policy
```powershell
# Allow PowerShell scripts to run
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Update Environment Variables
```powershell
# Add Node.js to PATH permanently
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\nodejs", [EnvironmentVariableTarget]::User)

# Refresh PATH for current session
$env:PATH = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User) + ";" + [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine)
```

## MCP Configuration

### 1. Locate MCP Configuration File
The MCP configuration file is located at:
```
%APPDATA%\Code\User\mcp.json
```

### 2. Basic MCP Configuration Structure
```json
{
    "servers": {
        "server-name": {
            "command": "command-to-run",
            "args": ["arg1", "arg2"],
            "env": {
                "ENVIRONMENT_VARIABLE": "value"
            }
        }
    }
}
```

### 3. Sequential Thinking Server Configuration
```json
{
    "servers": {
        "sequential-thinking": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
            "env": {
                "PATH": "C:\\Program Files\\nodejs;%PATH%"
            }
        }
    }
}
```

## Verification Steps

### 1. Test Node.js Installation
```powershell
node --version
npm --version
npx --version
```

### 2. Test MCP Server Manually
```powershell
& "C:\Program Files\nodejs\npx.cmd" -y "@modelcontextprotocol/server-sequential-thinking" --help
```

### 3. Check Environment Variables
```powershell
# Check User PATH
[Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)

# Check System PATH
[Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine)

# Find npx location
where.exe npx
```

## Adding Additional MCP Servers

### Example: Adding Multiple Servers
```json
{
    "servers": {
        "sequential-thinking": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
            "env": {
                "PATH": "C:\\Program Files\\nodejs;%PATH%"
            }
        },
        "filesystem": {
            "command": "C:\\Program Files\\nodejs\\npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", "--root", "C:\\Development"],
            "env": {
                "PATH": "C:\\Program Files\\nodejs;%PATH%"
            }
        }
    }
}
```

## Common Issues & Troubleshooting

### Issue: "npx command not found"
**Solution:**
1. Ensure Node.js is installed
2. Check PATH environment variables
3. Use full path to npx.cmd in configuration
4. Restart VS Code after PATH changes

### Issue: "node is not recognized"
**Solution:**
1. Add Node.js directory to PATH environment variable
2. Include `env` section in MCP configuration with PATH
3. Verify Node.js installation

### Issue: PowerShell execution policy errors
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Server fails to initialize
**Solution:**
1. Check server logs in VS Code output panel
2. Test server manually in terminal
3. Verify all paths are correct
4. Ensure server package exists

## Useful Commands

### Environment Management
```powershell
# Refresh environment variables
$env:PATH = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User) + ";" + [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine)

# Check if Node.js is in PATH
$env:PATH -split ';' | Where-Object { $_ -like "*nodejs*" }
```

### Testing MCP Servers
```powershell
# Test sequential thinking server
& "C:\Program Files\nodejs\npx.cmd" -y "@modelcontextprotocol/server-sequential-thinking" --help

# List available MCP servers (if registry exists)
& "C:\Program Files\nodejs\npx.cmd" -y "@modelcontextprotocol/create-server" --list
```

## Best Practices

1. **Use Full Paths**: Always use complete file paths in MCP configurations
2. **Environment Variables**: Include necessary environment variables in server config
3. **Testing**: Test servers manually before adding to MCP configuration
4. **Documentation**: Keep track of installed servers and their purposes
5. **Backup**: Keep a backup of your working mcp.json configuration

## Available MCP Servers

- `@modelcontextprotocol/server-sequential-thinking` - Structured reasoning
- `@modelcontextprotocol/server-filesystem` - File system operations
- `@modelcontextprotocol/server-fetch` - Web content fetching
- `@modelcontextprotocol/server-sqlite` - SQLite database operations

## Support

If you encounter issues:
1. Check VS Code output panel for MCP logs
2. Test commands manually in PowerShell
3. Verify all paths and environment variables
4. Restart VS Code after configuration changes

---

*This guide was created on September 11, 2025*