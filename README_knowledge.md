# THIS is a test, langchain-course.
## I - .ENV file has to have parameters:
1. OPEN_AI_API=...
2. LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
3. LANGSMITH_TRACING=true 
> [!IMPORTANT] 
> Use lowercase `true`.
4. LANGSMITH_API_KEY=...
5. LANGSMITH_AGENT_ID=hello-world 
> [!IMPORTANT] 
> Whatever name you wish to have here.
6. LANGSMITH_AGENT_ENVIRONMENT=production 
> [!IMPORTANT] 
> Look for traces in particular selectionbox afterwards.
## II - important helpers
1. **Hello World Chain** - Basic agent structure and LLM integration
```bash
- uv command: uv init --no-package   #creates base structure from scratch
- uv command: uv add langchain langchain-openai langchain-ollama langchain-tavily tavily-python python-dotenv black isort       
- git rm -rf . ' delete catalog
- source /Users/henrirene/Desktop/DEV/langchain-course/.venv/bin/activate
- git commit --amend --no-edit
- git push --force-with-lease 
```
## code examples
**Request Body:**
```json
--json
{
  "example_key": "example_value"
}
```
```sql
/!--sql--/
select * from db-table1
```
```python
# python code example
import os
```
## Ollama topics
# commands
```bash
ollama
henrirene@Henri-Renes-MBP ~ % ollama list
NAME           ID              SIZE      MODIFIED   
gemma3:270m    e7d36fb2c3b3    291 MB    8 days ago    
henrirene@Henri-Renes-MBP ~ % ollama pull gemma4:e2b
````
