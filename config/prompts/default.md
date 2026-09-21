Generate Markdown technical documentation for this project based on repository files and MCP context.
Use repository inspection tools and MCP tools to gather evidence.
The documentation should be useful not only as a source-code overview, but also as practical project documentation similar to user or developer manual.
Inspect repository source code, configuration files, build files, examples, scripts, and relevant documentation files.
Do not attempt exhaustive repository coverage. Focus on information that helps a developer nderstand, build, configure, use, and extend the project.
Only state facts supported by repository files, tool results, or MCP context.
Do not guess file paths.
Do not invent details.
Do not output tool calls as JSON or plain text.

Prefer evidence from:
- source code
- configuration files
- build files
- examples
- scripts
- existing repository documentation
- MCP documentation context

Where supported by available evidence, include the following sections:

# Table of Contents

# Project Overview
Explain what the project is, its purpose, and its main use cases.

# Getting Started
Describe how to build, run, or start the project when this information is available.

# Architecture and Main Components
Describe the main runtime components and important modules.
Focus on responsibilities and interactions rather than listing every module or class.

# Key Concepts
Explain the main domain concepts required to understand the project.

# APIs and Usage
Describe important public APIs, commands, services, or extension points.
Include short examples when supported by repository files.

# Configuration
Describe important configuration files, properties, defaults, and runtime settings.

# Deployment and Operations
If supported by repository evidence, describe deployment, startup, administration, monitoring, or operational concerns.

# Security
If repository or MCP context contains meaningful security configuration or guidance, summarize it.

# Dependencies and Requirements
Describe important runtime/build requirements and major dependencies.

# Testing and Development
Briefly describe how the project can be tested or developed if this information is clearly available.

Do not include a section if there is insufficient evidence for it.
Do not focus excessively on internal class names, implementation details, CI pipelines, release processes, or code quality tooling unless they are essential to understanding the project.
Use source code to verify architectural and API claims, but prefer user-relevant explanations over exhaustive implementation listings.
Stop using tools once the major documentation areas above are sufficiently supported.
Your final response must contain ONLY finished Markdown documentation without reasoning, planning, or foreword.
