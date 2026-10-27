"""Validação estrutural e ZIP privado, usando apenas a biblioteca padrão."""

import argparse
import json
import re
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "empresas", "escrituracao", "plano-contas", "periodos", "consultas",
    "notas-parceiros", "conciliacao", "demonstracoes", "simples-nacional", "fechamento",
}


def validate(release=False):
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    assert manifest["name"] == "nolivro", "O identificador permanente deve ser nolivro."
    assert manifest["displayName"] == "noLivro"
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Versão inválida."
    assert manifest["description"] and manifest["author"]["name"]
    mcp = json.loads((ROOT / ".mcp.json").read_text())
    assert mcp == {"mcpServers": {"nolivro": {
        "type": "http", "url": "https://mcp.nolivro.com.br/mcp",
    }}}, "A configuração deve conter somente o endpoint público aprovado."
    files = [ROOT / ".claude-plugin/plugin.json", ROOT / ".mcp.json", ROOT / "README.md"]
    readme = re.sub(r"```.*?```", "", files[-1].read_text(), flags=re.S)
    assert len(readme.split()) >= 40, "README precisa explicar uso e dados."
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    assert {p.parent.name for p in skills} == SKILLS, "Conjunto de skills incompleto."
    for path in skills:
        text = path.read_text()
        parts = text.split("---", 2)
        assert len(parts) == 3 and not parts[0].strip(), f"Frontmatter ausente: {path}"
        name = re.search(r"^name: (.+)$", parts[1], re.M)
        description = re.search(r"^description: (.+)$", parts[1], re.M)
        assert name and name[1] == path.parent.name, f"Nome divergente: {path}"
        assert description and description[1].strip(), f"Descrição ausente: {path}"
        assert parts[2].strip(), f"Skill vazia: {path}"
    files += skills + sorted((ROOT / "docs").glob("*.md"))
    files += [ROOT / "assets/nolivro.svg"]
    license_file = ROOT / "LICENSE"
    licensed = bool(manifest.get("license")) or (
        license_file.is_file() and bool(license_file.read_text().strip())
    )
    if license_file.is_file():
        files.append(license_file)
    for path in files:
        assert path.is_file() and not path.is_symlink(), f"Arquivo inválido: {path}"
        assert not any(p.is_symlink() for p in path.parents if p != ROOT), "Link simbólico."
    if release:
        assert licensed, "Publicação bloqueada: responsável ainda precisa escolher a licença."
    elif not licensed:
        print("Pendente para publicação: licença. O teste privado pode continuar.")
    print(f"Estrutura válida: {len(skills)} skills, MCP HTTPS e manifesto {manifest['version']}.")
    return manifest, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["check", "package"])
    parser.add_argument("--release", action="store_true", help="Exigir licença declarada.")
    args = parser.parse_args()
    try:
        manifest, files = validate(args.release)
        if args.action == "package":
            destination = ROOT / "dist"
            destination.mkdir(exist_ok=True)
            archive = destination / f"nolivro-claude-plugin-{manifest['version']}.zip"
            with ZipFile(archive, "x", compression=ZIP_DEFLATED) as package:
                for path in files:
                    package.write(path, path.relative_to(ROOT).as_posix())
            print(f"Pacote para teste privado: {archive}")
    except (AssertionError, OSError, ValueError, KeyError) as error:
        print(f"Falha: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
