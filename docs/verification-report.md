# GitHub Pages（Hugo）出力検証レポート

**検証日**: 2026-02-23  
**対象**: waybackmachine / output の元データと、Hugo による GitHub Pages 出力の整合性

---

## 概要

- **output**（WordPress エクスポート由来）の全ページ・投稿は **content** に取り込まれており、Hugo で正しく出力されています。
- **waybackmachine/old** および **waybackmachine/new** の記事は、スクリプト `scripts/wayback_to_hugo.py` により **content/posts/** へ一括移行済みです（old を優先、既存スラッグはスキップ）。固定ページ風の donation / page-213 / giars-howto も投稿として移行し、旧 URL 用リダイレクトを hugo.toml に追加済みです。
- 1件のみ不整合があり修正済み: 投稿 `fivescup-open-1` の URL が `fivescup-open-#1` になっていたため、`slug` を明示して `/posts/fivescup-open-1/` で出力するよう修正しました。

---

## 1. 元データの整理

### 1.1 output/（WordPress → Markdown）

| 種別 | スラッグ | content 対応 | Hugo 出力 |
|------|----------|-------------|-----------|
| ページ | about-fivescup | ✅ content/pages/about-fivescup/ | /about-fivescup/ |
| ページ | rules | ✅ content/pages/rules/ | /rules/ |
| 下書き | id-85 | 除外（excluded_from_build） | 出力なし |
| 投稿 | fivescup-challenge-season11 | ✅ | /posts/fivescup-challenge-season11/ |
| 投稿 | fivescup-challenge-season11-結果 | ✅ | /posts/fivescup-challenge-season11-結果/ |
| 投稿 | fivescup-challenge-season11-技術検証結果 | ✅ | /posts/fivescup-challenge-season11-技術検証結果/ |
| 投稿 | fivescup-survive-season1 | ✅ | /posts/fivescup-survive-season1/ |
| 投稿 | fivescup-survive-season1-結果 | ✅ | /posts/fivescup-survive-season1-結果/ |
| 投稿 | fivescup-open-1 | ✅（slug 修正済み） | /posts/fivescup-open-1/ |
| 投稿 | fivescup-experimental-season1 | ✅ | /posts/fivescup-experimental-season1/ |
| 投稿 | fivescup-experimental-season1-結果 | ✅ | /posts/fivescup-experimental-season1-結果/ |
| 投稿 | fivescup-experimental-season2 | ✅ | /posts/fivescup-experimental-season2/ |

**結論**: output の有効ページ 2 件・投稿 9 件はすべて content に存在し、Hugo で期待どおり出力されています。

### 1.2 waybackmachine/

- **waybackmachine/old**: 投稿相当の HTML 33 件（カテゴリ・タグ・author 等を除く）。
- **waybackmachine/new**: 投稿相当の HTML 67 件。合計 78 スラッグ（重複除く）。
- **content との対応**:
  - 投稿 74 件は `content/posts/` に存在し、Hugo で `/posts/:slug/` として出力済み。
  - `about-fivescup`, `rules` は wayback にもあるが **固定ページ** として `content/pages/` にあり、`/about-fivescup/`, `/rules/` で出力済み。
  - `fives-cup-open-1` は `fivescup-open-1` に統合（ALREADY_MIGRATED_AS）のため投稿は1件。旧 URL 用に `hugo.toml` で `/posts/fives-cup-open-1/` → `/posts/fivescup-open-1/` のリダイレクトを追加済み。
  - `feed` は WordPress の RSS 用 URLのため、Hugo では対応しない（RSS 対応は不要）。
- **結論**: wayback の全ページ相当は、投稿は content/posts、固定ページは content/pages でカバーされ、Hugo で正しく出力されています。

---

## 2. Hugo ビルド結果

- コマンド: `hugo --minify`
- 出力: **Pages 116**（トップ・固定 2・投稿 81・タグ/カテゴリ一覧等）
- 固定ページ: `/about-fivescup/`, `/rules/`
- 投稿: `/posts/:slug/` 形式で 81 件（permalinks 設定どおり）。wayback 移行分を含む全投稿が出力されています。

---

## 3. GitHub Pages 実機確認

| URL | 結果 |
|-----|------|
| https://fivescup.github.io/ | 200 OK |
| https://fivescup.github.io/about-fivescup/ | 200 OK |
| https://fivescup.github.io/rules/ | 確認（タイムアウトの可能性あり） |
| https://fivescup.github.io/posts/fivescup-challenge-season11/ | 200 OK |
| https://fivescup.github.io/posts/fivescup-open-1/ | 修正前は 404（slug 修正後はビルドで /posts/fivescup-open-1/ を出力） |
| https://fivescup.github.io/posts/fivescup-open-%231/ | 修正前は 200（同一記事の別 URL） |

**注意**: 本レポート時点では、`slug` 修正を反映したビルドを GitHub に push していないため、公開サイトで `/posts/fivescup-open-1/` が 200 になるかは、push および GitHub Actions ビルド後に再確認してください。

---

## 4. 実施した修正

- **ファイル**: `content/posts/fivescup-open-1/index.md`
  - **内容**: フロントマターに `slug: "fivescup-open-1"` を追加。
  - **理由**: タイトル "FIVESCUP OPEN #1" から Hugo がスラッグを `fivescup-open-#1` と生成し、リダイレクト先と一致せず 404 になっていたため。
- **ファイル**: `hugo.toml`（wayback 旧 URL 用リダイレクト追加）
  - `/posts/fives-cup-open-1/` → `/posts/fivescup-open-1/`（旧 WordPress スラッグ）

---

## 5. リダイレクト（旧 WordPress URL）について

- `hugo.toml` に `/2017/07/24/fivescup-open-1/` → `/posts/fivescup-open-1/` 等のリダイレクトが定義されています。
- GitHub Pages の標準では、Hugo が生成するリダイレクト用の仕組みがそのまま使えない場合があります。旧 URL にアクセスした場合の挙動は、デプロイ方法（GitHub Actions で `public` を出力しているか等）に依存するため、必要に応じて GitHub の設定や `404.html` でのリダイレクト等を検討してください。

---

## 6. 結論

| 項目 | 結果 |
|------|------|
| output の全ページが Hugo で出力されているか | ✅ はい（2 ページ） |
| output の全投稿が Hugo で出力されているか | ✅ はい（9 投稿・slug 修正済み） |
| wayback の全ページが content でカバーされ Hugo で出力されているか | ✅ はい（投稿 81・固定 2・リダイレクト追加済み） |
| 修正が必要だった点 | fivescup-open-1 の `slug` 明示、旧 URL 用リダイレクト 1 件（fives-cup-open-1）追加 |

**注意**: GitHub Pages の標準静的ホスティングでは、`hugo.toml` の `[[redirects]]` がそのまま適用されない場合があります。リダイレクトを効かせるには、デプロイ方法（GitHub Actions で `_redirects` を出力する等）の対応が必要です。

---

## 7. 全ページ検証（デザイン・リンク・タグ）— 2026-02-23 追記

### 7.1 実施内容

- **スクリプト**: `scripts/verify-pages.py`
- **対象**: ビルド済み `public/**/index.html` 全 100 ページ
- **確認項目**:
  - 内部リンク: 同一サイト内の `href` を解決し、対象ファイルの存在を確認
  - タグ: `<title>`, `rel="canonical"`, `charset`, `viewport` の有無

### 7.2 結果

| 項目 | 結果 |
|------|------|
| リンク切れ | ✅ なし（修正後） |
| title / canonical / charset / viewport | ✅ 全ページに存在 |

### 7.3 実施した修正

- **`../rule/` → `../../rules/`**: 2v2-s1, 2v2-s2, 2v2-s3（大会共通ルールへの誤リンク）
- **`../rule/steamid/` → `../steamid/`**: 2v2-s2, 2v2-s3, fivescup-challenge-season3, fivescup-challenge-season5, fivescup-beginning-season4（SteamID 確認方法への誤リンク）
- **`../2v2-s1-result/` → `../2v2-s1/`**: about, 2v2-s1, 2v2-s2, 2v2-s2-result（存在しないスラッグの差し替え）
- **検証スクリプト**: 内部リンク解決時に `unquote` を適用し、日本語等を含む URL を正しく解決するよう変更

### 7.4 デザイン・コンテンツ上の注意点

- **レイアウト**: 全ページで `baseof.html` を共有（`site-header`, `main`, `site-footer`）しており、デザインの枠組みは統一されています。
- **一部投稿の本文**: WordPress 移行由来の「Back to Top」や JavaScript 断片、著作権表記がそのまま Markdown として出力されている箇所があります（例: ban）。必要に応じて `content/posts/**/index.md` の該当部分を手動で削除・編集してください。
- **baseURL**: 現在 `hugo.toml` の `baseURL` は `https://fivescup.github.io/` です。リポジトリ名をサブパスにする（例: `.../fivescup/`）場合は、`baseURL` をそれに合わせて変更してください。
