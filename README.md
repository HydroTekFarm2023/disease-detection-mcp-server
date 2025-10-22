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



