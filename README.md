# FIVESCUP

S5Works が運営する CS2/VALORANT イベント「FIVESCUP」のサイトです。  
WordPress から GitHub Pages（Hugo）へ移行しました。

- **サイト**: https://fivescup.github.io/
- **リポジトリ**: https://github.com/FIVESCUP/fivescup.github.io

## 開発

### 必要なもの

- [Hugo](https://gohugo.io/installation/)（extended 推奨）

### ローカルでプレビュー

```bash
hugo server
```

ブラウザで http://localhost:1313 を開きます。

### ビルド

```bash
hugo --minify
```

生成された静的ファイルは `public/` に出力されます。

## GitHub Pages の設定

1. リポジトリの **Settings** → **Pages**
2. **Build and deployment** の **Source** で **GitHub Actions** を選択

`master` ブランチへ push（またはマージ）すると、GitHub Actions が Hugo をビルドし、GitHub Pages にデプロイします。

## ディレクトリ構成

- `content/` - 固定ページ（`pages/`）と投稿（`posts/`）の Markdown
- `layouts/` - Hugo テンプレート
- `static/` - 静的ファイル（画像など）
- `hugo.toml` - Hugo 設定

## Phase 8: 元データ・補助資産の削除（任意・確認後）

GitHub Pages で全ページ・リンク・画像に問題がないことを確認したあと、リポジトリから次を削除してリポジトリを軽量化できます。

- `output/` ディレクトリ一式
- `waybackmachine/` ディレクトリ一式
- `s5worksfivescup.WordPress.2026-02-23.xml`
- `docs/` ディレクトリ一式（コンテンツ一覧・検証レポート等）
- `scripts/` ディレクトリ一式（移行・検証用スクリプト）

削除後も Git 履歴には残るため、必要なら過去のコミットから復元できます。恒久バックアップが必要な場合は、削除前にタグや ZIP で別途アーカイブすることを推奨します。

```bash
git rm -r output waybackmachine docs scripts s5worksfivescup.WordPress.2026-02-23.xml
git commit -m "chore: remove original export data and auxiliary assets (output, waybackmachine, docs, scripts, XML)"
git push
```

※ 本 README は Phase 8 向けに簡素化済みです。

## ライセンス

コンテンツの利用については S5Works / FIVESCUP にご確認ください。
