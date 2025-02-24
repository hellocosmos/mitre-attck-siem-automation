# SIEM Alert Enrichment Automation using MITRE ATT&CK and n8n (en)

- **editor: hellocosmos@gmail.com**



## This workflow is ideal for:

* **Cybersecurity Teams & SOC Analysts** - Looking to automate SIEM alert enrichment
* **IT Security Professionals** - Wanting to integrate MITRE ATT&CK intelligence into ticketing systems
* **Anyone using n8n and vector stores** - Interested in building AI-powered security workflows

## What problem does this workflow solve?

Security teams receive **high volumes of raw SIEM alerts** lacking actionable context. Manually investigating every alert is **time-consuming** and can lead to **delayed response times**.

This workflow addresses this by:

* **Automatically enriching SIEM alerts** with MITRE ATT&CK TTPs
* **Tagging & categorizing alerts** based on known attack techniques
* **Providing remediation steps** for response teams

## Workflow Capabilities

1. **Collect SIEM alerts** from security collectors or sensors
2. **Query Qdrant vector store** containing MITRE ATT&CK techniques
3. **Extract relevant TTPs (Tactics, Techniques & Procedures)** from alerts
4. **Generate remediation steps** using AI-based enrichment
5. **Update Zendesk tickets** with threat intelligence & recommended actions
6. **Provide structured alert data** for further automation or reporting

## Setup Guide

### Prerequisites

* **n8n instance** (cloud or self-hosted)
* **Pinecone vector store** with embedded MITRE ATT&CK data
* **OpenAI API key** (for AI-based threat processing)
* Clean Mitre data Python script
* Refined Mitre data
* Complete Mitre data

### Setup Steps

1. **Embed MITRE ATT&CK data in Pinecone (Supabase or Qdrant possible)**
   * This workflow **imports MITRE ATT&CK data from Google Drive** and **loads it into Pinecone**
   * Data is **vectorized using OpenAI embeddings** for quick searching

2. **Deploy n8n chatbot**
   * Chatbot **receives SIEM alerts** and forwards them to the AI processing pipeline
   * Alerts are analyzed using an **AI agent trained on MITRE ATT&CK**

3. **Enrich SIEM alarm tickets**
   * Workflow extracts **MITRE ATT&CK techniques** from alerts
   * **Remediation steps** can be sent as internal notes for SOC teams

## Why this workflow is powerful

* **Time-saving**: Automates **alert triage & classification**
* **Improved security posture**: Helps SOC teams **respond faster** to threats
* **Leverages AI & vector search**: Uses **LLM-based enrichment** for **real-time context**
* **Works cross-platform**: Supports **n8n cloud, self-hosted, and Pinecone**



------



## MITRE ATT&CK와 n8n을 활용한 SIEM 알림 강화 자동화(ko)



## 이 워크플로우는 다음과 같은 분들에게 적합합니다:

* **사이버보안팀 & SOC 분석가** - SIEM 알림 강화를 자동화하고자 하는 분

* **IT 보안 전문가** - MITRE ATT&CK 인텔리전스를 티켓팅 시스템에 통합하고자 하는 분

* **n8n과 vector store를 사용하는 모든 사람** - AI 기반 보안 워크플로우를 구축하고자 하는 분

  

## 이 워크플로우는 어떤 문제를 해결하나요?

보안팀은 실행 가능한 맥락이 부족한 **대량의 원시 SIEM 알림**을 받습니다. 모든 알림을 수동으로 조사하는 것은 **시간이 많이 소요**되며 **대응 시간 지연**을 초래할 수 있습니다. 

이 워크플로우는 다음과 같은 방법으로 이 문제를 해결합니다:

* MITRE ATT&CK TTP로 **SIEM 알림 자동 강화**

* 알려진 공격 기술을 기반으로 **알림 태깅 & 분류**

* 대응팀을 위한 **해결 단계 제공**

  

## 워크플로우 기능

1. 보안정보수집기 또는 보안센서로부터 **SIEM 알림 수집**
2. MITRE ATT&CK 기술이 포함된 **Qdrant 벡터 저장소 쿼리**
3. 알림에서 **관련 TTP(전술, 기술 & 절차) 추출**
4. AI 기반 강화를 사용하여 **해결 단계 생성**
5. 위협 인텔리전스 & 권장 조치로 **Zendesk 티켓 업데이트**
6. 추가 자동화 또는 보고를 위한 **구조화된 알림 데이터 제공**



## 설정 가이드

### 사전 요구사항

* **n8n 인스턴스** (클라우드 또는 자체 호스팅)

* MITRE ATT&CK 데이터가 임베딩된 **Pinecone 벡터 저장소**

* (AI 기반 위협 처리를 위한) **OpenAI API 키**

* Clean Mitre 데이터 Python 스크립트

* 정제된 Mitre 데이터

* 전체 Mitre 데이터

  

### 설정 단계

1. **MITRE ATT&CK 데이터를 Pinecone에 임베딩(Supabase 또는 Qdrant 가능)**

   * 이 워크플로우는 **Google Drive**에서 MITRE ATT&CK 데이터를 가져와 **Pinecone에 로드**합니다.
   * 데이터는 빠른 검색을 위해 **OpenAI 임베딩을 사용하여 벡터화**됩니다.

2. **n8n 챗봇 배포**

   * 챗봇은 **SIEM 알림**을 수신하여 AI 처리 파이프라인으로 전송합니다.
   * 알림은 **MITRE ATT&CK로 훈련된 AI 에이전트**를 사용하여 분석됩니다.

3. **SIEM 알람 티켓 강화**

   * 워크플로우는 알림에서 **MITRE ATT&CK 기술**을 추출합니다.

   * **해결 단계**는 SOC 팀을 위한 내부 노트로 전송할 수 있습니다.

     

## 이 워크플로우가 강력한 이유

* **시간 절약**: **알림 분류 & 분류** 자동화
* **보안 태세 개선**: SOC 팀이 위협에 **더 빠르게 대응**하도록 지원
* **AI & 벡터 검색 활용**: **실시간 맥락**을 위한 **LLM 기반 강화** 사용
* **플랫폼 간 작동**: **n8n 클라우드, 자체 호스팅 및 Pinecone** 지원

