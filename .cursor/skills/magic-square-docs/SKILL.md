---
name: magic-square-docs
description: >-
  MagicSquare 세션 Report·Transcript·Checklist 문서를 번호 규칙에 맞게 생성한다.
  export-session, Report, Prompting, 세션 보고, transcript, checklist, Export 요청 시.
---

# MagicSquare Docs Skill

MagicSquare 세션 **문서화** — Report · Transcript · Checklist 생성 가이드.

---

## SSOT

| 파일 | 용도 |
|------|------|
| `.cursor/commands/export-session.md` | Export 절차·번호 규칙 |
| `.cursorrules` | 프로젝트·도메인 메타 |
| `docs/PRD.md` | PRD (없으면 `.cursorrules`) |

---

## Export (`/export-session`)

**추가 입력 없이 즉시 실행.** 현재 채팅에서 주제·산출물·Transcript 자동 추출.

### 번호 규칙

1. `Report/` · `Prompting/` 의 `NN.*` 확인
2. 최대 번호 + 1 → **2자리** (`05`)
3. 기존 번호 **덮어쓰기 금지**

### 생성 파일 (2개 필수)

| 파일 | 템플릿 |
|------|--------|
| `Report/NN.REPORT.md` | [report-template.md](./templates/report-template.md) |
| `Prompting/NN.Export-Transcript.md` | [transcript-template.md](./templates/transcript-template.md) |

---

## Checklist

세션·Phase 완료 시 [checklist-template.md](./templates/checklist-template.md) 기준으로 자체 점검. 별도 파일 저장은 `/export-session` 또는 사용자 요청 시.

---

## 문서 톤

- **한국어** — 설명·메타·주석
- 제목: `# MagicSquare_1004 — {세션 주제}`
- 마지막 줄: `*본 문서는 {경로} — …입니다.*`
- 솔루션名 남용 금지 — **과거 행동·비용·판정** 중심 (Mom Test 연계 시)

---

## 템플릿 위치

| 템플릿 | 경로 |
|--------|------|
| Report | `.cursor/skills/magic-square-docs/templates/report-template.md` |
| Transcript | `.cursor/skills/magic-square-docs/templates/transcript-template.md` |
| Checklist | `.cursor/skills/magic-square-docs/templates/checklist-template.md` |

---

## ARRR 세션 Checklist 연계

| Phase | Checklist 섹션 |
|-------|----------------|
| RED (Plan/Skeleton) | TDD RED |
| GREEN | TDD GREEN |
| Golden Master | Fixture |
| REFACTOR | Refactor |
| Export | Docs |

---

## 금지

| 금지 | 이유 |
|------|------|
| Report만 / Transcript만 | Export 2개 필수 |
| 번호 없는 `REPORT.md` | 추적 불가 |
| 사용자에게 주제·번호 질문 | 무인 Export |
