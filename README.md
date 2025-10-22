# MCP Server — Deployment Guide

This repository contains an **MCP (Model Context Protocol) Server** built with **FastAPI**.  
It powers model-based interactions, external API communication, and AI-driven processing.

You can deploy this server in **two ways**:
- Cloud deployment using **[Railway](https://railway.app/)**
- Local deployment via **Claude Desktop**

---

## Prerequisites

- Python **3.10+**
- A **Railway** account (for cloud deployment)
- **Claude Desktop** installed (for local MCP deployment)
- `requirements.txt` dependencies installed

---

## Environment Variables

Create a `.env` file (or set via Railway dashboard):
```
DYNAMODB_TABLE_NAME=your-dynamo-db-name
S3_BUCKET_NAME=your-s3-bucket-name
AWS_REGION=your-aws-region
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

> For Claude Desktop local deployment, environment variables can be added through the MCP configuration.

---

# Deployment Option 1: Railway (Cloud Hosting)

### 1. **Upload or Connect Your Repository**
- Push your project to GitHub.
- Go to [Railway Dashboard](https://railway.app/dashboard).
- Click **“New Project” → “Deploy from GitHub Repo”**.
- Select your MCP server repository.

### 2. **Set Environment Variables**
In Railway → **Settings → Variables**, add all keys from your `.env`.

### 3. **Configure the Start Command**
If Railway doesn’t auto-detect it, manually set:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
### 4. **Deploy!**
Click Deploy Now, and Railway will build and host your MCP server.

Once live, you’ll get a public URL:

`` https://your-mcp-server.up.railway.app/ ``

### 5. **Test the Deployment**
```bash
curl https://your-mcp-server.up.railway.app/
```
Expected response:
```
{"message":"Plant Disease MCP API running......."}
```

---

# Deployment Option 2: Claude Desktop (Local MCP)

### 1. **Claude Desktop Setup**
- First, make sure you have Claude for Desktop installed. [You can install the latest version here](https://claude.com/download).
- If you already have Claude for Desktop, make sure it’s updated to the latest version.
- We’ll need to configure Claude for Desktop for whichever MCP servers you want to use.
- To do this, open your Claude for Desktop App configuration at ``~/Library/Application Support/Claude/claude_desktop_config.json`` in a text editor.
- Make sure to create the file if it doesn’t exist.

macOS/Linux:
```
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

windows:
```
code $env:AppData\Claude\claude_desktop_config.json
```

### 2. **Add MCP Server**
You’ll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.

macOS/Linux:
```
{
  "mcpServers": {
    "server-name": {
      "command": "package-installer",     # uv/pip
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-folder",
        "run",
        "server-file.py"
      ]
    }
  }
}
```

windows:
```
{
  "mcpServers": {
    "server-name": {
      "command": "package-installer",     #uv/pip
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\mcp-folder",
        "run",
        "server-file.py"
      ]
    }
  }
}
```

**You may need to put the full path to the uv executable in the command field. You can get this by running `which uv` / `which pip` on macOS/Linux or `where uv` / `where pip` on Windows.**

This tells Claude for Desktop:
1. There’s an MCP server named “server-name”
2. To launch it by running `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-folder run server-file.py`

**Save the file, and restart Claude for Desktop.**

### 3. **Test with Commands**
- Make sure Claude for Desktop is picking up the two tools we’ve exposed in your `server-name`. You can do this by looking for the `Search and tools`  icon.
- After clicking on the slider icon, you should see all tools listed.
- If your server isn’t being picked up by Claude for Desktop, proceed to the **[Troubleshooting](https://modelcontextprotocol.io/docs/develop/build-server#troubleshooting)** section for debugging tips.
- If the tool settings icon has shown up, you can now test your server by running the commands in Claude for Desktop.
