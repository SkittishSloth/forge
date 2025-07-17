# Forge Project TODO.md

A smart, language-agnostic scaffolding and code generation tool. Inspired by Rails' generators and built for maintainable CLI scaffolding, Forge supports declarative file generation, smart code injection using comment markers, and template discovery across multiple projects and languages.

---

## ✅ Phase 1: Core MVP (Scaffolding Engine)

### Project Setup
- [ ] Scaffold CLI layout (`forge` entrypoint)
- [ ] Implement `forge new project <name>`
- [ ] Implement `forge new template <name>`
  - [ ] Render template files with Jinja2
  - [ ] Write output to destination directory
- [ ] Implement `forge generate <generator> <name>`
  - [ ] Load matching sub-generator (e.g. `command`)
  - [ ] Render target files with templated paths

### Template System
- Implement the template loading mechanism (see /docs/templates.md for details)
  - [ ] Load `.j2` templates from disk
  - [ ] Basic Jinja2 rendering with `dict` values
  - [ ] Add custom filters: `snake_case`, `kebab_case`, `fqn_to_path`
  - [ ] Template values from CLI args or config

### Directory & File Layout
- Implement the template discovery logic (see /docs/file_layout.md for details)
  - [ ] Define `.forge/templates/` folder per project
  - [ ] Walk upward to discover project-level templates
  - [ ] Fallback to `$HOME/.forge/templates/`

---

## 🧠 Phase 2: Smart Code Injection Engine

### Marker-Based Modification
- [ ] Define and parse `forge:<region>:start|end` markers
- [ ] Insert block content into marker region
- [ ] Support `block` and `block_per_item` modes
- [ ] Prevent duplication (idempotent insert)
- [ ] Item-level block support: `forge:<region>:<name>:start|end`

### Data Sources
- [ ] Source values from directory listings (e.g. `commands/*.py`)
- [ ] Filter by filename, extension, glob pattern
- [ ] Future: support file annotations (e.g. `forge:type:command`)

### Config for Injection
- [ ] Define and parse `modifications:` within the template's `forge.meta.yaml`
- [ ] Specify: file, region, template, value source, mode

---

## 🧩 Phase 3: Declarative Generator Config (forge.meta.yaml)
- [ ] Define and support a `files:` section within a template's `forge.meta.yaml` for file creation
  - [ ] Path templating
  - [ ] Conditional generation (`when:` support)
- [ ] Support `modifications:` section for file injection
  - [ ] Template references per block
  - [ ] Support static and dynamic values

---

## 🛰️ Phase 4: Remote Templates
- [ ] Support Git-based templates (`gh:user/repo`)
  - [ ] Download and cache to `~/.forge/templates/remote/`
  - [ ] Optional submodule support
  - [ ] Add `forge template install`, `list`, `update`

---

## 🔮 Phase 5: UX and Advanced Features (MVP2 or later)
- [ ] Add `FORGE_TEMPLATE_PATHS` support
- [ ] Interactive prompt for missing template values
- [ ] Named presets / variants for generators
- [ ] Registry for user-defined commands / template sets
- [ ] Plugin system (entry-points, local modules, or scripts)

---

## 🧪 Testing & Tooling
- [ ] Unit test: file generation from template
- [ ] Unit test: injection with marker blocks
- [ ] CLI test: `forge new`, `forge generate`
- [ ] Validate idempotency of inject logic

---