# Forge

**Forge** is a smart, language-agnostic scaffolding and code generation tool. Inspired by Rails generators and modern CLI tools, Forge empowers you to scaffold projects, generate boilerplate code, and safely modify existing files using declarative configuration and comment-based markers.


---
## ✨ Features

### Template Usage and File Generation

- 🧱 **Project scaffolding** with `forge new` using customizable templates
- 🧠 **Smart file modification** with `forge generate` and code injection
- 🧭 **Marker-based insertion** (`# forge:region:start|end`) that is idempotent and editable

### Template Creation and Management

- 🔍 **Template discovery** via `.forge/templates/`, supports per-project and global resolution
- 🌐 **Git-based templates** for shared or organization-level scaffolding
- 🧩 **Declarative configuration** with `forge.meta.yaml` for file and injection rules
- 🛠️ **Templating engine** powered by Jinja2 with support for custom filters

---
## 🚀 Getting Started


### Installation (coming soon)

```bash
pip install forge-cli
```

Or clone locally:

```bash
git clone https://github.com/yourname/forge
cd forge
python -m forge.cli
```

### Creating a New Project

```bash
forge new project myapp --template=typer-cli
```

### Creating a New Template

```bash
forge new template my-template --template=
```

### Generating a Command

```bash
forge generate command greet
```
This creates `commands/greet.py` and injects it into your CLI registry using predefined marker regions.