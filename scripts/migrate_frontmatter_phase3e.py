"""Phase 3e — standardize frontmatter on 27 not-yet-migrated atomic notes.

Preserves body content verbatim. Replaces the top YAML frontmatter block
(or inserts one if absent) with the canonical schema used by Phase 3b/c/d:

    ---
    ref: "[N]" | ""
    citekey: "<Filename>"
    title: "..."
    authors: "..."
    year: NNNN
    journal: "..."
    doi: "..."
    zotero_key: "..."
    zotero_status: verified | partial | not_in_zotero | mismatch
    last_verified: "2026-06-01"
    tags:
      - Verified
      - ...
    ---

For anomalous citekeys (OpenAI2021, Grieves2026) zotero_status is set to
not_in_zotero / mismatch and an inline `⚠` note prepended to the body.
"""

from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(r"H:\phd\6.pjt\LR1\papers\01_source")
LAST_VERIFIED = "2026-06-01"

# (citekey, ref, title, authors, year, journal, doi, zotero_key, status, extra_tags, anomaly_note)
RECORDS = [
    ("Adibi2024", "", "Sensor-driven digital twin platforms for smart environments: A systematic review and a proposed framework", "Sasan Adibi, Abbas Rajabifard, Davood Shojaei, Nilmini Wickramasinghe", 2024, "Sensors", "10.3390/s24092793", "HHRE3QTR", "verified", ["Digital-Twin", "Healthcare", "Smart-Environment", "Review"], None),
    ("Boje2020", "[5]", "Towards a semantic Construction Digital Twin: Directions for future research", "Calin Boje, Annie Guerriero, Sylvain Kubicki, Yacine Rezgui", 2020, "Automation in Construction", "10.1016/j.autcon.2020.103179", "6RG2MC52", "verified", ["Digital-Twin", "Construction", "Semantic", "Lifecycle"], None),
    ("Fuller2020", "[29]", "Digital Twin: Enabling technologies, challenges and open research", "Aidan Fuller, Zhong Fan, Charles Day, Chris Barlow", 2020, "IEEE Access", "10.1109/ACCESS.2020.2998358", "SSR5IGBW", "verified", ["Digital-Twin", "Foundation", "Survey"], None),
    ("Glaessgen2012", "[55]", "The digital twin paradigm for future NASA and U.S. Air Force vehicles", "Edward Glaessgen, David Stargel", 2012, "AIAA Conference (53rd Structures, Structural Dynamics, and Materials)", "10.2514/6.2012-1818", "8B7R5BZU", "verified", ["Digital-Twin", "Aerospace", "Foundation"], None),
    ("Götz2022", "", "Exploring applicability, interoperability and integrability of Blockchain-based digital twins for asset life cycle management", "Carl Sebastian Götz, Pelle Karlsson, Ibrahim Yitmen", 2022, "Smart and Sustainable Built Environment", "10.1108/SASBE-08-2020-0115", "56AMFECQ", "verified", ["Digital-Twin", "Blockchain", "Asset-Lifecycle"], None),
    ("Grieves2026", "[56]", "Front Running Simulation: A Digital Twin Framework for Real-Time Replication, Prediction, and Goal Navigation", "Michael Grieves", 2026, "Manuscript / Preprint (citekey body) — Zotero record points to Grieves & Vickers 2017 chapter", "10.1007/978-3-319-38756-7_4", "UXYJS9VB", "mismatch", ["Digital-Twin", "Foundation", "Mismatch-Flag"], "⚠ Citekey/body describe Grieves 2026 'Front Running Simulation' paper, but matched Zotero record (UXYJS9VB) is the 2017 Grieves & Vickers chapter. Resolve by either renaming this file to `GrievesVickers2017` or importing the actual 2026 FRS paper."),
    ("Hosamo2022", "", "A review of the digital twin technology in the AEC-FM industry", "Haidar Hosamo Hosamo, Hassan Hosamo, Mazen A. Al-Sinan, Khalid Al-Tarazi", 2022, "Advances in Civil Engineering", "10.1155/2022/2185170", "3QSAUVYC", "verified", ["Digital-Twin", "AEC-FM", "Review"], None),
    ("Jones2020", "[71]", "Characterising the Digital Twin: A systematic literature review", "David Jones, Chris Snider, Aydin Nassehi, Jason Yon, Ben Hicks", 2020, "CIRP Journal of Manufacturing Science and Technology", "10.1016/j.cirpj.2020.02.002", "9FNSJ6UJ", "verified", ["Digital-Twin", "Foundation", "Manufacturing", "Review"], None),
    ("Kritzinger2018", "[28]", "Digital Twin in manufacturing: A categorical literature review and classification", "Werner Kritzinger, Matthias Karner, Georg Traar, Jan Henjes, Wilfried Sihn", 2018, "IFAC-PapersOnLine", "10.1016/j.ifacol.2018.08.474", "J4XB34RN", "verified", ["Digital-Twin", "Foundation", "Classification"], None),
    ("Liu&Meng2021", "[76]", "Digital twin-based safety risk coupling of prefabricated building hoisting", "Zhansheng Liu, Yi Meng, Zhongmin Xing, Anshan Jiang", 2021, "Sensors", "10.3390/s21113583", "CDL7QW8N", "verified", ["Digital-Twin", "Safety", "Prefabrication"], None),
    ("Liu2020", "[75]", "A framework for an indoor safety management system based on digital twin", "Zhansheng Liu, Anshan Zhang, Jianxiang Wang", 2020, "Sensors", "10.3390/s20205771", "VI3RUWW4", "verified", ["Digital-Twin", "Safety", "Indoor"], None),
    ("Lu&Parlikad2020", "", "Developing a Digital Twin at building and city levels: Case study of West Cambridge campus", "Qiuchen Lu, Ajith Kumar Parlikad, Philip Woodall, Gishan Don Ranasinghe, Xiang Xie, Zhenglin Liang, Eirini Konstantinou, James Heaton, Jennifer Schooling", 2020, "Journal of Management in Engineering", "10.1061/(ASCE)ME.1943-5479.0000763", "7ANHKRIU", "verified", ["Digital-Twin", "Smart-Campus", "Multi-Scale"], None),
    ("Lu&Xie2020", "[9]", "Digital Twin-enabled anomaly detection for built asset monitoring in operation and maintenance", "Qiuchen Lu, Xiang Xie, Ajith Kumar Parlikad, Jennifer M. Schooling", 2020, "Automation in Construction", "10.1016/j.autcon.2020.103277", "PTY562CM", "verified", ["Digital-Twin", "Anomaly-Detection", "OandM"], None),
    ("Machado2023", "", "Construction 4.0 maturity model: A survey of academia and the construction industry", "F. V. Machado, F. T. Berssaneti", 2023, "Heliyon", "10.1016/j.heliyon.2023.e19390", "PTD7AVWZ", "verified", ["Construction-4.0", "Maturity-Model", "Survey"], None),
    ("MinQi2019", "", "Machine learning based digital twin framework for production optimization in petrochemical industry", "Qingfei Min, Yangguang Lu, Zhiyong Liu, Chao Su, Bo Wang", 2019, "International Journal of Information Management", "10.1016/j.ijinfomgt.2019.05.020", "WSF2RF5M", "verified", ["Digital-Twin", "Machine-Learning", "Petrochemical"], None),
    ("OpenAI2021", "", "Learning transferable visual models from natural language supervision (CLIP)", "Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever (OpenAI)", 2021, "arXiv preprint arXiv:2103.00020", "", "", "not_in_zotero", ["Foundation-Model", "Vision-Language", "Cross-Domain", "Not-In-Zotero"], "⚠ Body describes CLIP (Radford et al., 2021). Citekey `OpenAI2021` should likely be renamed to `Radford2021` and imported into Zotero. No matching Zotero record found in this session."),
    ("Pan&Zhang2021", "[19]", "A BIM-data mining integrated digital twin framework for advanced project management", "Yue Pan, Limao Zhang", 2021, "Automation in Construction", "10.1016/j.autcon.2021.103564", "YGJSXUXV", "verified", ["Digital-Twin", "BIM", "Project-Management"], None),
    ("Pome2023", "", "Digital twin for the built environment: Review of current research and future perspectives", "Andrea Giovanni Pomè, Cinzia Maria Luisa Signorini", 2023, "IOP Conference Series: Earth and Environmental Science", "10.1088/1755-1315/1176/1/012003", "NURYJTQW", "verified", ["Digital-Twin", "Built-Environment", "Review"], None),
    ("RajratnaKharat2018", "", "Detection of cracks on concrete surfaces using digital image processing", "Rajratna Kharat, Vikas Bavane", 2018, "Zenodo (deposited 2018)", "10.5281/zenodo.1493930", "9SMJBZXV", "verified", ["Computer-Vision", "Crack-Detection", "Low-Quality-Venue"], None),
    ("Rasheed2020", "[54]", "Digital Twin: Values, Challenges and Enablers From a Modeling Perspective", "Adil Rasheed, Omer San, Trond Kvamsdal", 2020, "IEEE Access", "10.1109/ACCESS.2020.2970143", "MKZ3HU7D", "verified", ["Digital-Twin", "Modeling", "Foundation"], None),
    ("Sun2023", "", "Industry 4.0 and digital twin in the context of the COVID-19 pandemic: A bibliometric review", "Tianqi Sun, Sicheng He, Zheng Li", 2023, "DIGITAL HEALTH", "10.1177/20552076221149651", "RA62TL5J", "verified", ["Digital-Twin", "Industry-4.0", "Bibliometric"], None),
    ("Tao2018", "", "Digital twin-driven prognostics and health management for complex equipment", "Fei Tao, Meng Zhang, Yushan Liu, A. Y. C. Nee", 2018, "CIRP Annals", "10.1016/j.cirp.2018.04.055", "FDTN2LDT", "verified", ["Digital-Twin", "PHM", "Manufacturing"], None),
    ("Tao2019", "[30]", "Digital twin in industry: State-of-the-art", "Fei Tao, He Zhang, Ang Liu, A. Y. C. Nee", 2019, "IEEE Transactions on Industrial Informatics", "10.1109/TII.2018.2873186", "MERRUE6E", "verified", ["Digital-Twin", "Foundation", "Industry"], None),
    ("Teisserenc2021", "", "Adoption of blockchain technology through digital twins in the construction industry 4.0: A PESTELS approach", "Benjamin Teisserenc, Samad Sepasgozar", 2021, "Buildings", "10.3390/buildings11120670", "EN7S2R5T", "verified", ["Digital-Twin", "Blockchain", "Construction-4.0"], None),
    ("Wang2022", "[1]", "Digital twin-enabled built environment sensing and monitoring through semantic enrichment of BIM with SensorML", "Mengfei Wang, Vincent J. L. Gan, Zhen-Zhong Hu, Yu-Cheng Liu", 2022, "Automation in Construction", "10.1016/j.autcon.2022.104625", "BZQ3K5G8", "verified", ["Digital-Twin", "BIM", "SensorML", "Semantic"], None),
    ("Zhao2023", "", "Blockchain-based decentralized digital twin for smart city resilience", "Yuxi Zhao, Zhenglin Chen, Fan Xue", 2023, "Automation in Construction", "10.1016/j.autcon.2022.104645", "QZPIVMLR", "verified", ["Digital-Twin", "Blockchain", "Smart-City"], None),
    ("Fu2026", "[99]", "A review of uncertainty quantification in digital twins for engineering applications", "Yifan Fu, Yujie Zhao, Yan Zhu, Hongchao Zheng, Yang Lu", 2026, "Archives of Computational Methods in Engineering", "10.1007/s11831-025-10332-6", "K3PFBG7P", "partial", ["Digital-Twin", "Uncertainty-Quantification", "Review"], None),
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {tag}" for tag in items)


def build_frontmatter(rec) -> str:
    citekey, ref, title, authors, year, journal, doi, zkey, status, tags, anomaly = rec
    tag_block = yaml_list(["Verified" if status == "verified" else status.replace("_", "-").capitalize(), *tags])
    lines = [
        "---",
        f'ref: "{ref}"',
        f'citekey: "{citekey}"',
        f'title: "{title}"',
        f'authors: "{authors}"',
        f"year: {year}",
        f'journal: "{journal}"',
        f'doi: "{doi}"',
        f'zotero_key: "{zkey}"',
        f"zotero_status: {status}",
        f'last_verified: "{LAST_VERIFIED}"',
        "tags:",
        tag_block,
        "---",
        "",
    ]
    if anomaly:
        lines += [f"> ⚠ **VERIFICATION FLAG (2026-06-01):** {anomaly}", ""]
    return "\n".join(lines)


_FM_RE = re.compile(r"^---\r?\n.*?\r?\n---\r?\n?", re.DOTALL)
_FLAG_RE = re.compile(r"^> ⚠ \*\*VERIFICATION FLAG[^\n]*\n+", re.MULTILINE)


def migrate_file(rec) -> tuple[str, int]:
    citekey = rec[0]
    fpath = ROOT / f"{citekey}.md"
    if not fpath.exists():
        return f"MISSING {citekey}", 0
    raw = fpath.read_text(encoding="utf-8")
    # Strip leading YAML frontmatter if present
    m = _FM_RE.match(raw)
    body = raw[m.end():] if m else raw
    # Drop any previous verification-flag callout
    body = _FLAG_RE.sub("", body, count=1)
    new_fm = build_frontmatter(rec)
    out = new_fm + body.lstrip("\n")
    # Write UTF-8 BOMless
    fpath.write_text(out, encoding="utf-8", newline="\n")
    return f"OK {citekey}", len(out)


def main() -> None:
    for rec in RECORDS:
        status, size = migrate_file(rec)
        print(f"{status}  ({size} bytes)")


if __name__ == "__main__":
    main()
