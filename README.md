# LangChain_NoLangChain

Learning repository comparing direct LLM API usage and LangChain wrappers using:

- Google Gemini
- Groq
- OpenAI
- Sophos Central API

---

## Project Structure

### Gemini

| File | Description |
|--------|-------------|
| gemini_no_langchain.py | Direct Gemini SDK |
| gemini_langchain.py | Gemini through LangChain |

---

### Groq

| File | Description |
|--------|-------------|
| groq_no_langchain.py | Direct Groq SDK |
| groq_langchain.py | Groq through LangChain |

---

### OpenAI

| File | Description |
|--------|-------------|
| openai_langchain_1.py | OpenAI basic example |
| openai_langchain_2.py | OpenAI LangChain example |

---

### Sophos API

| File | Description |
|--------|-------------|
| sophos_token.py | Sophos OAuth Token generation |
| langchain_sophos.py | LangChain chatbot integrated with Sophos APIs |

---

## Environment Variables

Create a `.env` file:

```env
GOOGLEGENERATIVEAI_API_KEY=your_key
GENAI_API_KEY=your_key

GROQ_API_KEY=your_key

OPENAI_API_KEY=your_key

CLIENT_ID=your_sophos_client_id
CLIENT_SECRET=your_sophos_client_secret
```

---

## Install Dependencies

```bash
pip install python-dotenv
pip install langchain
pip install langchain-google-genai
pip install langchain-groq
pip install langchain-openai
pip install requests
pip install google-genai
pip install groq
```

---

## Run Examples

Gemini

```bash
python3 gemini_no_langchain.py
python3 gemini_langchain.py
```

Groq

```bash
python3 groq_no_langchain.py
python3 groq_langchain.py
```

OpenAI

```bash
python3 openai_langchain_1.py
python3 openai_langchain_2.py
```

Sophos

```bash
python3 sophos_token.py
python3 langchain_sophos.py
```

---

## Learning Goal

Understand the difference between:

- Direct SDK usage
- LangChain wrappers
- Environment variable handling using dotenv
- API authentication
- Sophos Central API integration
